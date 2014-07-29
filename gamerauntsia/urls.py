from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from django.contrib import admin
from gamerauntsia.base.feed import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.views.index', name='index'),

    # GAMEPLAYAK
    url(r'^gameplayak/', include('gamerauntsia.gameplaya.urls')),
    
    # BERRIAK
    url(r'^berriak/(?P<slug>[-\w]+)/$', 'gamerauntsia.berriak.views.berria', name='berria'),
    url(r'^berriak/$', include('gamerauntsia.berriak.urls')),

    # JOKALARIAK
    url(r'^nor-gara/', include('gamerauntsia.gamer.urls')),

    # KONTAKTUA
    url(r'^kontaktua/$', 'gamerauntsia.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'gamerauntsia.kontaktua.views.bidali', name='kontaktua_bidali'),

    # BILAKETA
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'gamerauntsia.views.bilaketa', name='bilaketa'),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
