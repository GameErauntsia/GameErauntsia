from django.core.management.base import BaseCommand
from gamerauntsia.gamer.models import GamerUser
 
def calc_karma():
    users = GamerUser.objects.filter(is_active=True)

    for user in users:
        user.karma = user.get_karma()
        user.save()

class Command(BaseCommand):
    help = 'Calculate users karma'
    def handle(self, *args, **options):
        calc_karma()