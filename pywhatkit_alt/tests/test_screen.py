import unittest
import os
from pywhatkit_alt.screen import take_screenshot

class TestScreen(unittest.TestCase):
    def test_screenshot(self):
        take_screenshot("test_screenshot.png")
        self.assertTrue(os.path.exists("test_screenshot.png"))
        os.remove("test_screenshot.png")

if __name__ == "__main__":
    unittest.main()
