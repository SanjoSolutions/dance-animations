"""Playback variants retain source motion and provenance."""
import unittest

from import_assets import retrieve_playback_variants


class PlaybackVariantsTest(unittest.TestCase):
    def test_gogo_shared_origin_solos_have_independent_choices(self):
        entry = dict(id='gogo_step_touch', style='gogo', label='Gogo step touch',
                     performers=['man', 'woman'], duration=4.0,
                     file='animations/gogo/gogo_step_touch.glb',
                     sourceFile='animations/gogo/sources/gogo_step_touch.blend',
                     sourceSha256='source hash', originalExportSha256='export hash',
                     animationName='gogo_step_touch.review', status='Saved-source draft preview')
        variants = retrieve_playback_variants(entry)
        self.assertEqual([variant['id'] for variant in variants],
                         ['gogo_step_touch', 'gogo_step_touch_woman'])
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
