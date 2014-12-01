from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from datetime import datetime

def index(request):
    gameplayak = GamePlaya.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')[:4]
    berriak = Berria.objects.filter(status='1', pub_date__lt=datetime.now()).order_by('-pub_date')[:8]
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def bilaketa(request,bilatu):
    h = {}
    try:
        h['q'] = bilatu
    except:
        raise Http404 
    return render_to_response('bilaketa.html', h,context_instance=RequestContext(request))
