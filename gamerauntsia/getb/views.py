from gamerauntsia.getb.models import Atala
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import datetime

def index(request):
    atalak = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')
    return render_to_response('getb/index.html', locals(),context_instance=RequestContext(request))

def atala(request,slug):
    atala = get_object_or_404(Atala,slug=slug)
    facebook_id = settings.FACEBOOK_APP_ID
    return render_to_response('getb/atala.html', locals(),context_instance=RequestContext(request))
