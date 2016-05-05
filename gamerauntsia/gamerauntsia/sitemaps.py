from django.contrib import sitemaps
from gamerauntsia.berriak.models import Berria


class Sitemaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'hourly'

    def items(self):
        return Berria.objects.filter(status='1', pub_date__lt=datetime.now()).order_by('-pub_date')


    def lastmod(self, obj):
        return obj.pub_date 
