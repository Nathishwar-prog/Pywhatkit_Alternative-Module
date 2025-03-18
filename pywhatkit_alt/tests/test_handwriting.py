import unittest
import os
from pywhatkit_alt.handwriting import text_to_handwriting

class TestHandwriting(unittest.TestCase):
    def test_handwriting_image(self):
        text_to_handwriting("Hello, world!", "test_handwriting.png")
        self.assertTrue(os.path.exists("test_handwriting.png"))
        os.remove("test_handwriting.png")

if __name__ == "__main__":
    unittest.main()
