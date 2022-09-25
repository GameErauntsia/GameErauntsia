from django.conf.urls import url
from gamerauntsia.jokoa import views
from gamerauntsia.jokoen_itzulpenak import views as itzulpenakviews

urlpatterns = [
    url(r'^$', views.index, name='game_index'),

    # Euskarazko jokoak
    url(r'^euskarazko-bideojokoak/$', views.euskarazko_jokoak, name='euskarazko_jokoak'),

    # Garatzaileak
    url(r'^garatzaileak$', views.garatzaileak, name='garatzaileak'),
    url(r'^garatzaile-fitxa/(?P<slug>[-\w]+)$', views.garatzailea, name='garatzailea'),
    url(r'^(?P<slug>[-\w]+)$', views.jokoa, name='game'),
]
