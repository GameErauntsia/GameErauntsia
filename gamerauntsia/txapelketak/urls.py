from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.txapelketak.views.index', name='txapelketak_index'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.txapelketak.views.txapelketa', name='txapelketa'),
    url(r'^(?P<slug>[-\w]+)/izen_ematea$', 'gamerauntsia.txapelketak.views.txapelketa_insk', name='txapelketa_insk'),
    url(r'^(?P<slug>[-\w]+)/sortu_partaideak$', 'gamerauntsia.txapelketak.views.sortu_partaideak', name='sortu_partaideak'),
    url(r'^(?P<slug>[-\w]+)/partida/(?P<partida>[-\w]+)$', 'gamerauntsia.txapelketak.views.partida', name='partida'),
    url(r'^(?P<slug>[-\w]+)/partaidea/(?P<part_id>[-\w]+)$', 'gamerauntsia.txapelketak.views.partaidea', name='partaidea'),
)