import snowboydecoder

detector = snowboydecoder.HotwordDetector()

assistant = None

def callback():
    detector.terminate()
    assistant.start_conversation()
    detector.start(detected_callback=callback, sleep_time=0.03)

detector.start(detected_callback=callback, sleep_time=0.03)
# blocks?
detector.terminate()