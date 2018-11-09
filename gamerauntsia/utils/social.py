from django.conf import settings
import tweepy
import telebot
from facebookpagewriter.utils import post
from django.core.mail import EmailMultiAlternatives
from django.template import defaultfilters as filters
from gamerauntsia.gamer.models import GamerUser
from mastodon import Mastodon

BASE_PATH = getattr(settings, "BASE_PATH", "")

def post_to_email(obj):
    email_list = GamerUser.objects.values_list('email', flat=True).filter(is_active=True, buletin_notification=True)
    subject, text_content, html_content = obj.getEmailText()
    msg = EmailMultiAlternatives(subject, filters.safe(filters.striptags(text_content)), settings.BULETIN_FROM_EMAIL, bcc=email_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return True

def post_to_telegram(item):
    tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
    tb.send_message(settings.PUBLIC_CHAT_ID, item.getTelegramText())
    return True

def post_to_twitter(item):
    textua = item.getTwitText()
    auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(textua)
    return True

def post_to_mastodon(item):
    textua = item.getTwitText()
    api = Mastodon(settings.MASTODON_CLIENT_ID, settings.MASTODON_CLIENT_SECRET, settings.MASTODON_USER_ACCESS_TOKEN, api_base_url="https://mastodon.eus")
    media_dict = api.media_post(BASE_PATH + item.argazkia.image.url)
    api.status_post(textua, media_ids=media_dict, language="eus")
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
    except Exception:
        pass

def post_social(obj):
    #post_to_email(obj)
    post_to_twitter(obj)
    post_to_page(obj)
    post_to_telegram(obj)
    post_to_mastodon(obj)
    return True
