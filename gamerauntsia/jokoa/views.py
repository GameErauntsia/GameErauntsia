from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa

def index(request):
    topjokoak = GamerUser.objects.values('top_jokoak__izena').annotate(Count('top_jokoak')).order_by('-top_jokoak__count','-top_jokoak__izena')[:10]
    jokoak = Jokoa.objects.filter(publikoa_da=True).order_by("izena","bertsioa")
    return render_to_response('jokoa/index.html', locals(),context_instance=RequestContext(request))
   