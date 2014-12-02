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
          [{u"name" : u"Urtzi Odriozola", u"id" : u"urtzai", u"seed" : 1},{u"name" : u"Joxepo", u"id" : u"Joxepo", u"seed" : 2}],
          [{u"name" : u"Garikoitz Larrañaga", u"id" : u"gari_infernu", u"seed" : 3},{u"name" : u"Mitxelon", u"id" : u"Mitxelon", u"seed" : 4}],
          [{u"name" : u"Joseba Galarraga", u"id" : u"joxhell", u"seed" : 5},{u"name" : u"Haritz Odriozola", u"id" : u"theprodigyeh", u"seed" : 6}],
          [{u"name" : u"Eñaut Odriozola", u"id" : u"eodri", u"seed" : 7},{u"name" : u"Iker Bellido", u"id" : u"robouteguiliam", u"seed" : 8}],
          [{u"name" : u"Patxi Ordozgoiti", u"id" : u"ipatx", u"seed" : 9},{u"name" : u"Ander Intxaurrondo", u"id" : u"marmoka", u"seed" : 10}],
          [{u"name" : u"yolocaust", u"id" : u"Olentzero", u"seed" : 1},{u"name" : u"Bingen Galartza Iparragirre", u"id" : u"Galaipa", u"seed" : 12}],
          [{u"name" : u"Arkaitz Lasarte", u"id" : u"arklasarte", u"seed" : 13},{u"name" : u"Gari Galarza Aizpun", u"id" : u"Gari", u"seed" : 14}],
          [{u"name" : u"Diego Alvarez", u"id" : u"Gramity", u"seed" : 15},{u"name" : u"Iker Ibarguren", u"id" : u"ikerib", u"seed" : 16}]
        ],
        [
          [{u"name" : u"Urtzi Odriozola", u"id" : u"urtzai", u"seed" : 1},{u"name" : u"Garikoitz Larrañaga", u"id" : u"gari_infernu", u"seed" : 3}],
          [{u"name" : u"Joseba Galarraga", u"id" : u"joxhell", u"seed" : 5},{u"name" : u"Iker Bellido", u"id" : u"robouteguiliam", u"seed" : 8}],
          [{u"name" : u"Patxi Ordozgoiti", u"id" : u"ipatx", u"seed" : 10},{u"name" : u"yolocaust", u"id" : u"Olentzero", u"seed" : 12}],
          [{u"name" : u"Gari Galarza Aizpun", u"id" : u"Gari", u"seed" : 14},{u"name" : u"Iker Ibarguren", u"id" : u"ikerib", u"seed" : 15}]
        ],
        [
          [{u"name" : u"Urtzi Odriozola", u"id" : u"urtzai", u"seed" : 1},{u"name" : u"Joseba Galarraga", u"id" : u"joxhell", u"seed" : 5}],
          [{u"name" : u"Patxi Ordozgoiti", u"id" : u"ipatx", u"seed" : 10},{u"name" : u"Gari Galarza Aizpun", u"id" : u"Gari", u"seed" : 14}]
        ],
        [
          [{u"name" : u"Urtzi Odriozola", u"id" : u"urtzai", u"seed" : 1},{u"name" : u"Patxi Ordozgoiti", u"id" : u"ipatx", u"seed" : 10}]
        ],
        [
          [{u"name" : u"Urtzi Odriozola", u"id" : u"urtzai", u"seed" : 1}]
        ]
    ]
    return render_to_response('txapelketak/txapelketa.html', locals(),context_instance=RequestContext(request))
