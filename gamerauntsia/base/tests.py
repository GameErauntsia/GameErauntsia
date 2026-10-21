from urllib.parse import urlsplit
from xml.etree import ElementTree

from django.conf import settings
from django.contrib.sites.models import Site
from django.test import TestCase
from photologue.models import Photo

from gamerauntsia.podcast.models import PodcastEpisode, PodcastSeason, PodcastShow


ITUNES_NAMESPACE = "http://www.itunes.com/dtds/podcast-1.0.dtd"


class PodcastFeedImageTests(TestCase):
    def setUp(self):
        Site.objects.update_or_create(
            id=settings.SITE_ID,
            defaults={"domain": "gamerauntsia.eus", "name": "Game Erauntsia"},
        )
        Site.objects.clear_cache()

        show_image = Photo.objects.create(
            title="Programaren irudia",
            slug="programaren-irudia",
            image="photologue/photos/show.jpg",
        )
        episode_image = Photo.objects.create(
            title="Atalaren irudia",
            slug="atalaren-irudia",
            image="photologue/photos/episode.jpg",
        )
        show = PodcastShow.objects.create(
            name="Irudidun podcasta",
            slug="irudidun-podcasta",
            description="Deskribapena",
            image=show_image,
        )
        season = PodcastSeason.objects.create(
            podcast_show=show,
            name="Lehen denboraldia",
            slug="lehen-denboraldia",
            number=1,
        )
        PodcastEpisode.objects.create(
            podcast_season=season,
            name="Irudi propioa",
            slug="irudi-propioa",
            description="Atalaren deskribapena",
            image=episode_image,
            audio_file="podcasts/audio/own.mp3",
            number=1,
        )
        PodcastEpisode.objects.create(
            podcast_season=season,
            name="Programaren irudia",
            slug="programaren-irudia",
            description="Atalaren deskribapena",
            audio_file="podcasts/audio/fallback.mp3",
            number=2,
        )

        show_without_image = PodcastShow.objects.create(
            name="Irudirik gabeko podcasta",
            slug="irudirik-gabeko-podcasta",
            description="Deskribapena",
        )
        season_without_image = PodcastSeason.objects.create(
            podcast_show=show_without_image,
            name="Bigarren denboraldia",
            slug="bigarren-denboraldia",
            number=1,
        )
        PodcastEpisode.objects.create(
            podcast_season=season_without_image,
            name="Irudirik gabe",
            slug="irudirik-gabe",
            description="Atalaren deskribapena",
            audio_file="podcasts/audio/no-image.mp3",
            number=1,
        )

        self.response = self.client.get("/feed/podcastak")
        self.xml = self.response.content
        self.root = ElementTree.fromstring(self.xml)
        self.items = {
            item.findtext("title"): item for item in self.root.findall("channel/item")
        }

    def test_episode_image_takes_precedence(self):
        image = self.items["Irudidun podcasta - 1x01 Irudi propioa"].find(
            f"{{{ITUNES_NAMESPACE}}}image"
        )
        self.assertEqual(
            image.attrib["href"],
            "https://gamerauntsia.eus/media/photologue/photos/episode.jpg",
        )

    def test_show_image_is_used_as_fallback(self):
        image = self.items["Irudidun podcasta - 1x02 Programaren irudia"].find(
            f"{{{ITUNES_NAMESPACE}}}image"
        )
        self.assertEqual(
            image.attrib["href"],
            "https://gamerauntsia.eus/media/photologue/photos/show.jpg",
        )

    def test_image_element_is_omitted_when_no_image_exists(self):
        item = self.items["Irudirik gabeko podcasta - 1x01 Irudirik gabe"]
        self.assertIsNone(item.find(f"{{{ITUNES_NAMESPACE}}}image"))

    def test_image_url_is_absolute_https(self):
        for item in self.items.values():
            image = item.find(f"{{{ITUNES_NAMESPACE}}}image")
            if image is not None:
                parsed_url = urlsplit(image.attrib["href"])
                self.assertEqual(parsed_url.scheme, "https")
                self.assertTrue(parsed_url.netloc)

    def test_itunes_namespace_is_declared(self):
        declaration = f'xmlns:itunes="{ITUNES_NAMESPACE}"'.encode()
        self.assertIn(declaration, self.xml)

    def test_audio_enclosure_is_unchanged(self):
        enclosure = self.items["Irudidun podcasta - 1x01 Irudi propioa"].find(
            "enclosure"
        )
        self.assertEqual(
            enclosure.attrib,
            {
                "length": "0",
                "type": "audio/mpeg",
                "url": "https://gamerauntsia.eus/media/podcasts/audio/own.mp3",
            },
        )

    def test_feed_is_valid_xml(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.root.tag, "rss")
