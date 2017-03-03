from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import Partida, Txapelketa, Partaidea
from gamerauntsia.txapelketak.forms import TaldeaForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from gamerauntsia.txapelketak.serializers import TxapelketaSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def app_txapelketa_profile(request, pk):
    # 	return JSONResponse({1:1})
    item = Txapelketa.objects.get(pk=pk)
    # 	gameplayak = GamePlaya.objects.filter(publikoa_da=True,status='1', erabiltzailea=user_prof, pub_date__lt=datetime.now()).order_by('-pub_date')
    list_sailkapena = item.get_partaideak(['-points', '-win', 'lose', '-average'])

    # 	gameplayak = {"aaaaa":2}
    # 	data = serializers.serialize('json', gameplayak, fields=('izenburua','slug'))
    data = serialize('json', list_sailkapena, fields=('izenburua', 'slug'))

    # 	serializer =  GameUserSerializer(user_prof)
    # 	serializer2 = GamePlayaSerializer(gameplayak)
    # 	response_data['user'] = serializer.data
    # 	response_data['gameplayak'] = data
    # 	combined = chain(serializer.data, gameplayak)
    # 	return JSONResponse(combined)
    # 	return JSONResponse(json.dumps(list_sailkapena), content_type="application/json")
    return JSONResponse(data)


# 	return HttpResponse(json.dumps(combined), content_type="application/json")

@csrf_exempt
def txapelketa_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        txapelketak = Txapelketa.objects.all()
        serializer = TxapelketaSerializer(txapelketak, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def txapelketa_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        txapelketa = Txapelketa.objects.get(pk=pk)
    except Txapelketa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TxapelketaSerializer(txapelketa)
        return JSONResponse(serializer.data)
    elif request.method == 'HEAD':
        serializer = TxapelketaSerializer(txapelketa)
        return JSONResponse(serializer.data)


def index(request):
    items = Txapelketa.objects.filter(publikoa_da=True).order_by('-pub_date')
    return render(request, 'txapelketak/index.html', locals())


def txapelketa(request, slug):
    item = get_object_or_404(Txapelketa, slug=slug)
    video_parts = Partida.objects.filter(Q(txapelketa=item), Q(bideoa__isnull=False)).exclude(bideoa__iexact='').order_by('-date')[:3]
    next_parts = Partida.objects.filter(Q(txapelketa=item), Q(partaideak__isnull=False),
                                        Q(emaitza__isnull=True) | Q(emaitza__iexact='')).order_by('date',
                                                                                                  'jardunaldia').distinct()

    if item.mota == '0' or item.mota == '2':
        root_exists = Partida.objects.filter(Q(txapelketa=item), Q(parent__isnull=True),
                                             Q(txapelketa__mota='0') | Q(txapelketa__mota='2', is_playoff=True))
        if root_exists:
            first_node = root_exists[0]
            leaflvl = first_node.get_leafnodes(include_self=True)[0].get_level()

            graphdata = "["
            for x in range(leaflvl, -1, -1):
                graphdata += "["
                partidak = Partida.objects.filter(Q(level=x), Q(txapelketa=item),
                                                  Q(txapelketa__mota='0') | Q(txapelketa__mota='2', is_playoff=True))
                last_part = len(partidak) - 1
                for j, part in enumerate(partidak):
                    graphdata += "["
                    if part.partaideak.all():
                        if len(part.partaideak.all()) > 1:
                            last_gamer = len(part.partaideak.all()) - 1
                            for i, gamer in enumerate(part.partaideak.all()):
                                if i == last_gamer:
                                    graphdata += "{'name': '" + gamer.get_izena() + "', 'seed':" + str(
                                        gamer.id) + ", 'id':" + str(gamer.id) + "}"
                                else:
                                    graphdata += "{'name': '" + gamer.get_izena() + "', 'seed':" + str(
                                        gamer.id) + ", 'id':" + str(gamer.id) + "},"
                            if j == last_part:
                                graphdata += "]"
                            else:
                                graphdata += "],"
                        else:
                            gamer = part.partaideak.all()[0]
                            graphdata += "{'name': '" + gamer.get_izena() + "', 'seed':" + str(
                                gamer.id) + ", 'id':" + str(
                                gamer.id) + "},{'name': 'Deskalifikatuta', 'seed': '0', 'id': 0}]"
                    else:
                        graphdata += "{'name': '???', 'seed': '???', 'id': 0},{'name': '???', 'seed': '???', 'id': 0}]"
                graphdata += "],"
            try:
                irabazlea = Partaidea.objects.get(txapelketa=item, irabazlea=True)
                graphdata += "[[{'name': '" + irabazlea.get_izena() + "','seed': '" + str(
                    irabazlea.id) + "','id': " + str(irabazlea.id) + "}]]]"
            except:
                graphdata += "[[{'name': '???','seed': '???','id': 0}]]]"
        else:
            graphdata = ""

        if item.mota == '2':
            list_sailkapena = item.get_partaideak(['-points', '-win', 'lose', '-average'])

    else:
        list_sailkapena = item.get_partaideak(['-points', '-win', 'lose', '-average'])

    # api = get_tweepy_api()
    # search = '#' + item.hashtag
    # tweets = api.search(q=search,count=25)

    return render(request, 'txapelketak/txapelketa.html', locals())


def partaidea(request, slug, part_id):
    item = get_object_or_404(Txapelketa, slug=slug)
    partaidea = get_object_or_404(Partaidea, id=part_id)
    next_parts = Partida.objects.filter(Q(txapelketa=item), Q(partaideak=partaidea),
                                        Q(emaitza__isnull=True) | Q(emaitza__iexact='')).order_by('date',
                                                                                                  'jardunaldia').distinct()
    return render(request, 'txapelketak/partaidea.html', locals())


def partida(request, slug, partida):
    item = get_object_or_404(Txapelketa, slug=slug)
    queryset = Partida.objects.filter(emaitza__isnull=False).exclude(emaitza__iexact="")
    partida = get_object_or_404(queryset, id=partida)
    other_parts = Partida.objects.filter(txapelketa=item).exclude(id=partida.id, emaitza__isnull=False).order_by('date',
                                                                                                                 'jardunaldia').distinct()
    return render(request, 'txapelketak/partida.html', locals())


@login_required
def txapelketa_insk(request, slug):
    user = request.user
    item = get_object_or_404(Txapelketa, slug=slug)
    item.jokalariak.add(user)
    item.save()
    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug': slug}))


@login_required
def sortu_partaideak(request, slug):
    item = get_object_or_404(Txapelketa, slug=slug)

    for partai in item.jokalariak.all():
        part = Partaidea()
        part.txapelketa = item
        part.save()
        part.jokalariak.add(partai)
        part.save()

    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug': slug}))


@login_required
def sortu_taldea(request, slug):
    kapitaina = request.user
    txapelketa = get_object_or_404(Txapelketa, slug=slug)

    if request.method == 'POST':
        teamform = TaldeaForm(request.POST)
        if teamform.is_valid():
            team = teamform.save(commit=False)
            team.kapitaina = kapitaina
            team.save()
            teamform.save_m2m()
            return HttpResponseRedirect(reverse("partaidea", kwargs={'part_id': team.id}))
    else:
        teamform = TaldeaForm()
    return render(request, 'txapelketak/sortu_taldea.html', locals())
