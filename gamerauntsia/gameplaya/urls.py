from django.conf.urls import url
from gamerauntsia.gameplaya import views

urlpatterns = [
    url(r'^$', views.index, name='gameplay_index'),
    url(r'^kategoriak/(?P<kategoria>[-\w]+)$', views.index, name='gameplay_category'),
    url(r'^mailak/(?P<maila>[-\w]+)$', views.index, name='gameplay_level'),
    url(r'^jokoak/(?P<jokoa>[-\w]+)$', views.index, name='gameplay_game'),
    url(r'^plataformak/(?P<plataforma>[-\w]+)$', views.index, name='gameplay_platform'),
    url(r'^(?P<slug>[-\w]+)$', views.gameplaya, name='gameplay'),
]
