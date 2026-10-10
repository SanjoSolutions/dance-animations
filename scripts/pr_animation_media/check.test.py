"""Exercise comparison coverage using saved Git revisions and PR descriptions."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from check import Change, Description, PLAYBACK_CHECK, Repository


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name('check.py')
BASE = 'a' * 40
HEAD = 'b' * 40
VIDEO = 'https://github.com/user-attachments/assets/12345678-1234-1234-1234-123456789012'
GIF = '![After](https://example.com/after.gif)'


def comparison(identifier='step', before=None, after=None):
    before = before if before is not None else f'`{BASE}`\n\n{VIDEO}'
    after = after if after is not None else f'`{HEAD}`\n\n{GIF}'
    return f'### Animation: `{identifier}`\n\nBefore: {before}\n\nAfter: {after}\n\n{PLAYBACK_CHECK}\n'


class DescriptionTests(unittest.TestCase):
    def validate(self, body, changes=None):
        return Description(body).validate(changes or [Change('step', True, True)], BASE, HEAD)

    def test_existing_clip_accepts_playable_embed_forms_and_full_revisions(self):
        self.assertEqual(self.validate(comparison()), [])

    def test_windows_description_line_endings_preserve_playable_embeds(self):
        self.assertEqual(self.validate(comparison().replace('\n', '\r\n')), [])

    def test_each_changed_performer_requires_a_comparison(self):
        failures = self.validate(comparison(), [Change('step', True, True), Change('woman_step', True, True)])
        self.assertEqual(len(failures), 1)
        self.assertIn('woman_step', failures[0])

    def test_present_sides_require_media_and_current_revision(self):
        for after in (f'`{BASE}`\n\n{GIF}', f'`{HEAD}`'):
            with self.subTest(after=after):
                self.assertEqual(len(self.validate(comparison(after=after))), 1)

    def test_addition_and_removal_require_the_available_playback(self):
        addition = comparison(before='Added in this PR')
        removal = comparison(after='Removed in this PR')
        self.assertEqual(self.validate(addition, [Change('step', False, True)]), [])
        self.assertEqual(self.validate(removal, [Change('step', True, False)]), [])
        self.assertEqual(len(self.validate(addition)), 2)

    def test_visible_embeds_establish_coverage(self):
        examples = [f'<!--\n{comparison()}\n-->', f'```markdown\n{comparison()}\n```', f'~~~markdown\n{comparison()}\n~~~']
        for body in examples:
            with self.subTest(body=body):
                self.assertEqual(len(self.validate(body)), 1)

    def test_playback_verification_is_required_per_clip(self):
        body = comparison().replace('- [x]', '- [ ]')
        self.assertIn('verify playback', self.validate(body)[0])

    def test_static_images_and_download_links_request_a_playable_embed(self):
        for media in ('![After](https://example.com/after.png)', '[Video](https://example.com/after.mp4)',
                      '![After](C:/review/after.gif)', f'`{VIDEO}`', f'<!-- {GIF} -->',
                      f'    {VIDEO}', f'    {GIF}'):
            with self.subTest(media=media):
                failures = self.validate(comparison(after=f'`{HEAD}`\n\n{media}'))
                self.assertEqual(len(failures), 1)
                self.assertIn('needs a video', failures[0])

    def test_later_heading_keeps_unrelated_media_outside_comparison(self):
        body = comparison(after=f'`{HEAD}`') + f'\n## Other\n\n{VIDEO}\n'
        self.assertIn('needs a video', self.validate(body)[0])

    def test_duplicate_animation_sections_produce_an_actionable_error(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate animation comparison: step'):
            self.validate(comparison() * 2)

    def test_extra_shared_playback_comparisons_receive_validation(self):
        body = comparison() + comparison('other', after=f'`{HEAD}`')
        self.assertIn('other: After needs', self.validate(body)[0])


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        cache = ROOT / '.cache'
        cache.mkdir(exist_ok=True)
        self.directory = TemporaryDirectory(prefix='pr-media-test-', dir=cache)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repository = Repository(self.root)
        self.repository.git('init', '--quiet')
        self.repository.git('config', 'core.fsmonitor', 'false')
        self.entry = {
            'id': 'step', 'file': 'animations/style/step.glb',
            'sourceFile': 'animations/style/sources/step.blend',
            'performers': ['man'], 'duration': 4,
        }
        self.catalog = {'animations': [self.entry, dict(self.entry, id='woman_step', performers=['woman'])]}
        self.inventory = [{'id': 'step', 'file': self.entry['sourceFile'], 'runtimeExport': self.entry['file']}]
        self.write(self.entry['sourceFile'], 'source before')
        self.write(self.entry['file'], 'export before')
        self.save_documents()
        self.base = self.commit()

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')

    def save_documents(self):
        self.write('catalog.json', json.dumps(self.catalog))
        self.write('source-inventory.json', json.dumps(self.inventory))

    def commit(self):
        self.repository.git('add', '.')
        self.repository.git('-c', 'user.name=Codex', '-c', 'user.email=noreply@openai.com',
                            '-c', 'commit.gpgsign=false', 'commit', '--quiet', '-m',
                            'Create test fixture\n\nCo-authored-by: Codex <noreply@openai.com>')
        return self.repository.retrieve_revision('HEAD')

    def retrieve_changes(self):
        return self.repository.retrieve_changes(self.base, self.commit())

    def test_changed_source_covers_each_runtime_variant(self):
        self.write(self.entry['sourceFile'], 'source after')
        self.assertEqual(self.retrieve_changes(), [Change('step', True, True), Change('woman_step', True, True)])

    def test_changed_export_covers_each_runtime_variant(self):
        self.write(self.entry['file'], 'export after')
        self.assertEqual(len(self.retrieve_changes()), 2)

    def test_playback_catalog_edit_identifies_its_variant(self):
        self.entry['loop'] = False
        self.save_documents()
        self.assertEqual(self.retrieve_changes(), [Change('step', True, True)])

    def test_editorial_catalog_edit_has_empty_animation_scope(self):
        self.entry['label'] = 'Reviewed step'
        self.entry['status'] = 'Reviewed'
        self.save_documents()
        self.assertEqual(self.retrieve_changes(), [])

    def test_catalog_addition_and_removal_identify_existing_sides(self):
        self.catalog['animations'][1]['id'] = 'new_step'
        self.save_documents()
        self.assertEqual(self.retrieve_changes(), [Change('new_step', False, True), Change('woman_step', True, False)])

    def test_source_only_inventory_and_early_saved_assets_receive_coverage(self):
        self.write('animations/style/sources/early.blend', 'source')
        self.write('animations/style/sources/inventory.blend', 'source')
        self.inventory.append({'id': 'inventory_step', 'file': 'animations/style/sources/inventory.blend'})
        self.save_documents()
        self.assertEqual(self.retrieve_changes(), [
            Change('animations/style/sources/early.blend', False, True),
            Change('inventory_step', False, True),
        ])

    def test_shared_scene_edit_requires_all_clips(self):
        self.write('animations/shared_scene_data.blend', 'shared revision')
        self.assertEqual(len(self.retrieve_changes()), 2)

    def test_renamed_asset_keeps_existing_animation_comparison(self):
        old_path = self.entry['sourceFile']
        new_path = 'animations/style/sources/renamed.blend'
        (self.root / old_path).rename(self.root / new_path)
        for entry in self.catalog['animations']:
            entry['sourceFile'] = new_path
        self.inventory[0]['file'] = new_path
        self.save_documents()
        self.assertEqual(self.retrieve_changes(), [Change('step', True, True), Change('woman_step', True, True)])

    def test_event_command_checks_description_against_branch_merge_base(self):
        self.write(self.entry['file'], 'export after')
        head = self.commit()
        body = comparison() + comparison('woman_step')
        body = body.replace(BASE, self.base).replace(HEAD, head)
        # A base-only documentation commit advances the target branch after divergence.
        self.repository.git('checkout', '--quiet', '--detach', self.base)
        self.write('README.md', 'Base branch documentation')
        base_tip = self.commit()
        event = self.root / 'event.json'
        event.write_text(json.dumps({'pull_request': {'base': {'sha': base_tip},
                         'head': {'sha': head}, 'body': body}}), encoding='utf-8')
        result = subprocess.run([sys.executable, str(SCRIPT), '--event', str(event)],
                                cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f'Before: {self.base}', result.stdout)
        self.assertIn('Changed animations: 2', result.stdout)
        event.write_text(json.dumps({'pull_request': {'base': {'sha': base_tip},
                         'head': {'sha': head}, 'body': ''}}), encoding='utf-8')
        missing = subprocess.run([sys.executable, str(SCRIPT), '--event', str(event)],
                                 cwd=self.root, text=True, capture_output=True)
        self.assertEqual(missing.returncode, 1)
        self.assertIn('woman_step: add a comparison', missing.stdout)


if __name__ == '__main__':
    unittest.main()
