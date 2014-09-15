from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from django.contrib import admin
from django.http import HttpResponse
from gamerauntsia.base.feed import LatestEntriesFeed, LatestNewsFeed

admin.autodiscover()

urlpatterns = patterns('',
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
    url(r'^$', 'gamerauntsia.views.index', name='index'),

    # GAMEPLAYAK
    url(r'^gameplayak/', include('gamerauntsia.gameplaya.urls')),
    
    # BERRIAK
    url(r'^berriak/(?P<slug>[-\w]+)/$', 'gamerauntsia.berriak.views.berria', name='berria'),
    url(r'^berriak/$', include('gamerauntsia.berriak.urls')),

    # JOKALARIAK
    url(r'^nor-gara/', include('gamerauntsia.gamer.urls')),
    (r'^profilak/', include('cssocialuser.urls')),

    # KONTAKTUA
    url(r'^kontaktua/$', 'gamerauntsia.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'gamerauntsia.kontaktua.views.bidali', name='kontaktua_bidali'),

    # BILAKETA
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'gamerauntsia.views.bilaketa', name='bilaketa'),

    #RSS FEED
    url(r'^rss/gameplayak$', LatestEntriesFeed()),
    url(r'^rss/berriak$', LatestNewsFeed()),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
