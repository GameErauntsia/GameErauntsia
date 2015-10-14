from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.berriak.views.index', name='berriak_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'gamerauntsia.berriak.views.berria', name='berria'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':  getattr(settings, 'MEDIA_ROOT', '')}),
    )
