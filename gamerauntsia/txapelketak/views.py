from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import *
from django.core.urlresolvers import reverse

def index(request):
    items = Txapelketa.objects.filter(publikoa_da=True)
    return render_to_response('txapelketak/index.html', locals(),context_instance=RequestContext(request))

def txapelketa(request,slug):
    item = get_object_or_404(Txapelketa,slug=slug)
    
    if item.mota == '0': 
        kanporaketadatuak = "[[[{'name':'Urtzi','seed':1,'id':'urtzai'},{'name':'Jon','seed':2,'id':'jonny'}]],[[{'name':'Urtzi','seed':1,'id':'urtzai'}]]];"
    else:
        list_sailkapena = item.get_partaideak('points')

    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))

@login_required
def txapelketa_insk(request,slug):
    user = request.user
    item = get_object_or_404(Txapelketa,slug=slug)
    item.jokalariak.add(user)
    item.save()
    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug':slug}))