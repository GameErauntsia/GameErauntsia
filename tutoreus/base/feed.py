from django.contrib.syndication.views import Feed
from tutoreus.berriak.models import Berria

class LatestEntriesFeed(Feed):
    title = "BlenderEUS berriak"
    link = "/azken-berriak/"
    description = "BlenderEUS-en publikatzen diren berriak."

    def items(self):
        return Berria.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.izenburua

    def item_description(self, item):
        return item.desk
        

