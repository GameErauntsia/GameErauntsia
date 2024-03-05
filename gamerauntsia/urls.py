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
from gamerauntsia.berriak.views import BerriaViewSet
from rest_framework.authtoken.views import obtain_auth_token

from gamerauntsia import views as indexviews
from gamerauntsia.gamer import views as gamerviews
from gamerauntsia.kontaktua import views as kontaktuaviews
from gamerauntsia.base import views as baseviews
from gamerauntsia.finished import views as finishedviews


router = DefaultRouter()

berria_list = BerriaViewSet.as_view({"get": "list"})

admin.autodiscover()

urlpatterns = [
    url(
        r"^robots.txt$",
        lambda r: HttpResponse(
            "User-agent: *\nSitemap: https://gamerauntsia.eus/sitemap.xml\nDisallow: ",
            content_type="text/plain",
        ),
    ),
    url(
        r"^3dedcce0621f78db1fdf62d2bb02148e.txt$",
        lambda r: HttpResponse(
            "3dedcce0621f78db1fdf62d2bb02148e", content_type="text/plain"
        ),
    ),
    url(r"^$", indexviews.index, name="index"),
    # GETB
    url(r"^getb/", include("gamerauntsia.getb.urls")),
    # GAMEPLAYAK
    url(r"^gameplayak/", include("gamerauntsia.gameplaya.urls")),
    # BLOGA
    url(r"^bloga/", include("gamerauntsia.berriak.urls"), name="bloga"),
    # JOKOAK
    url(r"^jokoak/", include("gamerauntsia.jokoa.urls"), name="jokoak"),
    # JOKO ITZULPENAK
    url(
        r"^itzulpenak/",
        include("gamerauntsia.joko_itzulpenak.urls"),
        name="joko_itzulpenak",
    ),
    # JOKALARIAK
    url(r"^komunitatea/", include("gamerauntsia.gamer.urls")),
    url(r"^komunitatea/", include("registration.backends.default.urls")),
    # AURKEZPENAK
    url(r"^aurkezpenak/", include("gamerauntsia.aurkezpenak.urls")),
    # TXAPELKETAK
    url(r"^txapelketak/", include("gamerauntsia.txapelketak.urls")),
    # MINECRAFT SERVER
    url(r"^zerbitzariak/", include("gamerauntsia.zerbitzariak.urls")),
    # FOROA
    url(r"^foroa/reset-topics$", gamerviews.reset_topics, name="reset_topics"),
    url(r"^foroa/", include("django_forum_app.urls")),
    # KONTAKTUA
    url(r"^kontaktua/$", kontaktuaviews.contact_form, name="kontaktua"),
    # TERMINOLOGIA
    url(r"^terminologia/$", baseviews.index, name="terminologia"),
    url(r"^terminologia/bilatu", baseviews.search_term, name="search_term"),
    # PODCAST
    url(r"^podcastak/", include("gamerauntsia.podcast.urls")),
    # BILAKETA
    url(r"^bilaketa?(?P<bilatu>[-\w]+)/$", indexviews.bilaketa, name="bilaketa"),
    # RSS FEED
    url(r"^feed/gameplayak$", LatestEntriesFeed()),
    url(r"^feed/bloga$", LatestNewsFeed()),
    # FB
    url(r"^2b27b83ad50e677714b2dd832b42acc3", include("facebookpagewriter.urls")),
    # COMMENTS
    url(r"^comments/", include("django_comments.urls")),
    # KUDEATU
    url(r"^kudeatu/", admin.site.urls),
    url(r"^photologue/", include("photologue.urls", namespace="photologue")),
    # TINYMCE
    url(r"^tinymce/", include("tinymce.urls")),
    # STAR RATINGS
    url(r"^ratings/", include("star_ratings.urls", namespace="ratings")),
    # APIA
    url(r"^api/1.0/", include("gamerauntsia.api.urls")),
    # STREAMING
    url(r"^streaming/", include("gamerauntsia.streaming.urls")),
    # POKEDEX
    url(r"^pokedex/", include("gamerauntsia.pokedex.urls")),
    # APP
    # Auth
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-token-auth/$', obtain_auth_token),
    # # url(r'^rest-user/$',views.UserViewSet),
    # url(r'^app/v1/', include('gamerauntsia.app.authentication.urls')),
    # url(r'^app/berriak/$', berria_list, name='app_berria_list'),
    # url(r'^app/berria/(?P<pk>[0-9]+)/$', 'gamerauntsia.berriak.views.berria_detail', name='app_berria_detail'),
    # url(r'^app/getb/$', 'gamerauntsia.getb.views.app_getb_list', name='app_getb_list'),
    # url(r'^app/getb/(?P<pk>[0-9]+)/$', 'gamerauntsia.getb.views.atala_detail', name='atala_detail'),
    # url(r'^app/txapelketak/$', 'gamerauntsia.txapelketak.views.txapelketa_list', name='app_txapelketak_list'),
    # url(r'^app/txapelketak/(?P<pk>[0-9]+)/$', 'gamerauntsia.txapelketak.views.txapelketa_detail', name='app_txapelketak_detail'),
    # ERABILERA ETA PRIBATUTASUNA
    # url(r'^erabilera-baldintzak/$', TemplateView.as_view(template_name='erabilera_baldintzak.html')),
    # url(r'^pribatutasun-politika/$', TemplateView.as_view(template_name='pribatutasun_politika.html')),
    # url(r'^gameplay-arauak/$', TemplateView.as_view(template_name='upload_gp.html')),
    # url(r'^cookie/$', TemplateView.as_view(template_name='cookie.html')),
    # LIZENTZIEI BURUZKO INFORMAZIOA
    url(r"^lizentzia$", TemplateView.as_view(template_name="license.html")),
    # SITEMAP
    url(r"^sitemap\.xml$", sitemapsviews.index, {"sitemaps": sitemaps}),
    url(
        r"^sitemap-(?P<section>.+)\.xml$",
        sitemapsviews.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # AJAX ESKAERAK
    url(r"^ajax/get_jokoak/", gamerviews.get_jokoak, name="ajax_jokoak"),
    url(r"^ajax/get_erabiltzaileak/", gamerviews.get_user, name="ajax_user"),
    url(r"^ajax/post_finished/", finishedviews.add_finished, name="ajax_finished"),
    # FLATPAGEAK
    url(r"^(?P<url>.*/)$", views.flatpage),
    # DEBUG
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

router.register(r"profile", UsersViewSet)
