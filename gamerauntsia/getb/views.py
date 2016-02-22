from gamerauntsia.getb.models import Atala
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import datetime

def index(request):
    atal_nab = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')[0]
    atalak = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).exclude(id=atal_nab.id).order_by('-pub_date')
    atalgehiago = atalak[3:7]
    return render_to_response('getb/index.html', locals(),context_instance=RequestContext(request))

def atala(request,slug):
    atala = get_object_or_404(Atala,slug=slug)
    related_atalak = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).exclude(id=atala.id).order_by('-pub_date')[:5]
    facebook_id = settings.FACEBOOK_APP_ID
    return render_to_response('getb/atala.html', locals(),context_instance=RequestContext(request))
