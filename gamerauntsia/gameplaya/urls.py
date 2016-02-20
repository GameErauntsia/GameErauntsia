from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', 'gamerauntsia.gameplaya.views.index', name='gameplay_index'),
    url(r'^kategoriak/(?P<kategoria>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_category'),
    url(r'^mailak/(?P<maila>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_level'),
    url(r'^jokoak/(?P<jokoa>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_game'),
    url(r'^plataformak/(?P<plataforma>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_platform'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.gameplaya.views.gameplaya', name='gameplay'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': getattr(settings, 'MEDIA_ROOT', '')}),
    )
