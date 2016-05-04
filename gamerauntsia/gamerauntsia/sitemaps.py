from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class Sitemaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'hourly'

    def items(self):
        return ['gameplayak', 'berriak', 'txapelketak']

    def location(self, item):
        return reverse(item)
