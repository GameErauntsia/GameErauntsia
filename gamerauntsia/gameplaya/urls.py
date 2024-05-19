from django.urls import re_path
from gamerauntsia.gameplaya import views

urlpatterns = [
    re_path(r"^$", views.index, name="gameplay_index"),
    re_path(
        r"^kategoriak/(?P<kategoria>[-\w]+)$", views.index, name="gameplay_category"
    ),
    re_path(r"^mailak/(?P<maila>[-\w]+)$", views.index, name="gameplay_level"),
    re_path(r"^jokoak/(?P<jokoa>[-\w]+)$", views.index, name="gameplay_game"),
    re_path(
        r"^plataformak/(?P<plataforma>[-\w]+)$", views.index, name="gameplay_platform"
    ),
    re_path(r"^(?P<slug>[-\w]+)$", views.gameplaya, name="gameplay"),
]
