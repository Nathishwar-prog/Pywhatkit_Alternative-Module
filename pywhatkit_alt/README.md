# PywhatKit Alternative (`pywhatkit_alt`)  

PywhatKit-Alternative is a Python package that provides automation and utility tools such as WhatsApp messaging, YouTube automation, text-to-handwriting conversion, screen recording, and more.  

## Features  

- Send WhatsApp messages  
- Search YouTube videos  
- Convert text to handwriting  
- Convert images to ASCII art  
- Play YouTube videos  
- Screen recording  
- Take screenshots  
- Text-to-Speech (TTS)  
- Speech-to-Text (STT)  
- Generate PDFs  

## Installation  

You can install `pywhatkit_alt` directly from PyPI using:  

```bash
pip install pywhatkit_alt
```
## Usage
1. Send WhatsApp Message
````bash
 from pywhatkit_alt.whatsapp import send_whatsapp_message
send_whatsapp_message("+919876543210", "Hello from Python!")
```` 
2. Search YouTube Videos
````bash
from pywhatkit_alt.youtube import search_youtube
print(search_youtube("Python tutorial"))
````
3. Convert Text to Handwriting
````bash
from pywhatkit_alt.handwriting import text_to_handwriting
text_to_handwriting("Hello, world!", "handwriting.png")
````
4. Convert Image to ASCII Art
````bash
from pywhatkit_alt.ascii_art import image_to_ascii
print(image_to_ascii("image.png"))
````
5. Play YouTube Video
````bash
from pywhatkit_alt.utils import play_youtube_video
play_youtube_video("Python tutorial")
````
6. Record Screen
````bash
from pywhatkit_alt.screen import record_screen
record_screen("record.mp4", duration=10)
````
7. Take Screenshot
````bash
from pywhatkit_alt.screen import take_screenshot
take_screenshot("screenshot.png")
````
8. Text-to-Speech (TTS)
````bash
from pywhatkit_alt.voice import text_to_speech
text_to_speech("Hello, world!")
````
9. Speech-to-Text (STT)
````bash
from pywhatkit_alt.voice import speech_to_text
print(speech_to_text())
````
10. Generate PDF
````bash
from pywhatkit_alt.pdf import create_pdf
create_pdf("Hello, this is a test PDF!", "output.pdf")
````

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## Contact
For any queries, reach out at nathishwarc@gmail.com.