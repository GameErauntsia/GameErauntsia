from gamerauntsia.berriak.models import Berria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from datetime import datetime
from django.shortcuts import get_object_or_404

def index(request):
    h = {}
    zerr_berriak = Berria.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')
    HOST = settings.HOST
    return render_to_response('berriak/index.html', locals(),context_instance=RequestContext(request))
   
def berria(request,slug):
    item = get_object_or_404(Berria,slug=slug)
    facebook_id = settings.FACEBOOK_APP_ID
    return render_to_response('berriak/berria.html', locals(),context_instance=RequestContext(request))