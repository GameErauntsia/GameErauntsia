from django.core.management.base import BaseCommand
from django.template import defaultfilters as filters
from gamerauntsia.utils.urls import get_urljson
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.auto_gameplay.models import AutoGamePlaya
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.utils.images import loadUrlImage
from photologue.models import Photo
import time
import urllib2
from urlparse import urlparse
from django.core.files import File
 
def get_gameplays():
    gamers = GamerUser.objects.filter(is_gamer=True,ytube_channel__isnull=False)

    for gamer in gamers:
        user = gamer.ytube_channel[gamer.ytube_channel.rfind('/')+1:]
        channel = u'http://gdata.youtube.com/feeds/api/users/'+user+'/uploads?v=2&alt=json'
        print(channel)
        data = get_urljson(channel)

        for video in data['feed']['entry'][:5]:
            if not GamePlaya.objects.filter(bideoa=video['media$group']['yt$videoid']['$t'],erabiltzailea=gamer).exists():
                if not AutoGamePlaya.objects.filter(bideoa=video['media$group']['yt$videoid']['$t'],erabiltzailea=gamer).exists():
                    url = ''
                    for media in video['media$group']['media$thumbnail']:
                        if media['yt$name'] == 'sddefault':
                            url = media['url']
                        elif media['yt$name'] == 'hqdefault':
                            url = media['url']
                        elif media['yt$name'] == 'default':
                            url = media['url']

                    auto = AutoGamePlaya()
                    auto.izenburua = video['title']['$t'][:64]
                    auto.slug = filters.slugify(video['title']['$t'])[:50]
                    auto.desk = video['media$group']['media$description']['$t']
                    auto.iraupena_min = time.strftime('%M', time.gmtime(int(video['media$group']['yt$duration']['seconds'])))
                    auto.iraupena_seg = time.strftime('%S', time.gmtime(int(video['media$group']['yt$duration']['seconds'])))

                    auto.argazkia = loadUrlImage(url)
                    auto.bideoa = video['media$group']['yt$videoid']['$t']
                    auto.erabiltzailea = gamer
                    auto.save()
    return True                

class Command(BaseCommand):
    help = 'Get GPs automaticaly'
    def handle(self, *args, **options):
        get_gameplays()