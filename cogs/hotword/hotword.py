import snowboydecoder
import speech_recognition as sr


def listen_forever(text_callback):
    r = sr.Recognizer()
    detector = snowboydecoder.HotwordDetector(
        "resources/Ahria.pmdl", sensitivity=0.75)

    def callback():
        nonlocal detector
        detector.terminate()
        print("Heard ahria")
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5.0)
            try:
                text_callback(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

        detector = snowboydecoder.HotwordDetector(
            "resources/Ahria.pmdl", sensitivity=0.75)
        detector.start(detected_callback=callback, sleep_time=0.03)

    detector.start(detected_callback=callback, sleep_time=0.03)
    # blocks?
    detector.terminate()