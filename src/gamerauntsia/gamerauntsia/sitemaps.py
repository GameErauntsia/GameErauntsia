from django.conf import settings
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.getb.models import Atala
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.joko_itzulpenak.models import ItzulpenProiektua


class BerriaSitemap(Sitemap):
    protocol = "https"
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Berria.objects.filter(publikoa_da=True).order_by("-pub_date")

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse("berria", kwargs={"slug": obj.slug})


class GamePlayaSitemap(Sitemap):
    protocol = "https"
    changefreq = "never"
    priority = 0.5

    def items(self):
        return GamePlaya.objects.filter(publikoa_da=True).order_by("-pub_date")

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse("gameplay", kwargs={"slug": obj.slug})


class TxapelketaSitemap(Sitemap):
    protocol = "https"
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Txapelketa.objects.filter(publikoa_da=True).order_by("-pub_date")

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse("txapelketa", kwargs={"slug": obj.slug})


class AtalaSitemap(Sitemap):
    protocol = "https"
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Atala.objects.filter(publikoa_da=True).order_by("-pub_date")

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse("getb_atala", kwargs={"slug": obj.slug})


class JokoaSitemap(Sitemap):
    protocol = "https"
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Jokoa.objects.filter(publikoa_da=True).order_by("-mod_date")

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse("game", kwargs={"slug": obj.slug})


class ItzulpenProiektuaSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ItzulpenProiektua.objects.filter(publikoa_da=True).order_by(
            "-eguneratze_data"
        )

    def lastmod(self, obj):
        return obj.eguneratze_data

    def location(self, obj):
        return reverse("itzulpen_proiektua", kwargs={"slug": obj.slug})


class EstatikoakSitemap(Sitemap):
    protocol = "https"
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return [
            "euskarazko_jokoak",
            "talde_motorra",
            "minecraft_index",
            "berriak_index",
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {
    "gameplayak": GamePlayaSitemap(),
    "berriak": BerriaSitemap(),
    "txapelketak": TxapelketaSitemap(),
    "jokoak": JokoaSitemap(),
    "estatikoak": EstatikoakSitemap(),
    "flatpages": FlatPageSitemap(),
    "itzulpen_proiektuak": ItzulpenProiektuaSitemap(),
}
