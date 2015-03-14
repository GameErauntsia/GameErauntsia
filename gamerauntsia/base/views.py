from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.db.models import Q
from models import Terminoa
import json

def index(request):
    items = Terminoa.objects.all().order_by('term_eu')
    return render_to_response('base/terminologia.html', locals(),context_instance=RequestContext(request))


def search_term(request):
    q = request.GET.get('term', '')
    items = Terminoa.objects.filter(Q(term_eu__icontains = q)|Q(term_es__icontains=q)|Q(term_en__icontains=q)|Q(jokoa__izena__icontains=q))[:20]
    return render_to_response('base/terminologia.html', locals(),context_instance=RequestContext(request))
