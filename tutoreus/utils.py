import os
import twitter
import urllib, urllib2
from django.conf import settings
from django.contrib.sites.models import Site

TWITTER_MAXLENGTH = getattr(settings, 'TWITTER_MAXLENGTH', 140)

def post_to_twitter(sender, instance, *args, **kwargs):

    # avoid to post the same object twice
    if not kwargs.get('created'):
        return False

    # check if there's a twitter account configured
    try:
        consumer_key = settings.TWITTER_CONSUMER_KEY
        consumer_secret = settings.TWITTER_CONSUMER_SECRET
        access_token_key = settings.TWITTER_ACCESS_TOKEN_KEY
        access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
    except AttributeError:
        print 'WARNING: Twitter account not configured.'
        return False

    # if the absolute url wasn't a real absolute url and doesn't contains the
    # protocol and domain defineds, then append this relative url to the domain
    # of the current site, emulating the browser's behaviour
    url = instance.get_absolute_url()
    if not url.startswith('http://') and not url.startswith('https://'):
        domain = Site.objects.get_current().domain
        url = u'http://%s%s' % (domain, url)

    # tinyurl'ze the object's link
    create_api = 'http://tinyurl.com/api-create.php'
    data = urllib.urlencode(dict(url=url))
    link = urllib2.urlopen(create_api, data=data).read().strip()

    # create the twitter message
    try:
        text = instance.get_twitter_message()
    except AttributeError:
        text = unicode(instance)

    mesg = u'%s - %s' % (text, link)
    if len(mesg) > TWITTER_MAXLENGTH:
        size = len(mesg + '...') - TWITTER_MAXLENGTH
        mesg = u'%s... - %s' % (text[:-size], link)

    try:
        twitter_api = twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token_key, access_token_secret=access_token_secret)
        twitter_api.PostUpdate(mesg)
    except urllib2.HTTPError, ex:
        print 'ERROR:', str(ex)
        return False