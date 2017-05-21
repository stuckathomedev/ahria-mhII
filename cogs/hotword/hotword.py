import snowboydecoder
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)

    print("Done.")

    detector = snowboydecoder.HotwordDetector()

    assistant = None

    def callback():
        detector.terminate()
        r.listen(source)
        try:
            print(r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        detector.start(detected_callback=callback, sleep_time=0.03)

    detector.start(detected_callback=callback, sleep_time=0.03)
    # blocks?
    detector.terminate()