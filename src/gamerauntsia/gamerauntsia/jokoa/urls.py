from django.urls import re_path
from gamerauntsia.jokoa import views
from gamerauntsia.jokoen_itzulpenak import views as itzulpenakviews

urlpatterns = [
    re_path(r"^$", views.index, name="game_index"),
    # Euskarazko jokoak
    re_path(
        r"^euskarazko-bideojokoak/zenbakitan$",
        views.euskarazko_jokoak_zenbakitan,
        name="euskarazko_jokoak_zenbakitan",
    ),
    re_path(
        r"^euskarazko-bideojokoak/$", views.euskarazko_jokoak, name="euskarazko_jokoak"
    ),
    # Garatzaileak
    re_path(r"^garatzaileak$", views.garatzaileak, name="garatzaileak"),
    re_path(r"^garatzaile-fitxa/(?P<slug>[-\w]+)$", views.garatzailea, name="garatzailea"),
    re_path(r"^(?P<slug>[-\w]+)$", views.jokoa, name="game"),
]
