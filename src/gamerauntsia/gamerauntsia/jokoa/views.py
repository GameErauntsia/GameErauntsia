from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q, F, OuterRef, Exists, Count
from django.db.models.functions import Extract
from django.utils import timezone
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.base.models import Terminoa, ProiektuLaguna
from gamerauntsia.jokoa.models import Jokoa, Garatzailea
from gamerauntsia.jokoa.filters import EuskarazkoJokoaFilter, JokoGaratzaileakFilter
from gamerauntsia.jokoen_itzulpenak.models import EuskarazkoJokoa
from gamerauntsia.joko_itzulpenak.models import JokoItzulpena
from gamerauntsia.berriak.models import Berria
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.utils.urls import get_urljson


def index(request):
    topjokoak = (
        GamerUser.objects.values(
            "top_jokoak__izena",
            "top_jokoak__bertsioa",
            "top_jokoak__logoa",
            "top_jokoak__slug",
        )
        .annotate(Count("top_jokoak"))
        .order_by("-top_jokoak__count", "-top_jokoak__izena")[:10]
    )
    jokoak = (
        Jokoa.objects.filter(publikoa_da=True)
        .select_related("logoa")
        .order_by("izena", "bertsioa")
        .select_related("logoa")
    )
    last_jokoak = (
        Jokoa.objects.filter(publikoa_da=True)
        .select_related("logoa")
        .order_by("-id")[:10]
    )
    euskaljokoak = (
        EuskarazkoJokoa.objects.filter(publikoa_da=True)
        .select_related("jokoa__logoa")
        .order_by("-pub_date")[:5]
    )
    try:
        if last_jokoak[0].steam_id:
            steam_json = get_urljson(
                "https://store.steampowered.com/api/appdetails?appids="
                + str(last_jokoak[0].steam_id)
            )[str(last_jokoak[0].steam_id)]["data"]
    except:
        pass
    return render(request, "jokoa/index.html", locals())


def jokoa(request, slug):
    steam_json = None
    user = request.user
    jokoa = get_object_or_404(Jokoa, publikoa_da=True, slug=slug)
    if user.is_authenticated:
        fav_game = user.likes_game(jokoa)
    try:
        if jokoa.steam_id:
            steam_json = get_urljson(
                "https://store.steampowered.com/api/appdetails?appids="
                + str(jokoa.steam_id)
            )[str(jokoa.steam_id)]["data"]
    except:
        pass
    gameplayak = GamePlaya.objects.filter(
        jokoa=jokoa, publikoa_da=True, status="1", pub_date__lt=timezone.now()
    ).order_by("-pub_date")
    if steam_json:
        gameplayak_more = len(gameplayak) > 2
        gameplayak = gameplayak[:2]
    else:
        gameplayak_more = len(gameplayak) > 4
        gameplayak = gameplayak[:4]
    txapelketak = Txapelketa.objects.filter(jokoa=jokoa, publikoa_da=True).order_by(
        "-pub_date"
    )[:3]
    berriak = Berria.objects.filter(
        jokoa=jokoa, status="1", pub_date__lt=timezone.now()
    ).order_by("-pub_date")
    berriak_more = len(berriak) > 3
    berriak = berriak[:3]
    itzulpenak = jokoa.jokoitzulpena_set.all()
    return render(request, "jokoa/jokoa.html", locals())


def garatzaileak(request):
    jokogaratzaileak = (
        Garatzailea.objects.filter().order_by("izena").prefetch_related("logoa")
    )
    filters = JokoGaratzaileakFilter(request.GET, queryset=jokogaratzaileak)
    return render(request, "jokoa/garatzaileak.html", locals())


def garatzailea(request, slug):
    garatzailea = get_object_or_404(Garatzailea, slug=slug)
    berriak = (
        Berria.objects.filter(
            Q(garatzailea=garatzailea) | Q(jokoa__garatzailea=garatzailea)
        )
        .filter(status="1", pub_date__lt=timezone.now())
        .order_by("-pub_date")[:3]
    )
    jokoak = Jokoa.objects.filter(garatzailea=garatzailea).order_by(
        "-argitaratze_data"
    )[:3]
    return render(request, "jokoa/garatzailea.html", locals())


def euskarazko_jokoak(request):
    euskaraz = JokoItzulpena.objects.filter(jokoa=OuterRef("pk"))
    proiektu_lagunak = (
        ProiektuLaguna.objects.filter(publikoa_da=True)
        .select_related("irudia")
        .order_by("izena")
    )
    jokoak_kop = JokoItzulpena.objects.count()
    jokoak_azken_urtea_kop = JokoItzulpena.objects.filter(
        erabilgarritasun_data__year=timezone.now().year
    ).count()

    jokoak = (
        Jokoa.objects.annotate(euskaraz=Exists(euskaraz))
        .filter(euskaraz=True)
        .prefetch_related("karatula", "logoa")
    )
    filter_params = request.GET.copy()
    if "ordena" not in filter_params:
        filter_params["ordena"] = "-jokoitzulpena__erabilgarritasun_data"
    filters = EuskarazkoJokoaFilter(filter_params, queryset=jokoak)

    return render(request, "jokoa/euskarazko_jokoak.html", locals())


def taldeak_berrizendatu(taldeak, choices):
    for taldea in taldeak:
        taldea["taldea"] = dict(choices).get(taldea["taldea"])


def euskarazko_jokoak_zenbakitan(request):
    euskaraz = JokoItzulpena.objects.filter(jokoa=OuterRef("pk"))
    euskarazko_jokoak = Jokoa.objects.annotate(euskaraz=Exists(euskaraz)).filter(
        euskaraz=True
    )

    datuak_argitaratze_data = (
        euskarazko_jokoak.filter(argitaratze_data__isnull=False)
        .annotate(urtea=Extract("argitaratze_data", "year"))
        .values(taldea=F("urtea"))
        .annotate(kopurua=Count("taldea"))
        .order_by("taldea")
    )
    datuak_lizentzia = euskarazko_jokoak.values(taldea=F("lizentzia")).annotate(
        kopurua=Count("taldea")
    )
    datuak_plataforma = euskarazko_jokoak.values(
        taldea=F("jokoitzulpena__plataformak__izena")
    ).annotate(kopurua=Count("taldea"))
    datuak_generoa = euskarazko_jokoak.values(taldea=F("generoak__izena")).annotate(
        kopurua=Count("taldea")
    )

    datuak_euskaratze_data = (
        euskarazko_jokoak.annotate(
            urtea=Extract("jokoitzulpena__erabilgarritasun_data", "year")
        )
        .values(taldea=F("urtea"))
        .exclude(urtea__isnull=True)
        .annotate(kopurua=Count("taldea"))
        .order_by("taldea")
    )
    datuak_ofizialtasuna = euskarazko_jokoak.values(
        taldea=F("jokoitzulpena__ofiziala_da")
    ).annotate(kopurua=Count("taldea"))
    datuak_euskaratze_mota = euskarazko_jokoak.values(
        taldea=F("jokoitzulpena__jatorria")
    ).annotate(kopurua=Count("taldea"))

    taldeak_berrizendatu(datuak_lizentzia, Jokoa._meta.get_field("lizentzia").choices)
    taldeak_berrizendatu(
        datuak_euskaratze_mota, JokoItzulpena._meta.get_field("jatorria").choices
    )
    taldeak_berrizendatu(datuak_ofizialtasuna, [(True, "Bai"), (False, "Ez")])

    return render(request, "jokoa/euskarazko_jokoak_zenbakitan.html", locals())
