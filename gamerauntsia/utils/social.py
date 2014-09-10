from django.conf import settings
import tweepy

def post_to_twitter(item):
    if item.publikoa_da:
        textua = item.getTwitText()
        auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)  
        api.update_status(textua)
    return True