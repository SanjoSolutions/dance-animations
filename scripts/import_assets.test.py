"""Playback variants retain source motion and provenance."""
import unittest
import math
import json
from pathlib import Path

from import_assets import retrieve_playback_variants


class PlaybackVariantsTest(unittest.TestCase):
    def test_reviewed_directed_clips_regenerate_one_shot_metadata(self):
        root = Path(__file__).resolve().parents[1]
        evidence = json.loads((root / 'docs/animation_work_status/priority_recovery/evidence.json').read_text())
        directed = {clip['id'] for clip in evidence['clips'] if clip['loop'] is False}
        self.assertEqual(len(directed), 24)
        catalog = json.loads((root / 'catalog.json').read_text())
        for entry in catalog['animations']:
            with self.subTest(clip=entry['id']):
                if entry['id'] in directed:
                    self.assertIs(entry['loop'], False)
                    for status in ('Provisional export', 'Saved-source draft preview', 'Native deformation bake'):
                        for previous_loop in (None, True, False):
                            incoming = dict(entry, status=status)
                            incoming.pop('loop')
                            if previous_loop is not None:
                                incoming['loop'] = previous_loop
                            original = dict(incoming)
                            expected = dict(incoming, loop=False)
                            self.assertEqual(retrieve_playback_variants(incoming), [expected])
                            self.assertEqual(incoming, original)
                            self.assertEqual(retrieve_playback_variants(expected), [expected])
                else:
                    # Existing loops, House transitions, solo choices, and provenance persist.
                    self.assertEqual(retrieve_playback_variants(entry), [entry])

    def test_shared_origin_solos_have_independent_choices(self):
        for style, duration in [('jazz', 2.25), ('gogo', 4.0), ('cutting_shapes', 2.0), ('solo_disco_dance', 16.0)]:
            with self.subTest(style=style):
                entry = dict(id=f'{style}_step_touch', style=style, label=f'{style.capitalize()} step touch',
                             performers=['man', 'woman'], duration=duration,
                             file=f'animations/{style}/{style}_step_touch.glb',
                             sourceFile=f'animations/{style}/sources/{style}_step_touch.blend',
                             sourceSha256='source hash', originalExportSha256='export hash',
                             animationName=f'{style}_step_touch.review', status='Saved-source draft preview')
                variants = retrieve_playback_variants(entry)
                self.assertEqual([variant['id'] for variant in variants],
                                 [f'{style}_step_touch', f'{style}_step_touch_woman'])
                self.assertEqual([variant['performers'] for variant in variants], [['man'], ['woman']])
                for variant, actor in zip(variants, entry['performers']):
                    expected = dict(entry, moveId=entry['id'], id=entry['id'] if actor == 'man' else f'{entry["id"]}_{actor}',
                                    label=f'{entry["label"]} · {actor.capitalize()}', performers=[actor])
                    if style == 'jazz':
                        expected['previewRotation'] = -math.pi / 2 if actor == 'man' else math.pi / 2
                    self.assertEqual(variant, expected)
                    self.assertEqual(retrieve_playback_variants(variant), [variant])
                self.assertEqual(entry['performers'], ['man', 'woman'])

    def test_partner_choreography_retains_both_performers(self):
        entry = dict(id='merengue_basic_in_place', style='merengue', performers=['man', 'woman'])
        self.assertEqual(retrieve_playback_variants(entry), [entry])

    def test_quaternion_kick_retains_its_forward_heading(self):
        entry = dict(id='jazz_kick_front_left', style='jazz', label='Jazz kick front left',
                     performers=['man', 'woman'],
                     sourceFile='animations/jazz/sources/jazz_kick_front_left.blend',
                     status='Saved-source draft preview')
        for variant in retrieve_playback_variants(entry):
            self.assertEqual(variant.get('previewRotation', 0), 0)

    def test_native_bakes_use_their_authored_heading(self):
        entry = dict(id='jazz_step_touch', style='jazz', label='Jazz step touch',
                     performers=['man', 'woman'], sourceFile=None,
                     status='Native deformation bake')
        for variant in retrieve_playback_variants(entry):
            self.assertEqual(variant.get('previewRotation', 0), 0)


if __name__ == '__main__':
    unittest.main()
