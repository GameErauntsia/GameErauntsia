from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.db.models import Count
from datetime import datetime
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.base.models import Terminoa
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.berriak.models import Berria
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.utils.urls import get_urljson

def index(request):
    topjokoak = GamerUser.objects.values('top_jokoak__izena').annotate(Count('top_jokoak')).order_by('-top_jokoak__count','-top_jokoak__izena')[:10]
    jokoak = Jokoa.objects.filter(publikoa_da=True).order_by("izena","bertsioa")
    return render_to_response('jokoa/index.html', locals(),context_instance=RequestContext(request))

def jokoa(request,slug):
    jokoa = get_object_or_404(Jokoa, publikoa_da=True,slug=slug)
    try:
    	if jokoa.steam_id:
    	    steam_json = get_urljson("http://store.steampowered.com/api/appdetails?appids="+str(jokoa.steam_id))[str(jokoa.steam_id)]['data']
    except:
    	pass
    users = GamerUser.objects.filter(top_jokoak=jokoa,is_staff=False).order_by("-karma")[:6]
    gameplayak = GamePlaya.objects.filter(jokoa=jokoa, publikoa_da=True, status='1')[:2]
    terminoak = Terminoa.objects.filter(jokoa=jokoa).order_by("?")[:10]
    berriak = Berria.objects.filter(jokoa=jokoa,status='1', pub_date__lt=datetime.now()).order_by('-pub_date')[:3]
    txapelketak = Txapelketa.objects.filter(jokoa=jokoa,publikoa_da=True).order_by('-pub_date')[:3]
    return render_to_response('jokoa/jokoa.html', locals(),context_instance=RequestContext(request))
