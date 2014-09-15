from django.conf import settings
import tweepy
import facebook
import urllib 
import urlparse

def post_to_twitter(sender,instance,**kwargs):
    if instance.publikoa_da and kwargs['created']:
        textua = instance.getTwitText()
        auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)  
        api.update_status(textua)
    return True

def send_to_fb(item):
    oauth_args = dict(client_id = settings.FACEBOOK_APP_ID,
                  client_secret = settings.FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')

    oauth_response = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)).read()                                  


    attach = {'name': item.izenburua.encode('utf8'),
                  'link': item.get_absolute_url(),
                  }
    if item.argazkia:
        attach['picture'] = item.argazkia.get_blog_url()
    else:
        attach['picture'] = ''
    
    access_token_page = urlparse.parse_qs(str(oauth_response))['access_token'][0]
    graph = facebook.GraphAPI(access_token_page)
    try:
        graph.put_wall_post('', attachment=attach)
    except facebook.GraphAPIError as e:
        print e
