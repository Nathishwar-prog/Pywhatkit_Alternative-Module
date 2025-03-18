import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def send_whatsapp_message(phone_number: str, message: str):
    """
    Send a WhatsApp message using Selenium WebDriver.

    Args:
        phone_number (str): Receiver's phone number in international format (e.g., "+918888888888").
        message (str): The text message to be sent.
    """
    try:
        # Setup WebDriver with session persistence
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-data-dir=" + os.path.abspath("chrome-session"))  # Saves session
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open WhatsApp Web with pre-filled message
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
        driver.get(url)

        # Wait until QR code disappears (means logged in)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']"))
            )
            print("Scan the QR code to continue...")
            WebDriverWait(driver, 60).until_not(
                EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']"))
            )
            print("Logged in successfully!")
        except:
            print("Already logged in or QR code skipped.")

        # Wait until message box appears
        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
        )
        time.sleep(2)  # Allow text box to be ready

        # Click send button
        send_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']"))
        )
        send_button.click()
        print("Message sent successfully!")

        # Close browser after a delay
        time.sleep(5)
        driver.quit()

    except Exception as e:
        print("Error:", e)


# Example usage
# if __name__ == "__main__":
#     send_whatsapp_message("+91987654321", "Hello! This is an automated message from PyKit Alternative.")
