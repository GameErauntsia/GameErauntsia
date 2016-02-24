from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'gamerauntsia.log.views.index', name='log_index'),
                       url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.jokoa.views.jokoa', name='game'),
                       )

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': getattr(settings, 'MEDIA_ROOT', '')}),
                            )
