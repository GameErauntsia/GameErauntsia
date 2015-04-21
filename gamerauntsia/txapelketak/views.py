from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import *
from django.core.urlresolvers import reverse
from gamerauntsia.utils.timeline import get_tweepy_api

def index(request):
    items = Txapelketa.objects.filter(publikoa_da=True).order_by('-pub_date')
    return render_to_response('txapelketak/index.html', locals(),context_instance=RequestContext(request))

def txapelketa(request,slug):
    item = get_object_or_404(Txapelketa,slug=slug)
    next_parts = Partida.objects.filter(Q(txapelketa=item), Q(partaideak__isnull=False),Q(emaitza__isnull=True) | Q(emaitza__iexact='')).order_by('date','jardunaldia').distinct()

    if item.mota == '0':
        if Partida.objects.filter(txapelketa=item,jardunaldia=1).exists():
            first_node = Partida.objects.get(txapelketa=item,jardunaldia=1)
            leaflvl = first_node.get_leafnodes(include_self=True)[0].get_level()

            graphdata = "["
            for x in range(leaflvl,-1,-1):
                graphdata += "["
                partidak = Partida.objects.filter(level=x,txapelketa=item)
                last_part = len(partidak) - 1
                for j,part in enumerate(partidak):
                    graphdata += "["
                    if part.partaideak.all():
                        if len(part.partaideak.all()) > 1:
                            last_gamer = len(part.partaideak.all()) - 1
                            for i,gamer in enumerate(part.partaideak.all()):
                                if i == last_gamer:
                                    graphdata += "{'name': '"+gamer.get_izena()+"', 'seed':"+str(gamer.id)+", 'id':"+str(gamer.id)+"}"
                                else:
                                    graphdata += "{'name': '"+gamer.get_izena()+"', 'seed':"+str(gamer.id)+", 'id':"+str(gamer.id)+"},"
                            if j == last_part:
                                graphdata += "]"
                            else:
                                graphdata += "],"
                        else:
                            gamer = part.partaideak.all()[0]
                            graphdata += "{'name': '"+gamer.get_izena()+"', 'seed':"+str(gamer.id)+", 'id':"+str(gamer.id)+"},{'name': 'Deskalifikatuta', 'seed': '0', 'id': 0}]"
                    else:
                        graphdata += "{'name': '???', 'seed': '???', 'id': 0},{'name': '???', 'seed': '???', 'id': 0}]"
                graphdata += "],"
            try:
                irabazlea = Partaidea.objects.get(txapelketa=item,irabazlea=True)
                graphdata += "[[{'name': '"+irabazlea.get_izena()+"','seed': '"+str(irabazlea.id)+"','id': "+str(irabazlea.id)+"}]]]"
            except:
                graphdata += "[[{'name': '???','seed': '???','id': 0}]]]"
        else:
            graphdata = ""

    else:
        list_sailkapena = item.get_partaideak(['-points','-win','lose'])

    #api = get_tweepy_api()
    #search = '#' + item.hashtag
    #tweets = api.search(q=search,count=25)

    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))

@login_required
def txapelketa_insk(request,slug):
    user = request.user
    item = get_object_or_404(Txapelketa,slug=slug)
    item.jokalariak.add(user)
    item.save()
    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug':slug}))

@login_required
def sortu_partaideak(request,slug):
    user = request.user
    item = get_object_or_404(Txapelketa,slug=slug)

    for partai in item.jokalariak.all():
        part = Partaidea()
        part.txapelketa = item
        part.save()
        part.jokalariak.add(partai)
        part.save()

    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug':slug}))