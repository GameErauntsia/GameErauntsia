from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('gamerauntsia.gameplaya.views',
	url(r'^$', 'index', name='getb_index'),
    url(r'^(?P<slug>[-\w]+)$', 'atala', name='getb_atala'),
)