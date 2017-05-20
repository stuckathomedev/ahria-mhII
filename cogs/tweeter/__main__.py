import indicoio
import tweepy


def ask_for_approval(value, good_text, ungood_text, double_plus_ungood_text):
    if value >= 0.8:
        # FIXME: Use a voice-synthesis function
        print(good_text)
        return True
    elif 0.8 > value >= 0.4:
        return True
    elif 0.4 > value >= 0.2:
        print(ungood_text)
        # TODO: Ask for modification
        return False
    elif 0.2 > value > 0:
        print(double_plus_ungood_text)
        return False
    else:
        raise ValueError(
            "Value not in expected range: " + value)


def length_ok(text):
    if len(text) > 140:
        print("Sorry, your tweet is too long: it's "
              f"{len(text)} characters. Can you make it shorter?")
        return False
    else:
        return True


class Tweeter:
    def __init__(self, twitter_keys):
        auth = tweepy.OAuthHandler(
            twitter_keys.consumer_key,
            twitter_keys.consumer_secret)
        auth.set_access_token(twitter_keys.access_key, twitter_keys.access_secret)
        self.api = tweepy.API(auth)

    def tweet(self, text):
        analysis = indicoio.analyze_text(
            text,
            apis=['sentiment_hq', 'political', 'twitter_engagement'])

        if (ask_for_approval(
                    analysis.sentiment_hq,
                    "Woohoo! Let's go.",
                    "That seems a little negative. Want to reword?",
                    "That seems pretty negative. Want to reword it?") and
                ask_for_approval(
                    analysis.twitter_engagement,
                    "I suspect that this one'll be pretty popular.",
                    "I'm not sure if this'll appeal to many people. Want to reword it?",
                    "I think this one will be unpopular. Want to reword it?") and
                length_ok(text)):
            # Tweet it!
            self.api.update_status(text)
