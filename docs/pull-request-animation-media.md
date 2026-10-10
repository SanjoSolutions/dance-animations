# Animation comparisons in pull requests

Include playable Before and After videos or animated GIFs in the PR description
for every changed animation and performer variant. Prepare comparisons for local
quality review before publication, then verify playback in the rendered PR before
requesting PR review. Codex-authored descriptions start with `Created by Codex.`.

## Prepare the comparison

1. Capture Before from the merge base of the PR's base branch and head commit,
   and After from the head commit. Use each revision's saved source, export, and
   character dependencies. The [Blender workflow](blender.md) and
   [local validation](validation.md) describe composition and review.
2. Use standard MPFB base bodies, matching camera views, framing, and playback
   speed. Include every performer, the full motion, and a complete loop seam or
   directed transition. Add views that expose changed contacts or poses. Identify
   whether the capture shows authored source playback or the runtime export.
3. Keep renders and their source/export/dependency hashes in a task-specific
   review directory. Record the captured revision with each render. Refresh
   affected media after edits; update revision labels after confirming each
   capture still matches the current assets and dependencies.
4. Upload the media through the PR editor and keep the resulting embed in the
   description. GitHub supports [video and GIF attachments](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files).
   Use an uploaded video URL on its own line or the image Markdown supplied for
   an animated GIF. A persistent HTTPS `.gif` URL in image Markdown also works.
5. Play each side from the rendered PR as a reviewer would. Verify motion,
   complete coverage, and reviewer access, then check the per-animation box.
   Static screenshots, local file links, ordinary download links, and expiring
   CI artifacts provide supplemental evidence.

For a new animation, write `Before: Added in this PR` and provide After media.
For a removed animation, provide Before media and write `After: Removed in this PR`.
An existing animation always requires both captures. Renamed animation IDs appear
as removal/addition entries; identify the relationship in their descriptions.

## Description format

Repeat this block for each affected ID, using full commit hashes. Replace the
media placeholders with actual embeds. Keep the Before and After labels on their
own lines, with their media directly below. Each comparison has its own checklist.

```markdown
### Animation: `animation_id`

Before: `FULL_MERGE_BASE_COMMIT`

BEFORE_VIDEO_ATTACHMENT_OR_ANIMATED_GIF_EMBED

After: `FULL_HEAD_COMMIT`

AFTER_VIDEO_ATTACHMENT_OR_ANIMATED_GIF_EMBED

- [x] Playback verified in the rendered PR for every available side.
```

The [PR template](../.github/pull_request_template.md) includes this structure.
For a PR with zero affected animations, replace the example block with a short
statement of its scope.

## Local check and CI coverage

From the project root, list the required IDs and capture revisions:

```powershell
python scripts/pr_animation_media/check.py --base origin/main --head HEAD --list
```

Save the proposed PR description in `.cache/pr-body.md`, then check it:

```powershell
python scripts/pr_animation_media/check.py --base origin/main --head HEAD --body .cache/pr-body.md
python scripts/pr_animation_media/check.test.py
```

Choose the actual PR base branch when it differs from `origin/main`. The check
uses committed revisions. Prepare comparisons after saving and committing the
animation changes; each local commit follows the project's commit policy.

The `Animation before and after media` job runs on PR creation, description edits,
head updates, reopening, and readiness for review. It compares the merge base with
the event's head revision and checks:

- Changed saved Blender sources and GLB exports, including additions, removals,
  source-only inventory entries, and clips awaiting catalog registration.
- Every catalog variant using a changed asset, plus changes to participant,
  duration, loop, heading, binding, source, and transport settings.
- All clips when `animations/shared_scene_data.blend` changes.
- Visible, individually labeled embeds, current capture revisions, and completed
  playback attestations for every detected animation. Hidden comments and fenced
  examples serve as guidance only.

The check reads Git metadata and catalogs. CI validates embed structure and the
author's playback attestation; human review verifies that the attached content
loads, animates, and depicts the correct clip. Review shared character, wardrobe,
studio, and player-code changes for further affected animations and add their IDs
to the description. Additional comparisons receive the same media/revision checks.

After the workflow is published, configure `Animation before and after media`
as a required status check in the repository's branch rules to make its result a
merge prerequisite. This local change adds the workflow; repository rule settings
are a separate publication step.
