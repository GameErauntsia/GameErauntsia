from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.db.models import Count
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.base.models import Terminoa
from gamerauntsia.jokoa.models import Jokoa

def index(request):
    topjokoak = GamerUser.objects.values('top_jokoak__izena').annotate(Count('top_jokoak')).order_by('-top_jokoak__count','-top_jokoak__izena')[:10]
    jokoak = Jokoa.objects.filter(publikoa_da=True).order_by("izena","bertsioa")
    return render_to_response('jokoa/index.html', locals(),context_instance=RequestContext(request))

def jokoa(request,slug):
    jokoa = get_object_or_404(Jokoa, publikoa_da=True,slug=slug)
    users = GamerUser.objects.filter(top_jokoak=jokoa,is_staff=False).order_by("-karma")[:6]
    gameplayak = GamePlaya.objects.filter(jokoa=jokoa, publikoa_da=True, status='1')[:5]
    terminoak = Terminoa.objects.filter(jokoa=jokoa).order_by("?")[:10]
    return render_to_response('jokoa/jokoa.html', locals(),context_instance=RequestContext(request))
