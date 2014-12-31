from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.zerbitzariak.views.minecraft_server', name='minecraft_index'),
    url(r'^add$', 'gamerauntsia.zerbitzariak.views.minecraft_add', name='minecraft_add'),
)