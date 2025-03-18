import unittest
from pywhatkit_alt.ascii_art import image_to_ascii

class TestASCIIArt(unittest.TestCase):
    def test_ascii_conversion(self):
        result = image_to_ascii("sample_image.png")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
