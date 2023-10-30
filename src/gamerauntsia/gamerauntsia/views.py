from django.utils import timezone

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.bazkidetza.models import Eskaintza


def index(request):
    gameplayak = (
        GamePlaya.objects.filter(
            status="1", publikoa_da=True, pub_date__lt=timezone.now()
        )
        .order_by("-pub_date")
        .select_related("argazkia", "jokoa", "plataforma__icon")
    )
    berriak = (
        Berria.objects.filter(status="1", pub_date__lt=timezone.now())
        .order_by("-pub_date")
        .select_related("argazkia")
    )
    gp = gameplayak[0]
    berria = berriak[0]

    if gp.pub_date > berria.pub_date:
        live = gp
        gameplayak = gameplayak[1:4]
        berriak = berriak[:8]
    else:
        live = berria
        gameplayak = gameplayak[:3]
        berriak = berriak[1:9]

    if Txapelketa.objects.filter(publikoa_da=True, status__in=("0", "1", "2")).exists():
        list_tx = Txapelketa.objects.filter(
            publikoa_da=True, status__in=("0", "1", "2")
        ).order_by("-pub_date")
        if len(list_tx) > 1:
            txapelketak = list_tx
        else:
            txapelketa = list_tx[0]

    eskaintzak = Eskaintza.objects.filter(
        Q(is_public=True),
        Q(expire_date__gte=timezone.now()) | Q(expire_date__isnull=True),
    ).order_by("-activate_date")[:4]

    return render(request, "index.html", locals())


def bilaketa(request, bilatu):
    h = {}
    try:
        h["q"] = bilatu
    except:
        raise Http404
    return render(request, "bilaketa.html", h)
