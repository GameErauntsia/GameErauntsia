from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from gamerauntsia.app.authentication.viewsets import UsersViewSet
from django.contrib.flatpages import views

from django.contrib.sitemaps import views as sitemapsviews
from .sitemaps import sitemaps

from gamerauntsia.base.feed import LatestEntriesFeed, LatestNewsFeed
from gamerauntsia.log.views import DenboralerroaViewSet
from gamerauntsia.berriak.views import BerriaViewSet
from rest_framework.authtoken.views import obtain_auth_token

from gamerauntsia import views as indexviews
from gamerauntsia.gamer import views as gamerviews
from gamerauntsia.kontaktua import views as kontaktuaviews
from gamerauntsia.base import views as baseviews

router = DefaultRouter()

berria_list = BerriaViewSet.as_view({'get': 'list'})
denboralerroa_list = DenboralerroaViewSet.as_view({'get': 'list'})

admin.autodiscover()

urlpatterns = [
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain")),
    url(r'^3dedcce0621f78db1fdf62d2bb02148e.txt$', lambda r: HttpResponse("3dedcce0621f78db1fdf62d2bb02148e", content_type="text/plain")),

    url(r'^$', indexviews.index, name='index'),

    # GETB
    url(r'^getb/', include('gamerauntsia.getb.urls')),

    # GAMEPLAYAK
    url(r'^gameplayak/', include('gamerauntsia.gameplaya.urls')),

    # BLOGA
    url(r'^bloga/', include('gamerauntsia.berriak.urls'), name='bloga'),

    # DENBORA LERROA
    url(r'^denboralerroa/', include('gamerauntsia.log.urls'), name='log'),

    # JOKOAK
    url(r'^jokoak/', include('gamerauntsia.jokoa.urls'), name='jokoak'),

    # JOKALARIAK
    url(r'^komunitatea/', include('gamerauntsia.gamer.urls')),
    url(r'^komunitatea/', include('registration.backends.default.urls')),

    # AURKEZPENAK
    url(r'^aurkezpenak/', include('gamerauntsia.aurkezpenak.urls')),

    # TXAPELKETAK
    url(r'^txapelketak/', include('gamerauntsia.txapelketak.urls')),

    # MINECRAFT SERVER
    url(r'^zerbitzariak/', include('gamerauntsia.zerbitzariak.urls')),

    # FOROA
    url(r'^foroa/reset-topics$', gamerviews.reset_topics, name='reset_topics'),
    url(r'^foroa/', include('django_forum_app.urls')),

    # KONTAKTUA
    url(r'^kontaktua/$', kontaktuaviews.index, name='kontaktua'),
    url(r'^kontaktua/bidali/$', kontaktuaviews.bidali, name='kontaktua_bidali'),

    # TERMINOLOGIA
    url(r'^terminologia/$', baseviews.index, name='terminologia'),
    url(r'^terminologia/bilatu', baseviews.search_term, name='search_term'),

    # PODCAST
    url(r"^podcastak/", include("podcasting.urls")),

    # BILAKETA
    url(r'^bilaketa?(?P<bilatu>[-\w]+)/$', indexviews.bilaketa, name='bilaketa'),

    # RSS FEED
    url(r'^feed/gameplayak$', LatestEntriesFeed()),
    url(r'^feed/bloga$', LatestNewsFeed()),
    url(r"^feed/podcastak/", include("podcasting.urls_feeds")),

    # FB
    url(r'^2b27b83ad50e677714b2dd832b42acc3', include('facebookpagewriter.urls')),

    # COMMENTS
    url(r'^comments/', include('django_comments.urls')),

    # KUDEATU
    url(r'^kudeatu/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

    # MEZUAK
    url(r'^mezuak/', include('django_messages.urls')),

    # TINYMCE
    url(r'^tinymce/', include('tinymce.urls')),

    # STAR RATINGS
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

    # APIA
    url(r'^api/1.0/', include('gamerauntsia.api.urls')),

    # ERABILERA ETA PRIBATUTASUNA
    url(r'^erabilera-baldintzak/$', TemplateView.as_view(template_name='erabilera_baldintzak.html')),
    url(r'^pribatutasun-politika/$', TemplateView.as_view(template_name='pribatutasun_politika.html')),
    url(r'^gameplay-arauak/$', TemplateView.as_view(template_name='upload_gp.html')),
    url(r'^cookie/$', TemplateView.as_view(template_name='cookie.html')),

    # SITEMAP
    url(r'^sitemap\.xml$', sitemapsviews.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemapsviews.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    # AJAX ESKAERAK
    url(r'^ajax/get_jokoak/', gamerviews.get_jokoak, name='ajax_jokoak'),
    url(r'^ajax/get_erabiltzaileak/', gamerviews.get_user, name='ajax_user'),

    url(r'^(?P<url>.*/)$', views.flatpage),
]

router.register(r'profile', UsersViewSet)
