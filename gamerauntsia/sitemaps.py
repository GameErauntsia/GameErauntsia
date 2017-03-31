from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.txapelketak.models import Txapelketa
from gamerauntsia.getb.models import Atala
from gamerauntsia.jokoa.models import Jokoa


berria_sitemap = {
    'queryset': Berria.objects.filter(is_public=True),
    'date_field': 'mod_date',
}

gameplaya_sitemap = {
    'queryset': GamePlaya.objects.filter(is_public=True),
    'date_field': 'mod_date',
}

txapelketa_sitemap = {
    'queryset': Txapelketa.objects.filter(is_public=True),
    'date_field': 'mod_date',
}

atala_sitemap = {
    'queryset': Atala.objects.filter(is_public=True),
    'date_field': 'mod_date',
}

jokoa_sitemap = {
    'queryset': Jokoa.objects.filter(is_public=True),
    'date_field': 'mod_date',
}


sitemaps = {
    'gameplayak': GenericSitemap(gameplaya_sitemap, priority=0.6),
    'berriak': GenericSitemap(berria_sitemap, priority=0.6),
    'txapelketak': GenericSitemap(txapelketa_sitemap, priority=0.6),
    'atalak': GenericSitemap(atala_sitemap, priority=0.6),
    'jokoak': GenericSitemap(jokoa_sitemap, priority=0.6)
}
