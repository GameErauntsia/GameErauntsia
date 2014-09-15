from gamerauntsia.gameplaya.models import GamePlaya, Kategoria, Zailtasuna
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gamer.models import GamerUser
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404

def index(request,kategoria=None,username=None,maila=None,jokoa=None):
    if kategoria:
        kategoria = get_object_or_404(Kategoria,slug=kategoria)
        gameplayak = GamePlaya.objects.filter(publikoa_da=True,kategoria=kategoria).order_by('-pub_date')
    elif maila:
        maila = get_object_or_404(Zailtasuna,slug=maila)
        gameplayak = GamePlaya.objects.filter(publikoa_da=True,zailtasuna=maila).order_by('-pub_date')
    elif jokoa:
        jokoa = get_object_or_404(Jokoa,slug=jokoa)
        gameplayak = GamePlaya.objects.filter(publikoa_da=True,jokoa=jokoa).order_by('-pub_date')
    else:
        gameplayak = GamePlaya.objects.filter(publikoa_da=True).order_by('-pub_date')
    users = GamerUser.objects.filter(is_active=True,is_gamer=True)
    kategoriak = Kategoria.objects.exclude(gameplay__isnull=True).order_by('izena')
    zailtasunak = Zailtasuna.objects.exclude(gameplay__isnull=True).order_by('izena')
    jokoak = Jokoa.objects.exclude(gameplay__isnull=True).order_by('izena')
    return render_to_response('gameplaya/index.html', locals(),context_instance=RequestContext(request))
    
def gameplaya(request,slug):
    gp = get_object_or_404(GamePlaya,slug=slug)
    facebook_id = settings.FACEBOOK_APP_ID
    return render_to_response('gameplaya/gameplay.html', locals(),context_instance=RequestContext(request))
