from django.conf.urls import url
from gamerauntsia.txapelketak import views

urlpatterns = [
    url(r'^$', views.index, name='txapelketak_index'),
    url(r'^(?P<slug>[-\w]+)$', views.txapelketa, name='txapelketa'),
    url(r'^(?P<slug>[-\w]+)/izen_ematea$', views.txapelketa_insk, name='txapelketa_insk'),
    url(r'^(?P<slug>[-\w]+)/sortu_partaideak$', views.sortu_partaideak, name='sortu_partaideak'),
    url(r'^(?P<slug>[-\w]+)/partida/(?P<partida>[-\w]+)$', views.partida, name='partida'),
    url(r'^(?P<slug>[-\w]+)/sortu-taldea$', views.sortu_taldea, name='sortu_taldea'),
    url(r'^(?P<slug>[-\w]+)/taldea/(?P<part_id>[-\w]+)$', views.partaidea, name='partaidea'),
]
