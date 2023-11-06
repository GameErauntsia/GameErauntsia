from django.urls import re_path
from django.views.generic import TemplateView
from gamerauntsia.zerbitzariak import views

urlpatterns = [
    re_path(r"^minecraft$", views.minecraft_server, name="minecraft_index"),
    re_path(r"^minecraft/status$", views.minecraft_status, name="minecraft_status"),
    re_path(r"^minecraft/mapa$", views.minecraft_mapa, name="minecraft_mapa"),
    re_path(r"^minecraft/add$", views.minecraft_add, name="minecraft_add"),
    re_path(
        r"^mumble$",
        TemplateView.as_view(template_name="zerbitzariak/mumble.html"),
        name="mumble_index",
    ),
]
