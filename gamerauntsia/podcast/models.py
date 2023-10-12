from django.db import models
from photologue.models import Photo
from django.utils import timezone

STATUS_TYPES = (
    ("0", "Planned"),
    ("1", "Ongoing"),
    ("2", "Legacy"),
)


class PodcastShow(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default="0")
    image = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.SET_NULL)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = "Podcasta"
        verbose_name_plural = "Podcastak"


class PodcastSeason(models.Model):
    is_public = models.BooleanField(default=True)
    podcast_show = models.ForeignKey(PodcastShow, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)
    number = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s" % (self.podcast_show, self.name)

    class Meta:
        verbose_name = "Denboraldia"
        verbose_name_plural = "Denboraldiak"


class PodcastEpisode(models.Model):
    is_public = models.BooleanField(default=True)
    podcast_season = models.ForeignKey(PodcastSeason, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField()
    image = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(default=timezone.now)
    number = models.IntegerField(default=0)

    def get_show(self):
        return self.podcast_season.podcast_show

    def get_short_name(self):
        return "%dx%02d %s" % (self.podcast_season.number, self.number, self.name)

    def get_full_name(self):
        return "%s - %s" % (self.get_show().name, self.get_short_name())

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Saioa"
        verbose_name_plural = "Saioak"
