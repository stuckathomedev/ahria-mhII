import pyttsx


def speak(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()
