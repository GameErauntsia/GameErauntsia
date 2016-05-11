from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from models import Retro_IPS

def index(request):
    items = Retro_IPS.objects.filter(publikoa_da=True).order_by('-mod_date')
    return render_to_response('retro/index.html', locals(),context_instance=RequestContext(request))


def search_retro(request):
    q = request.GET.get('term', '')
    items = Retro_IPS.objects.filter(Q(publikoa_da=True),Q(izena__icontains=q)|Q(jokoa__izena__icontains=q)|Q(plataforma__izena__icontains=q)|Q(status=q))[:20]
    return render_to_response('retro/index.html', locals(),context_instance=RequestContext(request))
