from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.log.views.index', name='log_index'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.jokoa.views.jokoa', name='game'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root':     settings.MEDIA_ROOT}),
    )