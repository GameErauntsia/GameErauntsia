from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
	url(r'^$', 'gamerauntsia.gamer.views.index', name='gamer_index'),
    url(r'^(?P<username>[-\w]+)$', 'gamerauntsia.gamer.views.profile', name='gamer_profile'),
)