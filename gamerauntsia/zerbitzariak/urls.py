from django.conf.urls import url
from django.views.generic import TemplateView
from gamerauntsia.zerbitzariak import views

urlpatterns = [
    url(r"^minecraft$", views.minecraft_server, name="minecraft_index"),
    url(r"^minecraft/status$", views.minecraft_status, name="minecraft_status"),
    url(r"^minecraft/mapa$", views.minecraft_mapa, name="minecraft_mapa"),
    url(r"^minecraft/add$", views.minecraft_add, name="minecraft_add"),
    url(
        r"^mumble$",
        TemplateView.as_view(template_name="zerbitzariak/mumble.html"),
        name="mumble_index",
    ),
]
