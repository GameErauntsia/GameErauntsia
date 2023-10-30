import tweepy
from django.conf import settings


def get_tweepy_auth():
    consumer_key = getattr(settings, "TWITTER_CONSUMER_KEY", "")
    consumer_secret = getattr(settings, "TWITTER_CONSUMER_SECRET", "")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(control.twitter_access_token, control.twitter_access_token_secret)
    return auth


def get_tweepy_api():
    """ """
    auth = get_tweepy_auth()
    api = tweepy.API(auth)
    return api
