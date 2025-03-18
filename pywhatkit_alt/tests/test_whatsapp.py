import unittest
from pywhatkit_alt.whatsapp import send_whatsapp_message

class TestWhatsApp(unittest.TestCase):
    def test_send_message(self):
        result = send_whatsapp_message("+919876543210", "Test message")
        self.assertTrue(result)  # Assuming function returns True on success

if __name__ == "__main__":
    unittest.main()
