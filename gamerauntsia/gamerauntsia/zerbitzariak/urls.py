from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^minecraft$', 'gamerauntsia.zerbitzariak.views.minecraft_server', name='minecraft_index'),
    url(r'^minecraft/mapa$', 'gamerauntsia.zerbitzariak.views.minecraft_mapa', name='minecraft_mapa'),
    url(r'^minecraft/add$', 'gamerauntsia.zerbitzariak.views.minecraft_add', name='minecraft_add'),
    url(r'^mumble$', TemplateView.as_view(template_name='zerbitzariak/mumble.html'), name='mumble_index'),
)
