from django.core.management.base import BaseCommand
from datetime import datetime
from gamerauntsia.bazkidetza.models import Bazkidea


def calc_suscription():
    users = Bazkidea.objects.filter(paid=True, expire_date__lt=datetime.now())

    for user in users:
        user.paid = False
        user.save()


class Command(BaseCommand):
    help = "Calculate users suscription"

    def handle(self, *args, **options):
        calc_suscription()
