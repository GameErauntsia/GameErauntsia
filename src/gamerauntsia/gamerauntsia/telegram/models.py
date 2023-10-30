from django.db import models
from photologue.models import Photo


class TelegramGroup(models.Model):
    izena = models.CharField(max_length=100)
    deskribapena = models.TextField(verbose_name="Deskribapena", null=True, blank=True)
    telegram_kodea = models.CharField(max_length=100)

    photo = models.ForeignKey(Photo, on_delete=models.PROTECT)

    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Telegram taldea"
        verbose_name_plural = "Telegram taldeak"

    def __str__(self):
        return "%s" % self.izena
