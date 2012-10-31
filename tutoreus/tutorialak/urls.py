from django.conf.urls import patterns, include, url
from tutoreus import settings

urlpatterns = patterns('',
    url(r'^$', 'tutoreus.tutorialak.views.index', name='tutorialak_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )