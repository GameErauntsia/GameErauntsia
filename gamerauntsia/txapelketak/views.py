from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import *
from django.core.urlresolvers import reverse

def index(request):
    items = Txapelketa.objects.filter(publikoa_da=True)
    return render_to_response('txapelketak/index.html', locals(),context_instance=RequestContext(request))

def txapelketa(request,slug):
    item = get_object_or_404(Txapelketa,slug=slug)
    next_parts = Partida.objects.filter(txapelketa=item, partaideak__isnull=False).order_by('jardunaldia').distinct()
    
    if item.mota == '0':
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
                    graphdata += "{'name': '???', 'seed': '???', 'id': 0},{'name': '???', 'seed': '???', 'id': 0}]"
            graphdata += "],"
        try:
            graphdata += "[[{'name': '"+item.irabazlea.get_izena()+"','seed': '"+str(item.irabazlea.id)+"','id': "+str(item.irabazlea.id)+"}]]]"
        except:
            graphdata += "[[{'name': '???','seed': '???','id': 0}]]]"

        #graphdata += "[[[{'name':'Urtzi','seed':1,'id':'urtzai'},{'name':'Jon','seed':2,'id':'jonny'}]],[[{'name':'Urtzi','seed':1,'id':'urtzai'}]]];"            
    else:
        list_sailkapena = item.get_partaideak('points')

    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))

@login_required
def txapelketa_insk(request,slug):
    user = request.user
    item = get_object_or_404(Txapelketa,slug=slug)
    item.jokalariak.add(user)
    item.save()
    return HttpResponseRedirect(reverse("txapelketa", kwargs={'slug':slug}))