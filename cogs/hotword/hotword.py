import snowboydecoder
import speech_recognition as sr


def listen_forever(text_callback):
    listening = False
    r = sr.Recognizer()
    print("Done.")

    def interrupt():
        return listening

    detector = snowboydecoder.HotwordDetector(
        "resources/Ahria.pmdl", interrupt_check=interrupt, sensitivity=0.75)

    assistant = None

    def callback():
        global listening
        print("Heard ahria")
        listening = True
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text_callback(r.recognize_sphinx(audio))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
        listening = False

    detector.start(detected_callback=callback, sleep_time=0.03)
    # blocks?
    detector.terminate()