from gamerauntsia.gameplaya.models import GamePlaya, Kategoria, Zailtasuna
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone


def index(request, kategoria=None, username=None, maila=None, jokoa=None, plataforma=None):
    if kategoria:
        kategoria = get_object_or_404(Kategoria, slug=kategoria)
        gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, kategoria=kategoria, pub_date__lt=timezone.now()).order_by('-pub_date')
    elif maila:
        maila = get_object_or_404(Zailtasuna, slug=maila)
        gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, zailtasuna=maila, pub_date__lt=timezone.now()).order_by('-pub_date')
    elif jokoa:
        jokoa = get_object_or_404(Jokoa, slug=jokoa)
        gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, jokoa=jokoa, pub_date__lt=timezone.now()).order_by('-pub_date')
    elif plataforma:
        plataforma = get_object_or_404(Plataforma, slug=plataforma)
        gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, plataforma=plataforma, pub_date__lt=timezone.now()).order_by('-pub_date')
    else:
        gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, pub_date__lt=timezone.now()).order_by('-pub_date')
    kategoriak = Kategoria.objects.exclude(gameplay__isnull=True).order_by('izena')
    zailtasunak = Zailtasuna.objects.exclude(gameplay__isnull=True).order_by('izena')
    jokoak = Jokoa.objects.exclude(gameplay__isnull=True).order_by('izena')
    plataformak = Plataforma.objects.exclude(gameplay__isnull=True).order_by('izena')
    return render(request, 'gameplaya/index.html', locals())


def gameplaya(request, slug, related=None):
    gp = get_object_or_404(GamePlaya, slug=slug)
    related_gps = GamePlaya.objects.filter(status='1', publikoa_da=True, jokoa=gp.jokoa, pub_date__lt=gp.pub_date).exclude(id=gp.id).order_by('-pub_date')[:5]
    facebook_id = settings.FB_APP_ID
    return render(request, 'gameplaya/gameplay.html', locals())
