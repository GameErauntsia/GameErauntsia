from django.shortcuts import render_to_response
from django.template import RequestContext

from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa

def index(request):
    topjokoak = GamerUser.objects.values('top_jokoak__izena').annotate(Count('top_jokoak')).order_by('-top_jokoak__count','-top_jokoak__izena')[:10]
    jokoak = Jokoa.objetcts.all()
    return render_to_response('jokoa/index.html', h,context_instance=RequestContext(request))
   