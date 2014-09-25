from django.conf import settings
import tweepy
from facebookpagewriter.utils import post
import logging

def post_to_twitter(item):
    textua = item.getTwitText()
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)  
    api.update_status(textua)
    return True


def post_to_page(obj, data={}):
    PAGE_ID = getattr(settings, 'FB_PAGE_ID', None)
    
    data['link'] = unicode(obj.get_absolute_url())
    data['name'] = obj.izenburua.encode('utf8')
    data['description'] = obj.desk[:150].encode('utf8')
    if obj.argazkia:
        data['picture'] = unicode(settings.HOST+obj.argazkia.get_blog_url()).encode('utf8')
    else:
        data['picture'] = unicode(getattr(settings,'STATIC_URL')+u'img/fb_no_image.jpg').encode('utf8')
    component = u'feed'.encode('utf8')
    message = u''.encode('utf8')
    try:
        post(PAGE_ID, component, message, **data)
    except Exception, e:
        logging.error('post_to_page, ERROR: %(error)s' % {'error': e})

def post_social(sender,instance,**kwargs):
    logging.basicConfig(filename='debug.log',level=logging.ERROR)
    if instance.publikoa_da and kwargs['created']:
        post_to_twitter(instance)
        post_to_page(instance)
    return True