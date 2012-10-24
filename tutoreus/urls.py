from django.conf.urls import patterns, include, url
from tutoreus import settings
from django.contrib import admin

from base.feed import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'base.views.index', name='index'),
    url(r'^sarrera/$', 'base.views.index', name='index'),
    url(r'^tutorialak/bozkatuenak/$', 'tutorialak.views.bozkatuenak', name='tutorialak_bozkatuenak'),
    url(r'^tutorialak/(?P<slug>[-\w]+)/$', 'tutorialak.views.tutoriala', name='tutoriala'),
    url(r'^tutorialak/$', include('tutorialak.urls')),
    url(r'^tutorialak/aplikazioak/(?P<aplikazioa>[-\w]+)/$', 'tutorialak.views.tutorialak_aplikazioa', name='tutorialak_aplikazioa'),
    url(r'^tutorialak/gaiak/(?P<gaia>[-\w]+)/$', 'tutorialak.views.tutorialak_gaia', name='tutorialak_gaia'),
    url(r'^aplikazioak/(?P<slug>[-\w]+)/$', 'aplikazioak.views.aplikazioa', name='aplikazioa'),
    url(r'^aplikazioak/$', include('aplikazioak.urls')),
    url(r'^gaiak/$', 'tutorialak.views.gaiak', name='gaiak_index'),
    url(r'^gaiak/(?P<slug>[-\w]+)/$', 'tutorialak.views.gaia', name='gaia'),
    url(r'^berriak/(?P<slug>[-\w]+)/$', 'berriak.views.berria', name='berria'),
    url(r'^berriak/$', include('berriak.urls')),
    url(r'^kontaktua/$', 'kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'kontaktua.views.bidali', name='kontaktua_bidali'),
    (r'^azken-berriak/feed/$', LatestEntriesFeed()),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
