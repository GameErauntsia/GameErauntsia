from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
	url(r'^$', 'gamerauntsia.gameplaya.views.index', name='gameplay_index'),
    url(r'^kategoriak/(?P<kategoria>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_category'),
    url(r'^mailak/(?P<maila>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_level'),
    url(r'^jokoak/(?P<jokoa>[-\w]+)$', 'gamerauntsia.gameplaya.views.index', name='gameplay_game'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.gameplaya.views.gameplaya', name='gameplay'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )