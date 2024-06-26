from django.db import models
from django.conf import settings
from datetime import datetime
from gamerauntsia.gamer.models import GamerUser
from django.template import defaultfilters as filters


class Aurkezpena(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=64)
    slug = models.SlugField(
        db_index=True,
        unique=True,
        help_text="Eremu honetan aurkezpen honen URL helbidea zehazten ari zara.",
    )
    abstract = models.TextField(max_length=256, null=True, blank=True)
    slides = models.TextField()

    erabiltzailea = models.ForeignKey(GamerUser, on_delete=models.PROTECT)

    pub_date = models.DateTimeField("publikazio data", default=datetime.now)
    mod_date = models.DateTimeField("modifikazio data", default=datetime.now)

    class Meta:
        verbose_name = "Aurkezpenak"
        verbose_name_plural = "Aurkezpena"

    def __str__(self):
        return "%s" % (self.izena)
