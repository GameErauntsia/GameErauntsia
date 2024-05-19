from django.conf import settings
from django.urls import include, re_path
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


router = DefaultRouter()

berria_list = BerriaViewSet.as_view({"get": "list"})

admin.autodiscover()

urlpatterns = [
    re_path(
        r"^robots.txt$",
        lambda r: HttpResponse(
            "User-agent: *\nSitemap: https://gamerauntsia.eus/sitemap.xml\nDisallow: ",
            content_type="text/plain",
        ),
    ),
    re_path(
        r"^3dedcce0621f78db1fdf62d2bb02148e.txt$",
        lambda r: HttpResponse(
            "3dedcce0621f78db1fdf62d2bb02148e", content_type="text/plain"
        ),
    ),
    re_path(r"^$", indexviews.index, name="index"),
    # GETB
    re_path(r"^getb/", include("gamerauntsia.getb.urls")),
    # GAMEPLAYAK
    re_path(r"^gameplayak/", include("gamerauntsia.gameplaya.urls")),
    # BLOGA
    re_path(r"^bloga/", include("gamerauntsia.berriak.urls"), name="bloga"),
    # JOKOAK
    re_path(r"^jokoak/", include("gamerauntsia.jokoa.urls"), name="jokoak"),
    # JOKO ITZULPENAK
    re_path(
        r"^itzulpenak/",
        include("gamerauntsia.joko_itzulpenak.urls"),
        name="joko_itzulpenak",
    ),
    # JOKALARIAK
    re_path(r"^komunitatea/", include("gamerauntsia.gamer.urls")),
    re_path(r"^komunitatea/", include("registration.backends.default.urls")),
    # AURKEZPENAK
    re_path(r"^aurkezpenak/", include("gamerauntsia.aurkezpenak.urls")),
    # TXAPELKETAK
    re_path(r"^txapelketak/", include("gamerauntsia.txapelketak.urls")),
    # MINECRAFT SERVER
    re_path(r"^zerbitzariak/", include("gamerauntsia.zerbitzariak.urls")),
    # FOROA
    re_path(r"^foroa/reset-topics$", gamerviews.reset_topics, name="reset_topics"),
    re_path(r"^foroa/", include("django_forum_app.urls")),
    # KONTAKTUA
    re_path(r"^kontaktua/$", kontaktuaviews.contact_form, name="kontaktua"),
    # TERMINOLOGIA
    re_path(r"^terminologia/$", baseviews.index, name="terminologia"),
    re_path(r"^terminologia/bilatu", baseviews.search_term, name="search_term"),
    # PODCAST
    re_path(r"^podcastak/", include("gamerauntsia.podcast.urls")),
    # BILAKETA
    re_path(r"^bilaketa?(?P<bilatu>[-\w]+)/$", indexviews.bilaketa, name="bilaketa"),
    # RSS FEED
    re_path(r"^feed/gameplayak$", LatestEntriesFeed()),
    re_path(r"^feed/bloga$", LatestNewsFeed()),
    # COMMENTS
    re_path(r"^comments/", include("django_comments.urls")),
    # KUDEATU
    re_path(r"^kudeatu/", admin.site.urls),
    re_path(r"^photologue/", include("photologue.urls", namespace="photologue")),
    # TINYMCE
    re_path(r"^tinymce/", include("tinymce.urls")),
    # STAR RATINGS
    re_path(r"^ratings/", include("star_ratings.urls", namespace="ratings")),
    # APIA
    re_path(r"^api/1.0/", include("gamerauntsia.api.urls")),
    # STREAMING
    re_path(r"^streaming/", include("gamerauntsia.streaming.urls")),
    # POKEDEX
    re_path(r"^pokedex/", include("gamerauntsia.pokedex.urls")),
    # LIZENTZIEI BURUZKO INFORMAZIOA
    re_path(r"^lizentzia$", TemplateView.as_view(template_name="license.html")),
    # SITEMAP
    re_path(r"^sitemap\.xml$", sitemapsviews.index, {"sitemaps": sitemaps}),
    re_path(
        r"^sitemap-(?P<section>.+)\.xml$",
        sitemapsviews.sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # AJAX ESKAERAK
    re_path(r"^ajax/get_jokoak/", gamerviews.get_jokoak, name="ajax_jokoak"),
    re_path(r"^ajax/get_erabiltzaileak/", gamerviews.get_user, name="ajax_user"),
    # FLATPAGEAK
    re_path(r"^(?P<url>.*/)$", views.flatpage),
    # DEBUG
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

router.register(r"profile", UsersViewSet)
