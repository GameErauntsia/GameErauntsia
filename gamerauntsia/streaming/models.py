from django.db import models
from gamerauntsia.gamer.models import GamerUser
from django.utils import timezone


class Streaming(models.Model):
    title = models.CharField(max_length=200, verbose_name="Izenburua")
    user = models.ForeignKey(
        GamerUser,
        verbose_name="Erabiltzailea",
        related_name="streamingak",
        on_delete=models.PROTECT,
    )
    start_date = models.DateTimeField("Hasiera data/ordua", default=timezone.now)
    end_date = models.DateTimeField("Amaiera data/ordua", default=None, null=True)
    twitch_id = models.CharField(max_length=50, null=True, unique=True)
    game_name = models.CharField(max_length=100, verbose_name="Jokoa", null=True)

    def __str__(self):
        return self.twitch_id

    class Meta:
        verbose_name = "Streaming"
        verbose_name_plural = "Streamingak"
