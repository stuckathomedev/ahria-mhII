import pyttsx


def speak(text):
    engine = pyttsx.init()
    engine.setProperty('rate', 110)
    engine.setProperty('voice', 'english+f1') # linux only m9
    engine.say(text)
    engine.runAndWait()
