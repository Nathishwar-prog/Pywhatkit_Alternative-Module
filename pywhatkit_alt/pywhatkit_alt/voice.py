import pyttsx3
import speech_recognition as sr


def text_to_speech(text, voice_id=0):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()



def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, couldn't understand"
    except sr.RequestError:
        return "Speech recognition service error"
