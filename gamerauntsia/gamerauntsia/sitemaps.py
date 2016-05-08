from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from datetime import datetime


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'dayly'

    def items(self):
        return ['getb_index','berriak_index', 'game_index','gameplay_index','txapelketak_index']


    def location(self, item):
        return reverse(item) 
