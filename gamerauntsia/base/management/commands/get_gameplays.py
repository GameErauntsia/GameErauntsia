from django.core.management.base import BaseCommand
from gamerauntsia.utils.urls import get_urljson
from gamerauntsia.gamer.models import GamerUser
 
def get_gameplays():
    gamers = GamerUser.objects.filter(is_gamer=True,ytube_channel__isnull=False)

    for gamer in gamers:
        channel = 'http://gdata.youtube.com/feeds/api/users/'+gamer.username+'/uploads?v=2&alt=json'

class Command(BaseCommand):
    help = 'Get GPs automaticaly'
    def handle(self, *args, **options):
        get_gameplays()