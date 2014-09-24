from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from gamerauntsia.base.feed import LatestEntriesFeed, LatestNewsFeed

admin.autodiscover()

urlpatterns = patterns('',
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
    url(r'^$', 'gamerauntsia.views.index', name='index'),

    # GAMEPLAYAK
    url(r'^gameplayak/', include('gamerauntsia.gameplaya.urls')),
    
    # BERRIAK
    url(r'^berriak/(?P<slug>[-\w]+)/$', lambda x, slug: HttpResponseRedirect(reverse('berria', args=[slug]))),
    url(r'^bloga/', include('gamerauntsia.berriak.urls'), name='bloga'),

    # JOKALARIAK
    url(r'^nor-gara/', include('gamerauntsia.gamer.urls')),
    url(r'^erabiltzaileak/$', RedirectView.as_view(url='/nor-gara/', permanent=False)),
    (r'^erabiltzaileak/', include('cssocialuser.urls')),
    (r'^erabiltzaileak/', include('registration.urls')),

    # FOROA
    url(r'^foroa/', include('django_simple_forum.urls')),

    # KONTAKTUA
    url(r'^kontaktua/$', 'gamerauntsia.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'gamerauntsia.kontaktua.views.bidali', name='kontaktua_bidali'),

    # BILAKETA
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'gamerauntsia.views.bilaketa', name='bilaketa'),

    #RSS FEED
    url(r'^rss/gameplayak$', LatestEntriesFeed()),
    url(r'^rss/bloga$', LatestNewsFeed()),

    # COMMENTS
    (r'^comments/', include('django_comments.urls')),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
