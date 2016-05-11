from django.core.management.base import BaseCommand
from gamerauntsia.gamer.models import GamerUser
 
def calc_karma(days):
    users = GamerUser.objects.filter(is_active=True)

    for user in users:
        user.karma = user.get_karma(days)
        user.save()

class Command(BaseCommand):
    help = 'Calculate users karma'

    def add_arguments(self, parser):
        parser.add_argument('days', type=int)

    def handle(self, *args, **options):
        calc_karma(days=options.get('days', 30))