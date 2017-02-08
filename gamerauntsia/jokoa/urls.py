from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.jokoa.views.index', name='game_index'),

    # JOKOEN ITZULPENAK
   url(r'^euskarazko-bideojokoak/$', 'gamerauntsia.jokoen_itzulpenak.views.index',
       name='euskarazko_jokoak'),
   url(r'^jokoen-itzulpenak/bilatu', 'gamerauntsia.jokoen_itzulpenak.views.search_retro',
       name='search_itzulpenak'),

    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.jokoa.views.jokoa', name='game'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': getattr(settings, 'MEDIA_ROOT', '')}),
    )
