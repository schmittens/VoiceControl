import unittest

from src.voice.voice import Voice


class VoiceTests(unittest.TestCase):
    def test_voice_object_initiated_empty(self):
        voice = Voice()
        self.assertIsNone(voice.query)

    def test_set_keyphrase_in_voice_object(self):
        voice = Voice()
        voice.set_keyphrase("Merlin")
        self.assertEqual(voice.keyphrase,"Merlin")