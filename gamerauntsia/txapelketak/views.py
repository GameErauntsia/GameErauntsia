from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import *

def index(request):
    items = Txapelketa.objects.all()
    return render_to_response('txapelketak/index.html', locals(),context_instance=RequestContext(request))

def txapelketa(request,slug):
    item = get_object_or_404(Txapelketa,slug=slug)
    list_sailkapena = item.get_partaideak('points')

    kanporaketadatuak = [
        
    ]
    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))
