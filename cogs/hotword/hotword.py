import cogs.hotword.snowboydecoder as snowboydecoder
import cogs.voice.tts as tts
import speech_recognition as sr


def listen_forever(text_callback):
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    detector = snowboydecoder.HotwordDetector(
        "cogs/hotword/resources/Ahria.pmdl", sensitivity=0.5)

    def callback():
        nonlocal detector
        detector.terminate()
        print('"Ahria" spoken.')
        tts.speak("Hi! I'm Ahria.")
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5.0)
            print("Recognizing audio...")
            try:
                text_callback(r.recognize_google(audio))
            except sr.UnknownValueError:
                tts.speak("Sorry, I didn't get that.")
            except sr.RequestError as e:
                print("Ahria error; {0}".format(e))

        detector = snowboydecoder.HotwordDetector(
            "cogs/hotword/resources/Ahria.pmdl", sensitivity=0.75)
        detector.start(detected_callback=callback, sleep_time=0.03)

    detector.start(detected_callback=callback, sleep_time=0.03)
    # blocks?
    detector.terminate()