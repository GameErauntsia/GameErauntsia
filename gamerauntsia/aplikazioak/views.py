from django.shortcuts import render_to_response
from django.template import RequestContext

from tutoreus.aplikazioak.models import Aplikazioa
from tutoreus.berriak.models import Berria

def index(request):
    h = {}
    h['zerr_aplikazioa'] = Aplikazioa.objects.all()[:5]
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('aplikazioak/index.html', h,context_instance=RequestContext(request))
    
def aplikazioa(request,slug):
    h = {}
    h['aplikazioa'] = Aplikazioa.objects.filter(slug=slug)[0]
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('aplikazioak/aplikazioa.html', h,context_instance=RequestContext(request))
