from datetime import datetime

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.getb.models import Atala
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.utils.urls import get_urljson

GAMERAUNTSIA_TWITCH = "gamerauntsia"
TWITCH_URL = "https://api.twitch.tv/kraken/streams/"


def index(request):
    # stream_data = get_urljson(TWITCH_URL+GAMERAUNTSIA_TWITCH)
    # is_streaming = stream_data.get("stream", False)
    #
    twitch = None
    # if not is_streaming:
    #     gamerrak = GamerUser.objects.filter(Q(is_gamer=True),Q(twitch_channel__isnull=False),~Q(twitch_channel='')).order_by("-karma")
    #     for gamer in gamerrak:
    #         stream_data = get_urljson(TWITCH_URL+gamer.twitch_channel)
    #         is_streaming = stream_data.get("stream", False)
    #         if is_streaming:
    #             twitch = stream_data
    #             break
    # else:
    #     twitch = stream_data

    gameplayak = GamePlaya.objects.filter(status='1', publikoa_da=True, pub_date__lt=datetime.now()).order_by(
        '-pub_date')
    berriak = Berria.objects.filter(status='1', pub_date__lt=datetime.now()).order_by('-pub_date')
    if not twitch:
        atala = Atala.objects.latest('pub_date')
        gp = gameplayak[0]
        berria = berriak[0]

        if atala.pub_date > gp.pub_date and atala.pub_date > berria.pub_date:
            live = atala
            gameplayak = gameplayak[:3]
            berriak = berriak[:8]
        elif gp.pub_date > atala.pub_date and gp.pub_date > berria.pub_date:
            live = gp
            gameplayak = gameplayak[1:4]
            berriak = berriak[:8]
        else:
            live = berria
            gameplayak = gameplayak[:3]
            berriak = berriak[1:9]
    else:
        gameplayak = gameplayak[:3]
        berriak = berriak[:8]

    if Txapelketa.objects.filter(publikoa_da=True, status__in=('0', '1', '2')).exists():
        list_tx = Txapelketa.objects.filter(publikoa_da=True, status__in=('0', '1', '2')).order_by('-pub_date')
        if len(list_tx) > 1:
            txapelketak = list_tx
        else:
            txapelketa = list_tx[0]

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def bilaketa(request, bilatu):
    h = {}
    try:
        h['q'] = bilatu
    except:
        raise Http404
    return render_to_response('bilaketa.html', h, context_instance=RequestContext(request))
