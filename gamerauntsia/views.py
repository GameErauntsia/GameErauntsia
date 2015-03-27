from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from gamerauntsia.txapelketak.models import Txapelketa
from datetime import datetime

def index(request):
    gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')[:4]
    berriak = Berria.objects.filter(status='1', pub_date__lt=datetime.now()).order_by('-pub_date')[:8]
    if Txapelketa.objects.filter(publikoa_da=True,status__in=('0','1','2')).exists():
        list_tx = Txapelketa.objects.filter(publikoa_da=True,status__in=('0','1','2')).order_by('-pub_date')
        if len(list_tx) > 1:
            txapelketak = list_tx
        else:
            txapelketa = list_tx[0]

    if Txapelketa.objects.filter(publikoa_da=True,pub_date__lt=datetime.now(),live_bideoa__isnull=False,status='2').exists():
        tx = Txapelketa.objects.filter(publikoa_da=True,pub_date__lt=datetime.now(),live_bideoa__isnull=False,status='2')[0]
        match = tx.get_next_match()
        if match and match<datetime.now():
            live_gp = tx
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def bilaketa(request,bilatu):
    h = {}
    try:
        h['q'] = bilatu
    except:
        raise Http404
    return render_to_response('bilaketa.html', h,context_instance=RequestContext(request))
