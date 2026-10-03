"""Playback variants retain source motion and provenance."""
import unittest

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
                                          performers=[actor]))
            self.assertEqual(retrieve_playback_variants(variant), [variant])
        self.assertEqual(entry['performers'], ['man', 'woman'])

    def test_partner_choreography_retains_both_performers(self):
        entry = dict(id='merengue_basic_in_place', style='merengue', performers=['man', 'woman'])
        self.assertEqual(retrieve_playback_variants(entry), [entry])


if __name__ == '__main__':
    unittest.main()
