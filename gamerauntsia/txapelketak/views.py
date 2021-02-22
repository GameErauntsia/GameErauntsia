# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import Partida, Txapelketa, Partaidea
from gamerauntsia.txapelketak.forms import TaldeaForm
from django.urls import reverse
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
    items = Txapelketa.objects.filter(publikoa_da=True).order_by('-pub_date').select_related('irudia','jokoa')
    return render(request, 'txapelketak/index.html', locals())


def txapelketa(request, slug):
    item = get_object_or_404(Txapelketa.objects.select_related('irudia').prefetch_related('jokalariak__photo','adminak__photo'), slug=slug)
    list_sailkapena = item.get_partaideak(['-points', '-win', 'lose', '-average']).prefetch_related('jokalariak__photo')
    single_gamers = item.get_single_gamers()
    partidak = Partida.objects.filter(txapelketa=item).order_by('date').prefetch_related('partaideak__jokalariak')
    video_parts = Partida.objects.filter(Q(txapelketa=item), Q(bideoa__isnull=False)).exclude(bideoa__iexact='').order_by('-date')[:3]
    next_parts = Partida.objects.filter(Q(txapelketa=item), Q(partaideak__isnull=False),
                                        Q(emaitza__isnull=True) | Q(emaitza__iexact='')).order_by('date',
                                                                                                  'jardunaldia').distinct()

    return render(request, 'txapelketak/txapelketa.html', locals())

def zuhaitza(request, slug):
    item = get_object_or_404(Txapelketa.objects.select_related('irudia').prefetch_related('jokalariak__photo','adminak__photo'), slug=slug)
    jardunaldi_kopurua = Partida.objects.filter(txapelketa=item).aggregate(Max('jardunaldia'))['jardunaldia__max']
    roundlabels = ["{}. jardunaldia".format(zbk + 1) for zbk in range(jardunaldi_kopurua)]
    def get_partida(partida):
        return [{'name': gamer.get_izena(),
                 'seed': gamer.id,
                 'id': gamer.id}
                for gamer in partida.partaideak.all()]

    def get_jardunaldi_partidak(jardunaldi_zbk):
        jardunaldia = Partida.objects.filter(Q(txapelketa=item),
                                             Q(jardunaldia=jardunaldi_zbk+1)).prefetch_related('partaideak__jokalariak')
        return [get_partida(partida) for partida in jardunaldia]

    graphdata = [get_jardunaldi_partidak(jardunaldia) for jardunaldia in range(jardunaldi_kopurua)]

    try:
        irabazlea = Partaidea.objects.get(txapelketa=item, irabazlea=True)
        azkena = [[{'name':irabazlea.get_izena(),'seed': irabazlea.id,'id': irabazlea.id}]]
    except:
        azkena = [[{'name':'???','seed': '???','id': 0}]]
        graphdata.append(azkena)
    return render(request, 'txapelketak/zuhaitza.html', locals())

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
