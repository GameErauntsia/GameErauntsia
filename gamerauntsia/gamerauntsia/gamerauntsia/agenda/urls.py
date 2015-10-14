from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('gamerauntsia.agenda.views',
    url(r'^$', 'index', name='agenda_index'),
)