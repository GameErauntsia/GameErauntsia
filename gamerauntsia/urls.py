from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from gamerauntsia.base.feed import LatestEntriesFeed
from gamerauntsia.berriak.models import Berria

admin.autodiscover()



info_dict = {
    'queryset': Berria.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'berriak': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.base.views.index', name='index'),
    url(r'^googleaf6b2cbbb22dca3f\.html', 'gamerauntsia.base.views.google', name='google'),
    url(r'^sarrera/$', 'gamerauntsia.base.views.index', name='index'),
    url(r'^sarrera/bozkatuenak/$', 'gamerauntsia.tutorialak.views.bozkatuenak', name='tutorialak_bozkatuenak'),
    url(r'^tutorialak/(?P<slug>[-\w]+)/$', 'gamerauntsia.tutorialak.views.tutoriala', name='tutoriala'),
    url(r'^tutorialak/$', include('gamerauntsia.tutorialak.urls')),
    url(r'^tutorialak/aplikazioak/(?P<aplikazioa>[-\w]+)/$', 'gamerauntsia.tutorialak.views.tutorialak_aplikazioa', 
name='tutorialak_aplikazioa'),
    url(r'^tutorialak/gaiak/(?P<gaia>[-\w]+)/$', 'gamerauntsia.tutorialak.views.tutorialak_gaia', name='tutorialak_gaia'),
    url(r'^aplikazioak/(?P<slug>[-\w]+)/$', 'gamerauntsia.aplikazioak.views.aplikazioa', name='aplikazioa'),
    url(r'^aplikazioak/$', include('gamerauntsia.aplikazioak.urls')),
    url(r'^gaiak/$', 'gamerauntsia.tutorialak.views.gaiak', name='gaiak_index'),
    url(r'^gaiak/(?P<slug>[-\w]+)/$', 'gamerauntsia.tutorialak.views.gaia', name='gaia'),
    url(r'^berriak/(?P<slug>[-\w]+)/$', 'gamerauntsia.berriak.views.berria', name='berria'),
    url(r'^berriak/$', include('gamerauntsia.berriak.urls')),
    url(r'^kontaktua/$', 'gamerauntsia.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'gamerauntsia.kontaktua.views.bidali', name='kontaktua_bidali'),
    (r'^azken-berriak/feed/$', LatestEntriesFeed()),
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'gamerauntsia.views.bilaketa', name='bilaketa'),
    url(r'^rating/$', 'gamerauntsia.base.views.rating', name='rating'),
    (r'^comments/', include('django.contrib.comments.urls')),
    #(r'^grappelli/', include('grappelli.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('social_auth.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^kudeatu/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_DOC_ROOT}),
    )
