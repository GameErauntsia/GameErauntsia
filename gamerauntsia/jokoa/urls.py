from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.jokoa.views.index', name='aplikazioak_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root':     settings.MEDIA_ROOT}),
    )