import base64
import json
import webbrowser

import tweepy


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


def main():
    twitter_keys = authorize_twitter()
    with open('data.json', 'w') as file:
        file.write(json.dumps({'twitter': twitter_keys}))
        print("Saved initial data to data.json.")

if __name__ == '__main__':
    main()