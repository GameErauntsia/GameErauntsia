from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from gamerauntsia.base.feed import LatestEntriesFeed, LatestNewsFeed
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
    url(r'^$', 'gamerauntsia.views.index', name='index'),
    url(r'^lastlogin/$', 'gamerauntsia.gamer.views.lastlogin', name='gamer_lastlogin'),
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

    #AURKEZPENAK
    (r'^aurkezpenak/', include('gamerauntsia.aurkezpenak.urls')),

    #TXAPELKETAK
    (r'^txapelketak/', include('gamerauntsia.txapelketak.urls')),

    #MINECRAFT SERVER
    (r'^minecraft/', include('gamerauntsia.zerbitzariak.urls')),

    # FOROA
    url(r'^foroa/', include('django_simple_forum.urls')),

    # KONTAKTUA
    url(r'^kontaktua/$', 'gamerauntsia.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'gamerauntsia.kontaktua.views.bidali', name='kontaktua_bidali'),

    # TERMINOLOGIA
    url(r'^terminologia/$', 'gamerauntsia.base.views.index', name='terminologia'),

    # BILAKETA
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'gamerauntsia.views.bilaketa', name='bilaketa'),

    #RSS FEED
    url(r'^rss/gameplayak$', LatestEntriesFeed()),
    url(r'^rss/bloga$', LatestNewsFeed()),

    #FB
    url(r'^2b27b83ad50e677714b2dd832b42acc3', include('facebookpagewriter.urls')),

    # COMMENTS
    (r'^comments/', include('django_comments.urls')),

    # GRAPPELLI
    (r'^grappelli/', include('grappelli.urls')),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
    (r'^photologue/', include('photologue.urls')),

    #MEZUAK
    (r'^mezuak/', include('django_messages.urls')),

    #EGUTEGIA
    (r'^calendar/', include('django_bootstrap_calendar.urls')),

    #TODO
    (r'^todo/', include('todo.urls')),

    #ERABILERA ETA PRIBATUTASUNA
    (r'^erabilera-baldintzak/$', TemplateView.as_view(template_name='erabilera_baldintzak.html')),
    (r'^pribatutasun-politika/$', TemplateView.as_view(template_name='pribatutasun_politika.html')),
)



urlpatterns += patterns('gamerauntsia.gamer.views',
    url(r'^komunitatea/gehitu-artikulua$','add_article', name='add_article'),
    url(r'^komunitatea/gehitu-gameplaya$','add_gameplay', name='add_gameplay'),
    url(r'^komunitatea/editatu-profil$','edit_profile', name='edit_profile'),
    url(r'^komunitatea/editatu-profil-jakin$','edit_notifications', name='edit_profile_noti'),
    url(r'^komunitatea/editatu-profil-ord$','edit_computer', name='edit_profile_comp'),
    url(r'^komunitatea/editatu-profil-plat$','edit_platform', name='edit_profile_plat'),
    url(r'^komunitatea/editatu-profil-top$','edit_top_games', name='edit_profile_top'),
    url(r'^komunitatea/editatu-profil-pass/$','password_change', name='edit_profile_pass'),
    url(r'^komunitatea/editatu-profil-pass-done/$','password_change_done', name='edit_profile_pass_done'),
    url(r'^komunitatea/(?P<username>[-\w]+)$', 'profile', name='gamer_guestprofile'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
