import unittest
from pywhatkit_alt.voice import text_to_speech

class TestVoice(unittest.TestCase):
    def test_tts(self):
        result = text_to_speech("Hello, world!")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
