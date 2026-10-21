import os
from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from gamerauntsia.podcast.models import PodcastEpisode
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.feedgenerator import Rss201rev2Feed


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


class PodcastRssFeed(Rss201rev2Feed):
    def rss_attributes(self):
        attributes = super().rss_attributes()
        attributes["xmlns:itunes"] = "http://www.itunes.com/dtds/podcast-1.0.dtd"
        return attributes

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        if item["image_url"]:
            handler.addQuickElement("itunes:image", "", {"href": item["image_url"]})


class LatestPodcastEpisodesFeed(Feed):
    feed_type = PodcastRssFeed
    title = "Gamerauntsia podcast harpidetza"
    link = "https://gamerauntsia.eus/podcastak/"
    feed_url = "https://gamerauntsia.eus/feed/podcastak"
    description = "Gamerauntsiako podcast saio berriak"
    language = "eu"

    def _force_https(self, url):
        if url.startswith("http://gamerauntsia.eus"):
            return url.replace("http://gamerauntsia.eus", "https://gamerauntsia.eus", 1)
        return url

    def items(self):
        return (
            PodcastEpisode.objects.filter(is_public=True, audio_file__isnull=False)
            .exclude(audio_file="")
            .select_related("image", "podcast_season__podcast_show__image")
            .order_by("-pub_date")[:20]
        )

    def item_extra_kwargs(self, item):
        image = item.image or item.podcast_season.podcast_show.image
        if not image:
            return {"image_url": None}
        return {
            "image_url": "https://%s%s"
            % (Site.objects.get_current().domain, image.image.url)
        }

    def item_title(self, item):
        return item.get_full_name()

    def item_description(self, item):
        return strip_tags(item.description or "")

    def item_pubdate(self, item):
        return item.pub_date

    def item_link(self, item):
        return self._force_https(
            "http://%s%s"
            % (
                Site.objects.get_current().domain,
                reverse(
                    "podcast_episode",
                    kwargs={
                        "show_slug": item.podcast_season.podcast_show.slug,
                        "episode_slug": item.slug,
                    },
                ),
            )
        )

    def item_enclosure_url(self, item):
        return self._force_https(
            "http://%s%s" % (Site.objects.get_current().domain, item.audio_file.url)
        )

    def item_enclosure_length(self, item):
        try:
            if item.audio_file and hasattr(item.audio_file, "path"):
                return os.path.getsize(item.audio_file.path)
        except Exception:
            pass

        try:
            return item.audio_file.size or 0
        except Exception:
            return 0

    def item_enclosure_mime_type(self, item):
        return "audio/mpeg"
