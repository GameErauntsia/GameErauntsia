from gamerauntsia.berriak.models import Berria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def index(request):
    h = {}
    berria_list = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')
    paginator = Paginator(berria_list, 10)
    page = request.GET.get('orria')
    try:
        berriak = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        berriak = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        berriak = paginator.page(paginator.num_pages)
    h['zerr_berriak'] = berriak
    h['HOST'] = settings.HOST
    return render_to_response('berriak/index.html', h,context_instance=RequestContext(request))
   
def berria(request,slug):
    h = {}
    h['item'] = Berria.objects.filter(slug=slug)[0]
    return render_to_response('berriak/berria.html', h,context_instance=RequestContext(request))