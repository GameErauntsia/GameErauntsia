from django.shortcuts import render
from django.db.models import Q
from models import Terminoa


def index(request):
    items = Terminoa.objects.all().order_by('term_eu')
    return render(request, 'base/terminologia.html', locals())


def search_term(request):
    q = request.GET.get('term', '')
    items = Terminoa.objects.filter(Q(term_eu__icontains=q) | Q(term_es__icontains=q) | Q(term_en__icontains=q) | Q(jokoa__izena__icontains=q))[:20]
    return render(request, 'base/terminologia.html', locals())
