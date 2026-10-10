"""Check per-animation before/after embeds in a pull request description."""

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


PLAYBACK_FIELDS = (
    'file', 'transportFile', 'sourceFile', 'animationName', 'performers',
    'duration', 'loop', 'previewRotation',
)
PLAYBACK_CHECK = '- [x] Playback verified in the rendered PR for every available side.'
SECTION = re.compile(r'^### Animation: `([^`\n]+)`\s*$', re.MULTILINE)
SIDE = re.compile(r'^(Before|After): (.+)$', re.MULTILINE)
ATTACHMENT_PATH = re.compile(
    r'/(?:user-attachments/assets|assets/\d+)/'
    r'[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}'
)


class Repository:
    def __init__(self, root):
        self.root = Path(root)

    def git(self, *arguments):
        return subprocess.check_output(
            ['git', *arguments], cwd=self.root, text=True, encoding='utf-8',
        )

    def retrieve_revision(self, reference):
        return self.git('rev-parse', '--verify', '--end-of-options', reference + '^{commit}').strip()

    def retrieve_snapshot(self, revision):
        files = set(self.git('ls-tree', '-r', '--name-only', '-z', revision).split('\0'))
        catalog = self.retrieve_document(revision, files, 'catalog.json', {})
        inventory = self.retrieve_document(revision, files, 'source-inventory.json', [])
        animations = {}
        covered = set()
        for entry in catalog.get('animations', []):
            paths = {entry[field] for field in ('file', 'transportFile', 'sourceFile') if entry.get(field)}
            animations[entry['id']] = Animation(paths, {field: entry.get(field) for field in PLAYBACK_FIELDS})
            covered.update(paths)
        for entry in inventory:
            if entry['file'] not in covered:
                paths = {entry['file']}
                if entry.get('runtimeExport'):
                    paths.add(entry['runtimeExport'])
                animations[entry['id']] = Animation(paths, {})
                covered.update(paths)
        # Include saved clips as they enter the project, ahead of catalog registration.
        for path in files - covered:
            if path.startswith('animations/') and path.endswith(('.blend', '.glb')) and path != 'animations/shared_scene_data.blend':
                animations[path] = Animation({path}, {})
        return animations

    def retrieve_document(self, revision, files, path, fallback):
        if path in files:
            document = json.loads(self.git('show', f'{revision}:{path}'))
        else:
            document = fallback
        return document

    def retrieve_changes(self, base, head):
        before = self.retrieve_snapshot(base)
        after = self.retrieve_snapshot(head)
        paths = set(self.git('diff', '--name-only', '--no-renames', '-z', base, head, '--').split('\0'))
        shared_changed = 'animations/shared_scene_data.blend' in paths
        changes = []
        for identifier in sorted(before.keys() | after.keys()):
            previous = before.get(identifier)
            current = after.get(identifier)
            assets = (previous.paths if previous else set()) | (current.paths if current else set())
            if previous != current or assets & paths or shared_changed:
                changes.append(Change(identifier, previous is not None, current is not None))
        return changes


@dataclass(frozen=True)
class Animation:
    paths: set
    playback: dict


@dataclass(frozen=True)
class Change:
    identifier: str
    before: bool
    after: bool


class Description:
    def __init__(self, body):
        # Examples and hidden comments serve as guidance, while visible embeds count.
        normalized = body.replace('\r\n', '\n').replace('\r', '\n')
        visible = re.sub(r'<!--.*?-->', '', normalized, flags=re.DOTALL)
        self.visible = re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', visible, flags=re.MULTILINE | re.DOTALL)

    def retrieve_sections(self):
        sections = {}
        headings = list(re.finditer(r'^#{1,3} .+$', self.visible, re.MULTILINE))
        for index, heading in enumerate(headings):
            match = SECTION.fullmatch(heading.group())
            if match:
                end = headings[index + 1].start() if index + 1 < len(headings) else len(self.visible)
                identifier = match[1]
                if identifier in sections:
                    raise ValueError(f'Duplicate animation comparison: {identifier}')
                sections[identifier] = self.visible[heading.end():end]
        return sections

    def validate(self, changes, base, head):
        sections = self.retrieve_sections()
        failures = []
        # Additional comparisons cover effects identified during shared/player review.
        expected = {change.identifier: change for change in changes}
        for identifier in sections.keys() - expected.keys():
            expected[identifier] = Change(identifier, True, True)
        for identifier, change in expected.items():
            if identifier in sections:
                section = sections[identifier]
                sides = list(SIDE.finditer(section))
                if [side[1] for side in sides] == ['Before', 'After']:
                    for index, (present, revision, label) in enumerate((
                        (change.before, base, 'Added in this PR'),
                        (change.after, head, 'Removed in this PR'),
                    )):
                        side = sides[index]
                        end = sides[index + 1].start() if index + 1 < len(sides) else len(section)
                        media = section[side.end():end]
                        if present:
                            if side[2].strip() != f'`{revision}`':
                                failures.append(f'{identifier}: {side[1]} must identify `{revision}`.')
                            if not self.contains_embed(media):
                                failures.append(f'{identifier}: {side[1]} needs a video attachment or animated GIF embed.')
                        elif side[2].strip() != label:
                            failures.append(f'{identifier}: {side[1]} must say {label}.')
                else:
                    failures.append(f'{identifier}: include one Before and one After section, in that order.')
                if PLAYBACK_CHECK.lower() not in {line.lower() for line in section.splitlines()}:
                    failures.append(f'{identifier}: verify playback and complete its checklist.')
            else:
                failures.append(f'{identifier}: add a comparison headed ### Animation: `{identifier}`.')
        return failures

    @staticmethod
    def contains_embed(content):
        candidates = [(url, True) for url in re.findall(
            r'^ {0,3}!\[[^\]\n]*\]\((https://[^\s)]+)\)[ \t]*$', content, re.MULTILINE,
        )]
        candidates.extend((url, False) for url in re.findall(
            r'^ {0,3}(https://\S+)[ \t]*$', content, re.MULTILINE,
        ))
        accepted = False
        for url, image in candidates:
            parts = urlsplit(url)
            attachment = parts.netloc == 'github.com' and ATTACHMENT_PATH.fullmatch(parts.path) is not None
            legacy = parts.netloc == 'user-images.githubusercontent.com'
            if image:
                accepted |= attachment or parts.path.lower().endswith('.gif')
            else:
                accepted |= attachment or (legacy and parts.path.lower().endswith(('.mp4', '.mov', '.webm')))
        return accepted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Base branch/reference; comparisons use its merge base with head.')
    parser.add_argument('--head', default='HEAD')
    parser.add_argument('--body', type=Path, help='Saved PR Markdown description to validate.')
    parser.add_argument('--event', type=Path, help='GitHub pull_request event JSON.')
    parser.add_argument('--list', action='store_true', help='Print the revisions and required animation IDs.')
    arguments = parser.parse_args()
    repository = Repository(Path.cwd())
    if arguments.event:
        request = json.loads(arguments.event.read_text(encoding='utf-8'))['pull_request']
        base_reference, head_reference = request['base']['sha'], request['head']['sha']
        body = request.get('body') or ''
    else:
        if arguments.base is None or (arguments.body is None and not arguments.list):
            parser.error('Provide --event, or --base with --body / --list.')
        base_reference, head_reference = arguments.base, arguments.head
        body = arguments.body.read_text(encoding='utf-8') if arguments.body else ''
    head = repository.retrieve_revision(head_reference)
    base = repository.git('merge-base', repository.retrieve_revision(base_reference), head).strip()
    changes = repository.retrieve_changes(base, head)
    print(f'Before: {base}\nAfter: {head}\nChanged animations: {len(changes)}')
    if arguments.list:
        for change in changes:
            print(change.identifier)
    else:
        failures = Description(body).validate(changes, base, head)
        for failure in failures:
            print(failure)
        if failures:
            print('See docs/pull-request-animation-media.md for the comparison format.')
        else:
            print('Animation comparison coverage and playback attestations pass.')
        return int(bool(failures))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Animation media check failed: {error}', file=sys.stderr)
        sys.exit(1)
