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
    url(r'^komunitatea/$', 'gamerauntsia.gamer.views.community', name='komunitatea'),
    (r'^komunitatea/', include('cssocialuser.urls')),
    (r'^komunitatea/', include('registration.urls')),

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

    #FB
    url(r'^2b27b83ad50e677714b2dd832b42acc3', include('facebookpagewriter.urls')),

    # COMMENTS
    (r'^comments/', include('django_comments.urls')),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),
)

urlpatterns += patterns('gamerauntsia.gamer.views',
    url(r'^komunitatea/editatu-profil-jakin$','edit_notifications', name='edit_profile_noti'), 
    url(r'^komunitatea/editatu-profil-plat$','edit_platform', name='edit_profile_plat'),  
    url(r'^komunitatea/(?P<username>[-\w]+)$', 'guestprofile', name='gamer_guestprofile'), 
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
