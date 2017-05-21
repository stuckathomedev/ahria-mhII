import argparse
import os
import json

import snowboydecoder
import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

detector = snowboydecoder.HotwordDetector()

assistant = None

def callback():
    detector.terminate()
    assistant.start_conversation()
    detector.start(detected_callback=callback, sleep_time=0.03)

parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
            **json.load(f))
        global assistant
        assistant = Assistant(credentials)
        assistant.start()
        detector.start(detected_callback=callback, sleep_time=0.03)
        # blocks?
        detector.terminate()