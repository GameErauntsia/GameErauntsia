from django.db import models
from photologue.models import Photo
from django.utils import timezone

STATUS_TYPES = (
    ("0", "Planned"),
    ("1", "Ongoing"),
    ("2", "Legacy"),
)


class PodcastVideoPlatform(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField(default=0)
    embed_url_pattern = models.CharField(max_length=200, null=True, blank=True)
    link_url_pattern = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Podcast bideo plataforma"
        verbose_name_plural = "Podcast bideo plataformak"

    def __str__(self):
        return "%s" % (self.name)


class PodcastAudioPlatform(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField(default=0)
    link_url_pattern = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Podcast audio paltaforma"
        verbose_name_plural = "Podcast audio plataformak"

    def __str__(self):
        return "%s" % (self.name)


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


class PodcastEpisodeVideoPlatform(models.Model):
    podcast_episode = models.ForeignKey(PodcastEpisode, on_delete=models.CASCADE)
    video_platform = models.ForeignKey(PodcastVideoPlatform, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100, verbose_name="Bideoaren kodea")

    def get_embed_url(self):
        return self.video_platform.embed_url_pattern.replace("{{id}}", self.video_id)

    def get_link_url(self):
        return self.video_platform.link_url_pattern.replace("{{id}}", self.video_id)

    class Meta:
        verbose_name = "Saioaren bideoa"
        verbose_name_plural = "Saioaren bideoak"


class PodcastEpisodeAudioPlatform(models.Model):
    podcast_episode = models.ForeignKey(PodcastEpisode, on_delete=models.CASCADE)
    audio_platform = models.ForeignKey(PodcastAudioPlatform, on_delete=models.CASCADE)
    audio_id = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Audioaren kodea"
    )
    override_link_url = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Audioaren URLa"
    )

    def get_link_url(self):
        if self.override_link_url:
            return self.override_link_url
        else:
            return self.audio_platform.link_url_pattern.replace("{{id}}", self.video_id)

    class Meta:
        verbose_name = "Saioaren audioa"
        verbose_name_plural = "Saioaren audioak"
