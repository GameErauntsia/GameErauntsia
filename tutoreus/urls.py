from django.conf.urls import patterns, include, url
from tutoreus import settings
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from tutoreus.base.feed import LatestEntriesFeed
from tutoreus.berriak.models import Berria

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
    url(r'^$', 'tutoreus.base.views.index', name='index'),
    url(r'^googleaf6b2cbbb22dca3f\.html', 'tutoreus.base.views.google', name='google'),
    url(r'^sarrera/$', 'tutoreus.base.views.index', name='index'),
    url(r'^sarrera/bozkatuenak/$', 'tutoreus.tutorialak.views.bozkatuenak', name='tutorialak_bozkatuenak'),
    url(r'^tutorialak/(?P<slug>[-\w]+)/$', 'tutoreus.tutorialak.views.tutoriala', name='tutoriala'),
    url(r'^tutorialak/$', include('tutoreus.tutorialak.urls')),
    url(r'^tutorialak/aplikazioak/(?P<aplikazioa>[-\w]+)/$', 'tutoreus.tutorialak.views.tutorialak_aplikazioa', 
name='tutorialak_aplikazioa'),
    url(r'^tutorialak/gaiak/(?P<gaia>[-\w]+)/$', 'tutoreus.tutorialak.views.tutorialak_gaia', name='tutorialak_gaia'),
    url(r'^aplikazioak/(?P<slug>[-\w]+)/$', 'tutoreus.aplikazioak.views.aplikazioa', name='aplikazioa'),
    url(r'^aplikazioak/$', include('tutoreus.aplikazioak.urls')),
    url(r'^gaiak/$', 'tutoreus.tutorialak.views.gaiak', name='gaiak_index'),
    url(r'^gaiak/(?P<slug>[-\w]+)/$', 'tutoreus.tutorialak.views.gaia', name='gaia'),
    url(r'^berriak/(?P<slug>[-\w]+)/$', 'tutoreus.berriak.views.berria', name='berria'),
    url(r'^berriak/$', include('tutoreus.berriak.urls')),
    url(r'^kontaktua/$', 'tutoreus.kontaktua.views.index', name='kontaktua'),
    url(r'^kontaktua/bidali/$', 'tutoreus.kontaktua.views.bidali', name='kontaktua_bidali'),
    (r'^azken-berriak/feed/$', LatestEntriesFeed()),
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', 'tutoreus.views.bilaketa', name='bilaketa'),
    url(r'^rating/$', 'tutoreus.base.views.rating', name='rating'),
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
