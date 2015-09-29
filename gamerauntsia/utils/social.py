from django.conf import settings
import tweepy
from facebookpagewriter.utils import post
from django.core.mail import EmailMultiAlternatives
from django.template import defaultfilters as filters
import logging
from gamerauntsia.gamer.models import GamerUser

def post_to_email(obj):
    email_list = GamerUser.objects.values_list('email', flat=True).filter(is_active=True, buletin_notification=True)
    subject, text_content, html_content = obj.getEmailText()
    msg = EmailMultiAlternatives(subject, filters.safe(filters.striptags(text_content)), settings.BULETIN_FROM_EMAIL, bcc=email_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return True

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

    name, desk, pic = obj.getFBinfo()

    data['name'] = name.encode('utf8')
    data['description'] = filters.safe(filters.striptags(desk))[:150].encode('utf8')
    if pic:
        data['picture'] = unicode(settings.HOST+pic.get_blog_url()).encode('utf8')
    else:
        data['picture'] = unicode(getattr(settings,'STATIC_URL')+u'img/fb_no_image.jpg').encode('utf8')
    component = u'feed'.encode('utf8')
    message = u''.encode('utf8')
    try:
        post(PAGE_ID, component, message, **data)
    except Exception, e:
        logging.error('post_to_page, ERROR: %(error)s' % {'error': e})

def post_social(obj):
    logging.basicConfig(filename='debug.log',level=logging.ERROR)
    post_to_email(obj)
    post_to_twitter(obj)
    post_to_page(obj)
    return True
