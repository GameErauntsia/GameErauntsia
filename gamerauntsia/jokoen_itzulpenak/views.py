from django.shortcuts import render
from django.db.models import Q
from models import Itzulpena, EuskarazkoJokoa, Euskalinkak


def index(request):
    # items = Itzulpena.objects.filter(publikoa_da=True).order_by('-mod_date')
    items = EuskarazkoJokoa.objects.filter(publikoa_da=True).order_by('jokoa__izena')
    links = Euskalinkak.objects.filter(publikoa_da=True)
    return render(request, 'jokoen_itzulpenak/index.html', locals())


def search_retro(request):
    q = request.GET.get('term', '')
    items = Itzulpena.objects.filter(Q(publikoa_da=True), Q(izena__icontains=q) | Q(jokoa__izena__icontains=q) | Q(plataforma__izena__icontains=q) | Q(status=q))[:20]
    return render(request, 'jokoen_itzulpenak/index.html', locals())
