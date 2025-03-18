import unittest
from pywhatkit_alt.youtube import search_youtube

class TestYouTube(unittest.TestCase):
    def test_search_video(self):
        result = search_youtube("Python tutorial")
        self.assertIsInstance(result, list)  # Should return a list of results

if __name__ == "__main__":
    unittest.main()
