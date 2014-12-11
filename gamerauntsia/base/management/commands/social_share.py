from django.core.management.base import BaseCommand
from django.conf import settings
import datetime
from django.db.models import Q
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.utils.social import post_social
from datetime import timedelta

def social_share(minutuak):
    minutuak=int(minutuak)
    orain = datetime.datetime.now()
    duela_x_ordu=orain - timedelta(minutes=minutuak)
    berriak=Berria.objects.all().filter(Q(pub_date__gte=duela_x_ordu) 
                                                                     & Q(pub_date__lte=orain) & Q(status='1') 
                                                                     & Q(shared=False)).order_by('-pub_date')
    gpak=GamePlaya.objects.all().filter(Q(pub_date__gte=duela_x_ordu) 
                                                                     & Q(pub_date__lte=orain) & Q(publikoa_da=True) 
                                                                     & Q(shared=False)).order_by('-pub_date')

    txak=Txapelketa.objects.all().filter(Q(pub_date__gte=duela_x_ordu) 
                                                                     & Q(pub_date__lte=orain) & Q(publikoa_da=True) 
                                                                     & Q(shared=False)).order_by('-pub_date')
  
    for berria in berriak:
        post_social(berria)
        berria.shared=True
        berria.save()

    for gp in gpak:
        post_social(gp)
        gp.shared=True
        gp.save()

    for tx in txak:
        post_social(tx)
        tx.shared=True
        tx.save()

    return True

class Command(BaseCommand):
   help = 'Social share'
   def handle(self, *args, **options):
       minutuak=args[0]
       social_share(minutuak)  
