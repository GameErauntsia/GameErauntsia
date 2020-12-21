from django.db import models
from gamerauntsia.gamer.models import GamerUser
from django.utils import timezone

class Streaming(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(GamerUser, related_name='streamingak', on_delete=models.PROTECT)
    start_date = models.DateTimeField('Hasiera data/ordua', default=timezone.now)
    end_date = models.DateTimeField('Amaiera data/ordua', default=None)
    twitch_id= models.CharField(max_length=50)

    class Meta:
        verbose_name = "Streaming"
        verbose_name_plural = "Streamingak"
