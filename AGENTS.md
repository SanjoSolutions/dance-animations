## Commits

Whenever you create a Git commit, append exactly one commit trailer:

Co-authored-by: Codex <noreply@openai.com>

## GitHub

Identify Codex-authored GitHub communication as written by Codex.
Publish only after the user approves the local quality review.

## Assets

Use the strict size-based LFS policy from sanjo-solutions:
files larger than 100 MiB use Git LFS; smaller files use regular Git.
Run `python scripts/lfs_policy.py sync` after staging and
`python scripts/lfs_policy.py check` before committing.

Keep per-clip provenance and the source's procedural-study status.
Use MPFB base character meshes for previews.

# Principles

Make sure to always follow the principle guidelines.

## Main principles

- Use OOP with composition. Strong tools of OOP are composition, encapsulation and polymorphism.
- Strongly follow the DRY principle. Generalize as similar patterns emerge.
- Strongly follow the SRP principle (single responsibility principle).
- Prefer higher abstractions
- Optimize code for readability for the user. This includes expressive names and straight forward flows. This does not include verbose comments that add redundant info.
- Follow YAGNI principle

## Other principles

- Use US English.
- Use expressive names for identifiers (variable names, function names, class names, property names etc.)
- Highly prefer to write natural language class-inclusively: every sentence states positive class membership — what something IS, what belongs, what to do — using only affirmative content words. This rules out negation particles (no, never, not), privatives (without, lacking, absent), negation morphemes (un-, in-/im-, non-, dis-, a-, -less).
- Prefer class-inclusive expressions: state membership in the intended category directly rather than excluding another category. For example, prefer is_available over not is_busy when availability is the intended condition.
  This preference concerns meaning, not syntax or vocabulary. Negation is appropriate when it expresses the intended condition accurately. For boolean checks, prefer idiomatic not condition over condition == false.
- Avoid early-skip guard chains for ordinary control flow. Prefer structuring conditions so the primary path is inside the `if` branch and fallback behavior is in `else` when that keeps the flow readable.
- Avoid early stop returns after a branch performs work. Prefer placing the remaining ordinary control flow in the `else` branch.
- For getter functions, use the verb "retrieve" instead of "get" (for example, `retrieveThing` instead of `getThing`).
- Don't include the unit (ms etc.) of the value in identifiers (variable names, parameter names, function names, class names, property names etc.). Instead document the unit with GDScript documentation comments (i.e. `## In milliseconds.`, `## Returns a value in milliseconds.`, or `## Parameter value in milliseconds.`). So instead of `durationMs`, rather `duration` with documentation comment with the unit.
- Avoid uncommon abbreviations in identifiers and prose.
- Structure projects modularily (not by type). Files that are closer related to each other should be closer to each other in the file system.
- Clean up temporary files that you have created when you no longer need them.

### Testing

Principles:

- Test fils should be next to the files that they test.
- Test what the system should do. Don't test what the system should not do.
- No test-only behavior.
- Only test things through their public API.

# UI

Use Bootstrap for new projects or when it is already used by the project.
UI should be minimalistic, to the point what functionally is required.
Avoid marketing prose. Assume users are familiar with common web patterns.

- Form buttons should be right aligned.
- First field should be auto focused when the page is one form primarily.


## Dance authoring

- Run extension installation tests with a dedicated temporary Blender profile. Create its config, scripts, and extensions directories before launching Blender, and set BLENDER_USER_RESOURCES, BLENDER_USER_CONFIG, BLENDER_USER_SCRIPTS, and BLENDER_USER_EXTENSIONS to those existing directories.
- Before extension repository changes, extension installation, or saving preferences in a test, verify that bpy.utils.user_resource('CONFIG') resolves to the intended temporary config directory. Record and compare the regular userpref.blend hash around the test to confirm the user's preferences remain intact. Factory startup alone provides factory settings and still permits writes to the regular preferences file.
- Use Blender 5.2 with the native Man.rigify and Woman.rigify IK controls.
- Keep standard MPFB base bodies and the shared deformation rigs.
- Keep each animation source and GLB under animations/<dance-style>/.
- Keep shared_scene_data.blend as the portable rig template for per-animation sources.
- Use Helpers > Animation to select, create, edit, rename, and save animations.
- Animate Blender-origin rigs in their Blender sources. Prefer sparse IK keys at approach, contact, hold, and release poses.
- Fit hands, wrists, fingers, hips, head, and feet naturally. Preserve native wrist constraints and the shared rig rotation modes.
- For partner steps, plan support contacts and performer spacing in world space. Check interpolated hand contacts, body clearance, planted feet, and loop seams.
- Calibrate solo ready stances against evaluated sole geometry and forearm references.
- Preserve constant transform channels in bakes and compare every deform bone after reopening the source.
- Keep explicit action slots, participant metadata, shared NLA names, frame ranges, and loop metadata.
- Identify authored controls, saved source playback, deformation bakes, runtime exports, and visual review as separate validation stages.
- Keep procedural studies and provisional exports clearly labeled. Retain original hashes and historical review records.
- Each export worker uses a distinct result and log file. Verify embedded animation names, duration, and performer targets.
- Record interrupted work with asset inventories, source hashes, validation coverage, known failures, process state, and exact resume commands.
- Run npm run check, npm test, and npm run build for changes affecting assets or playback.
