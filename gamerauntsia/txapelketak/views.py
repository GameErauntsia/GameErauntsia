from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import get_object_or_404
from gamerauntsia.txapelketak.models import *

def index(request):
    items = Txapelketa.objects.all()
    return render_to_response('txapelketak/index.html', locals(),context_instance=RequestContext(request))

def txapelketa(request,slug):
    item = get_object_or_404(Txapelketa,slug=slug)
    list_sailkapena = item.get_partaideak('points')

    kanporaketadatuak = [
                # [
                #   [ {"name" : u"Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : u"Joxepo", "id" : u"Joxepo", "seed" : 2} ],
                #   [ {"name" : u"Garikoitz Larrañaga", "id" : "gari_infernu", "seed" : 3},  {"name" : u"Mitxelon", "id" : u"Mitxelon", "seed" : 4}],
                #   [ {"name" : u"Joseba Galarraga", "id" : "joxhell", "seed" : 5},          {"name" : u"Haritz Odriozola", "id" : "theprodigyeh", "seed" : 6} ],
                #   [ {"name" : u"Eñaut Odriozola", "id" : "eodri", "seed" : 7},             {"name" : u"Iker Bellido", "id" : "robouteguiliam", "seed" : 8}],
                #   [ {"name" : u"Patxi Ordozgoiti", "id" : "ipatx", "seed" : 9},             {"name" : u"Ander Intxaurrondo", "id" : "marmoka", "seed" : 10} ],
                #   [ {"name" : u"yolocaust", "id" : "Olentzero", "seed" : 1},           {"name" : u"Bingen Galartza Iparragirre", "id" : "Galaipa", "seed" : 12}],
                #   [ {"name" : u"Arkaitz Lasarte", "id" : "arklasarte", "seed" : 13},          {"name" : u"Gari Galarza Aizpun", "id" : "Gari", "seed" : 14} ],
                #   [ {"name" : u"Diego Alvarez", "id" : "Gramity", "seed" : 15},          {"name" : u"Iker Ibarguren", "id" : "ikerib", "seed" : 16}]
                # ],
                # [
                #   [ {"name" : u"Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : u"Garikoitz Larrañaga", "id" : "gari_infernu", "seed" : 3} ],
                #   [ {"name" : u"Joseba Galarraga", "id" : "joxhell", "seed" : 5},          {"name" : u"Iker Bellido", "id" : "robouteguiliam", "seed" : 8} ],
                #   [ {"name" : u"Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10},           {"name" : u"yolocaust", "id" : "Olentzero", "seed" : 12} ],
                #   [ {"name" : u"Gari Galarza Aizpun", "id" : "Gari", "seed" : 14},           {"name" : u"Iker Ibarguren", "id" : "ikerib", "seed" : 15} ]
                # ],
                # [
                #   [ {"name" : u"Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : u"Joseba Galarraga", "id" : "joxhell", "seed" : 5} ],
                #   [ {"name" : u"Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10},           {"name" : u"Gari Galarza Aizpun", "id" : "Gari", "seed" : 14} ]
                # ],
                # [
                #   [ {"name" : u"Urtzi Odriozola", "id" : "urtzai", "seed" : 1},   {"name" : u"Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10} ]
                # ],
                # [
                #   [ {"name" : u"Urtzi Odriozola", "id" : "urtzai", "seed" : 1} ]
                # ]
            ]

    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))
