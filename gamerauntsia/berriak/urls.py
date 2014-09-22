from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.berriak.views.index', name='berriak_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'gamerauntsia.berriak.views.berria', name='berria'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )