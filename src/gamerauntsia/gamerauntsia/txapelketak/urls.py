from django.urls import re_path
from gamerauntsia.txapelketak import views

urlpatterns = [
    re_path(r"^$", views.index, name="txapelketak_index"),
    re_path(r"^(?P<slug>[-\w]+)$", views.txapelketa, name="txapelketa"),
    re_path(r"^(?P<slug>[-\w]+)/zuhaitza", views.zuhaitza, name="zuhaitza"),
    re_path(
        r"^(?P<slug>[-\w]+)/izen_ematea$", views.txapelketa_insk, name="txapelketa_insk"
    ),
    re_path(
        r"^(?P<slug>[-\w]+)/sortu_partaideak$",
        views.sortu_partaideak,
        name="sortu_partaideak",
    ),
    re_path(
        r"^(?P<slug>[-\w]+)/partida/(?P<partida>[-\w]+)$", views.partida, name="partida"
    ),
    re_path(r"^(?P<slug>[-\w]+)/sortu-taldea$", views.sortu_taldea, name="sortu_taldea"),
    re_path(
        r"^(?P<slug>[-\w]+)/taldea/(?P<part_id>[-\w]+)$",
        views.partaidea,
        name="partaidea",
    ),
]
