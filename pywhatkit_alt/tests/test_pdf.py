import unittest
import os
from pywhatkit_alt.pdf import create_pdf

class TestPDF(unittest.TestCase):
    def test_pdf_creation(self):
        create_pdf("Test PDF content", "test_output.pdf")
        self.assertTrue(os.path.exists("test_output.pdf"))
        os.remove("test_output.pdf")

if __name__ == "__main__":
    unittest.main()

