from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.gameplaya.views.index', name='gameplay_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )