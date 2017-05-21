import base64
import fcntl
from subprocess import Popen, PIPE
import json
import webbrowser

import tweepy
import os






TWEEPY_CONSUMER_KEY = "RksIJD0x7kb2toj5vJMOmA8IO"
# such not human readable
TWEEPY_CONSUMER_SECRET = base64.b64decode("RmNYZHMxTG94bmJxRlhGbHBKalVIdXJraGFvRzdwbDJIRmxTR0hOcndhYVZRMzIzZTE=").decode("utf-8")


def authorize_twitter():
    auth = tweepy.OAuthHandler(TWEEPY_CONSUMER_KEY, TWEEPY_CONSUMER_SECRET)

    print("Please authorize Project Astley to post tweets. Loading authorization URL...")

    auth_url = auth.get_authorization_url()
    print("Authorization URL:", auth_url)
    print("Opening in web browser.")
    webbrowser.open(auth_url)

    verifier = input("Enter PIN: ")
    auth.get_access_token(verifier)

    # authenticate and retrieve user name
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    username = api.me().name
    print('Ready to post to ' + username)

    return {
        'consumer_key': TWEEPY_CONSUMER_KEY,
        'consumer_secret': TWEEPY_CONSUMER_SECRET,
        'access_key': auth.access_token,
        'access_secret': auth.access_token_secret
    }


def authorize_google_assistant():
    def set_fd_nonblocking(fd):
        """
        Set the file description of the given file descriptor to non-blocking.
        """
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        flags = flags | os.O_NONBLOCK
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)

    p = Popen("google-oauthlib-tool --client-secrets "
              "./cogs/hotword/client_secret_940842120674-3vjlihqggtr5hed4open7aabbakn0msc.apps.googleusercontent.com.json "
              "--scope https://www.googleapis.com/auth/assistant-sdk-prototype "
              "--save --headless", stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1)
    set_fd_nonblocking(p.stdout)
    set_fd_nonblocking(p.stderr)

    p.stdin.write("1\n")
    while True:
        try:
            out1 = p.stdout.read()
        except IOError:
            continue
        else:
            break
    out1 = p.stdout.read()
    p.stdin.write("5\n")
    while True:
        try:
            out2 = p.stdout.read()
        except IOError:
            continue
        else:
            break

def main():
    twitter_keys = authorize_twitter()
    authorize_google_assistant()
    with open('data.json', 'w') as file:
        file.write(json.dumps({'twitter': twitter_keys}))
        print("Saved initial data to data.json.")

if __name__ == '__main__':
    main()