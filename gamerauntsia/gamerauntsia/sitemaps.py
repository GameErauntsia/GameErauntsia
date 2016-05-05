from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class Sitemaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'hourly'

    def items(self):
        return ['gameplay_index', 'bloga', 'jokoak', 'txapelketak_index']

    def location(self, item):
        return reverse(item)
