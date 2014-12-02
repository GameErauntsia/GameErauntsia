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
                [
                  [ {"name" : "Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : "Joxepo", "id" : "joxepo", "seed" : 2} ],
                  [ {"name" : "Garikoitz Larrañaga", "id" : "gari_infernu", "seed" : 3},  {"name" : "Mitxelon", "id" : "mitxelon", "seed" : 4}],
                  [ {"name" : "Joseba Galarraga", "id" : "joxhell", "seed" : 5},          {"name" : "Haritz Odriozola", "id" : "theprodigyeh", "seed" : 6} ],
                  [ {"name" : "Eñaut Odriozola", "id" : "eodri", "seed" : 7},             {"name" : "Iker Bellido", "id" : "robouteguiliam", "seed" : 8}],
                  [ {"name" : "Patxi Ordozgoiti", "id" : "ipatx", "seed" : 9},             {"name" : "Ander Intxaurrondo", "id" : "marmoka", "seed" : 10} ],
                  [ {"name" : "yolocaust", "id" : "Olentzero", "seed" : 1},           {"name" : "Bingen Galartza Iparragirre", "id" : "Galaipa", "seed" : 12}],
                  [ {"name" : "Arkaitz Lasarte", "id" : "arklasarte", "seed" : 13},          {"name" : "Gari Galarza Aizpun", "id" : "Gari", "seed" : 14} ],
                  [ {"name" : "Diego Alvarez", "id" : "Gramity", "seed" : 15},          {"name" : "Iker Ibarguren", "id" : "ikerib", "seed" : 16}]
                ],
                [
                  [ {"name" : "Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : "Garikoitz Larrañaga", "id" : "gari_infernu", "seed" : 3} ],
                  [ {"name" : "Joseba Galarraga", "id" : "joxhell", "seed" : 5},          {"name" : "Iker Bellido", "id" : "robouteguiliam", "seed" : 8} ],
                  [ {"name" : "Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10},           {"name" : "yolocaust", "id" : "Olentzero", "seed" : 12} ],
                  [ {"name" : "Gari Galarza Aizpun", "id" : "Gari", "seed" : 14},           {"name" : "Iker Ibarguren", "id" : "ikerib", "seed" : 15} ]
                ],
                [
                  [ {"name" : "Urtzi Odriozola", "id" : "urtzai", "seed" : 1},            {"name" : "Joseba Galarraga", "id" : "joxhell", "seed" : 5} ],
                  [ {"name" : "Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10},           {"name" : "Gari Galarza Aizpun", "id" : "Gari", "seed" : 14} ]
                ],
                [
                  [ {"name" : "Urtzi Odriozola", "id" : "urtzai", "seed" : 1},   {"name" : "Patxi Ordozgoiti", "id" : "ipatx", "seed" : 10} ]
                ],
                [
                  [ {"name" : "Urtzi Odriozola", "id" : "urtzai", "seed" : 1} ]
                ]
            ];

    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))
