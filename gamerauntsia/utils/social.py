from django.conf import settings
from gamerauntsia.gamer.models import GamerUser
import tweepy
import facebook
import urllib 
import urlparse
import logging

def post_to_twitter(item):
    textua = item.getTwitText()
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)  
    api.update_status(textua)
    return True

def _get_fb_graph():
    FACEBOOK_ID = getattr(settings, 'FACEBOOK_USER_ID', None)
    try:
        user = GamerUser.objects.get(facebook_id=FACEBOOK_ID)
    except:
        logging.error('Ez dago FB erabiltzailerik')
        return 0
        
    fb_backend = user.social_auth.filter(provider=u'facebook')
    if fb_backend.exists():
        fb_backend = fb_backend[0]
    else:
        logging.error('ez daukagu login informaziorik')
        return 0
    access_token = fb_backend.tokens.get('access_token',None)
    if access_token == None:
        logging.error('Ez dago access tokenik')
        return 0
    graph = facebook.GraphAPI(access_token)
    return graph

def send_to_fb_wall(item, attachment):
    graph = _get_fb_graph()
    if not graph:
        return 0
    try:
        graph.put_wall_post('',attachment=attachment)
    except Exception, e:
        logging.error('Errorea FBra bidaltzean: %(error)s' % {'error': e})
    return 1

def send_to_fb_page(item, attachment):
    graph = _get_fb_graph()
    #Parametro hauek lortzeko joan:
    #graph.facebook.com/ORRIAREN_IZENA (orri sorreran jarritako URL-a)
    PAGE_ID = getattr(settings, 'FACEBOOK_PAGE_ID', None)
    FB_PAGE = getattr(settings, 'FACEBOOK_PAGE_NAME', None)
    if not (graph and PAGE_ID and FB_PAGE):
        logging.error('Ezin lortu orrian idazteko osagaiak')
        logging.error(PAGE_ID+ ' '+FB_PAGE)
        return 0
    page_access_token = graph.get_object(PAGE_ID, fields='access_token').get('access_token')
    if not page_access_token:
        logging.error('Errorea FBko orriaren access tokena lortzean')
        return 0
    try:
        page_graph = facebook.GraphAPI(page_access_token)
        page_graph.put_object(PAGE_ID, FB_PAGE,'',**attachment)
    except Exception, e:
        logging.error('Errorea FBra bidaltzean: %(error)s' % {'error': e})
    return 1
    

def send_to_fb(item):
    send_to_page = getattr(settings, 'FACEBOOK_PAGE_ID', None)
    """
    attacment = 
    {"name": "Link name"
    "link": "http://www.example.com/",
    "caption": "{*actor*} posted a new review",
    "description": "This is a longer description of the attachment",
    "picture": "http://www.example.com/thumbnail.jpg"}
    """

    attachment = {'name': item.izenburua.encode('utf8'),
                  'link': item.get_absolute_url(),
                  }
    if item.argazkia:
        attachment['picture'] = item.argazkia.get_blog_url()
    else:
        attachment['picture'] = ''

    if not(send_to_page):
        send_to_fb_wall(item, attachment)
    else:
        send_to_fb_page(item, attachment)


def post_social(sender,instance,**kwargs):
    logging.basicConfig(filename='debug.log',level=logging.ERROR)
    if instance.publikoa_da:# and kwargs['created']:
        #post_to_twitter(instance)
        send_to_fb(instance)
    return True