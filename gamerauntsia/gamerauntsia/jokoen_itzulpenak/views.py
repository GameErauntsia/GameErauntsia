from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from models import Itzulpena

def index(request):
    items = Itzulpena.objects.filter(publikoa_da=True).order_by('-mod_date')
    return render_to_response('jokoen_itzulpenak/index.html', locals(),context_instance=RequestContext(request))


def search_retro(request):
    q = request.GET.get('term', '')
    items = Itzulpena.objects.filter(Q(publikoa_da=True),Q(izena__icontains=q)|Q(jokoa__izena__icontains=q)|Q(plataforma__izena__icontains=q)|Q(status=q))[:20]
    return render_to_response('jokoen_itzulpenak/index.html', locals(),context_instance=RequestContext(request))
