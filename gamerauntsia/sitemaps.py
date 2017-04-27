from django.conf import settings
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.getb.models import Atala
from gamerauntsia.jokoa.models import Jokoa


class BerriaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Berria.objects.filter(publikoa_da=True)

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse('berria', kwargs={'slug': obj.slug})


class GamePlayaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return GamePlaya.objects.filter(publikoa_da=True)

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse('gameplay', kwargs={'slug': obj.slug})


class TxapelketaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Txapelketa.objects.filter(publikoa_da=True)

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse('txapelketa', kwargs={'slug': obj.slug})


class AtalaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Atala.objects.filter(publikoa_da=True)

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse('getb_atala', kwargs={'slug': obj.slug})


class JokoaSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Jokoa.objects.filter(publikoa_da=True)

    def lastmod(self, obj):
        return obj.mod_date

    def location(self, obj):
        return reverse('game', kwargs={'slug': obj.slug})


sitemaps = {
    'gameplayak': GamePlayaSitemap(),
    'berriak': BerriaSitemap(),
    'txapelketak': TxapelketaSitemap(),
    'atalak': AtalaSitemap(),
    'jokoak': JokoaSitemap()
}
