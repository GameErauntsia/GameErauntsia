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
from gamerauntsia.finished import views as finishedviews


router = DefaultRouter()

berria_list = BerriaViewSet.as_view({"get": "list"})

admin.autodiscover()

re_pathpatterns = [
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
    re_path(r"^getb/", include("gamerauntsia.getb.re_paths")),
    # GAMEPLAYAK
    re_path(r"^gameplayak/", include("gamerauntsia.gameplaya.re_paths")),
    # BLOGA
    re_path(r"^bloga/", include("gamerauntsia.berriak.re_paths"), name="bloga"),
    # JOKOAK
    re_path(r"^jokoak/", include("gamerauntsia.jokoa.re_paths"), name="jokoak"),
    # JOKO ITZULPENAK
    re_path(
        r"^itzulpenak/",
        include("gamerauntsia.joko_itzulpenak.re_paths"),
        name="joko_itzulpenak",
    ),
    # JOKALARIAK
    re_path(r"^komunitatea/", include("gamerauntsia.gamer.re_paths")),
    re_path(r"^komunitatea/", include("registration.backends.default.re_paths")),
    # AURKEZPENAK
    re_path(r"^aurkezpenak/", include("gamerauntsia.aurkezpenak.re_paths")),
    # TXAPELKETAK
    re_path(r"^txapelketak/", include("gamerauntsia.txapelketak.re_paths")),
    # MINECRAFT SERVER
    re_path(r"^zerbitzariak/", include("gamerauntsia.zerbitzariak.re_paths")),
    # AGENDA
    re_path(r"^agenda/", include("gamerauntsia.agenda.re_paths")),
    # FOROA
    re_path(r"^foroa/reset-topics$", gamerviews.reset_topics, name="reset_topics"),
    re_path(r"^foroa/", include("django_forum_app.re_paths")),
    # KONTAKTUA
    re_path(r"^kontaktua/$", kontaktuaviews.contact_form, name="kontaktua"),
    # TERMINOLOGIA
    re_path(r"^terminologia/$", baseviews.index, name="terminologia"),
    re_path(r"^terminologia/bilatu", baseviews.search_term, name="search_term"),
    # PODCAST
    re_path(r"^podcastak/", include("gamerauntsia.podcast.re_paths")),
    # BILAKETA
    re_path(r"^bilaketa?(?P<bilatu>[-\w]+)/$", indexviews.bilaketa, name="bilaketa"),
    # RSS FEED
    re_path(r"^feed/gameplayak$", LatestEntriesFeed()),
    re_path(r"^feed/bloga$", LatestNewsFeed()),
    re_path(r"^feed/podcastak/", include("podcasting.re_paths_feeds")),
    # FB
    re_path(r"^2b27b83ad50e677714b2dd832b42acc3", include("facebookpagewriter.re_paths")),
    # COMMENTS
    re_path(r"^comments/", include("django_comments.re_paths")),
    # KUDEATU
    re_path(r"^kudeatu/", admin.site.re_paths),
    re_path(r"^photologue/", include("photologue.re_paths", namespace="photologue")),
    # MEZUAK
    re_path(r"^mezuak/", include("django_messages.re_paths")),
    # EGUTEGIA
    re_path(r"^calendar/", include("django_bootstrap_calendar.re_paths")),
    # TINYMCE
    re_path(r"^tinymce/", include("tinymce.re_paths")),
    # STAR RATINGS
    re_path(r"^ratings/", include("star_ratings.re_paths", namespace="ratings")),
    # APIA
    re_path(r"^api/1.0/", include("gamerauntsia.api.re_paths")),
    # STREAMING
    re_path(r"^streaming/", include("gamerauntsia.streaming.re_paths")),
    # POKEDEX
    re_path(r"^pokedex/", include("gamerauntsia.pokedex.re_paths")),
    # APP
    # Auth
    # re_path(r'^rest-auth/', include('rest_auth.re_paths')),
    # re_path(r'^rest-token-auth/$', obtain_auth_token),
    # # re_path(r'^rest-user/$',views.UserViewSet),
    # re_path(r'^app/v1/', include('gamerauntsia.app.authentication.re_paths')),
    # re_path(r'^app/berriak/$', berria_list, name='app_berria_list'),
    # re_path(r'^app/berria/(?P<pk>[0-9]+)/$', 'gamerauntsia.berriak.views.berria_detail', name='app_berria_detail'),
    # re_path(r'^app/getb/$', 'gamerauntsia.getb.views.app_getb_list', name='app_getb_list'),
    # re_path(r'^app/getb/(?P<pk>[0-9]+)/$', 'gamerauntsia.getb.views.atala_detail', name='atala_detail'),
    # re_path(r'^app/txapelketak/$', 'gamerauntsia.txapelketak.views.txapelketa_list', name='app_txapelketak_list'),
    # re_path(r'^app/txapelketak/(?P<pk>[0-9]+)/$', 'gamerauntsia.txapelketak.views.txapelketa_detail', name='app_txapelketak_detail'),
    # ERABILERA ETA PRIBATUTASUNA
    # re_path(r'^erabilera-baldintzak/$', TemplateView.as_view(template_name='erabilera_baldintzak.html')),
    # re_path(r'^pribatutasun-politika/$', TemplateView.as_view(template_name='pribatutasun_politika.html')),
    # re_path(r'^gameplay-arauak/$', TemplateView.as_view(template_name='upload_gp.html')),
    # re_path(r'^cookie/$', TemplateView.as_view(template_name='cookie.html')),
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
    re_path(r"^ajax/post_finished/", finishedviews.add_finished, name="ajax_finished"),
    # FLATPAGEAK
    re_path(r"^(?P<re_path>.*/)$", views.flatpage),
    # DEBUG
]

if settings.DEBUG:
    import debug_toolbar

    re_pathpatterns = [
        re_path(r"^__debug__/", include(debug_toolbar.re_paths)),
    ] + re_pathpatterns

router.register(r"profile", UsersViewSet)