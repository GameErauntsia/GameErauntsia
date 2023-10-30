from django.contrib.syndication.views import Feed
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from django.utils import timezone


class LatestEntriesFeed(Feed):
    title = "Gamerauntsia harpidetza"
    link = "/gameplayak/"
    description = "Gamerauntsian argitaratzen diren gameplayak"

    def items(self):
        return GamePlaya.objects.filter(
            status="1", publikoa_da=True, pub_date__lt=timezone.now()
        ).order_by("-pub_date")[:20]

    def item_title(self, item):
        return item.izenburua

    def item_description(self, item):
        return item.desk


class LatestNewsFeed(Feed):
    title = "Gamerauntsia berrien harpidetza"
    link = "/berriak/"
    description = "Gamerauntsian argitaratzen diren berriak"

    def items(self):
        return Berria.objects.filter(status="1", pub_date__lt=timezone.now()).order_by(
            "-pub_date"
        )[:20]

    def item_title(self, item):
        return item.izenburua

    def item_description(self, item):
        return item.get_desk_txikia()
