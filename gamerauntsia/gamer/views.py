from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Count

def index(request):
    users = GamerUser.objects.filter(is_active=True)
    return render_to_response('gamer/index.html', locals(),context_instance=RequestContext(request))
    
def profile(request,username):
    user = get_object_or_404(GamerUser,username=username)
    gameplayak = GamePlaya.objects.filter(publikoa_da=True,erabiltzailea=user).order_by('-pub_date')
    gp_count = len(gameplayak)
    gameplayak = gameplayak[:5]
    categs = GamePlaya.objects.filter(publikoa_da=True,erabiltzailea=user).values('kategoria__izena',).annotate(count=Count('id'))
    berriak = Berria.objects.filter(publikoa_da=True,erabiltzailea=user).order_by('-pub_date')
    bcategs = Berria.objects.filter(publikoa_da=True,erabiltzailea=user).values('gaia__izena',).annotate(count=Count('id'))
    berri_count = len(berriak)
    berriak = berriak[:5]
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))
