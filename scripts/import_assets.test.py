"""Playback variants retain source motion and provenance."""
import unittest
import math

from import_assets import retrieve_playback_variants


class PlaybackVariantsTest(unittest.TestCase):
    def test_jazz_shared_origin_solos_have_independent_choices(self):
        entry = dict(id='jazz_step_touch', style='jazz', label='Jazz step touch',
                     performers=['man', 'woman'], duration=2.25,
                     file='animations/jazz/jazz_step_touch.glb',
                     sourceFile='animations/jazz/sources/jazz_step_touch.blend',
                     sourceSha256='source hash', originalExportSha256='export hash',
                     animationName='jazz_step_touch.review', status='Saved-source draft preview')
        variants = retrieve_playback_variants(entry)
        self.assertEqual([variant['id'] for variant in variants],
                         ['jazz_step_touch', 'jazz_step_touch_woman'])
        self.assertEqual([variant['performers'] for variant in variants], [['man'], ['woman']])
        for variant, actor in zip(variants, entry['performers']):
            self.assertEqual(variant, dict(entry, id=entry['id'] if actor == 'man' else f'{entry["id"]}_{actor}',
                                          label=f'{entry["label"]} · {actor.capitalize()}',
                                          performers=[actor],
                                          previewRotation=-math.pi / 2 if actor == 'man' else math.pi / 2))
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
