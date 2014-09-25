from django.core.management.base import BaseCommand
from gamerauntsia.utils.urls import get_urljson
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.auto_gameplay.models import AutoGamePlaya
 
def get_gameplays():
    gamers = GamerUser.objects.filter(is_gamer=True,ytube_channel__isnull=False)

    for gamer in gamers:
        user = gamer.ytube_channel.replace('http://www.youtube.com/user/','').replace('https://www.youtube.com/channel/','')
        channel = u'http://gdata.youtube.com/feeds/api/users/'+user+'/uploads?v=2&alt=json'
        data = get_urljson(channel)

        for video in data['entry']:
            print video['title']['$t']

        break

class Command(BaseCommand):
    help = 'Get GPs automaticaly'
    def handle(self, *args, **options):
        get_gameplays()