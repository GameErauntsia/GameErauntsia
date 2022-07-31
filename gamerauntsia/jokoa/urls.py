from django.conf.urls import url
from gamerauntsia.jokoa import views
from gamerauntsia.jokoen_itzulpenak import views as itzulpenakviews

urlpatterns = [
    url(r'^$', views.index, name='game_index'),

    # JOKOEN ITZULPENAK
    url(r'^euskarazko-bideojokoak/$', itzulpenakviews.index, name='euskarazko_jokoak'),
    url(r'^jokoen-itzulpenak/bilatu', itzulpenakviews.search_retro, name='search_itzulpenak'),
    ############
    url(r'^euskaraz$', views.euskarazko_jokoak, name='jokoak_euskaraz'),

    # Garatzaileak
    url(r'^garatzaileak$', views.garatzaileak, name='garatzaileak'),
    url(r'^garatzailea/(?P<slug>[-\w]+)$', views.garatzailea, name='garatzailea'),
    url(r'^(?P<slug>[-\w]+)$', views.jokoa, name='game'),
]
