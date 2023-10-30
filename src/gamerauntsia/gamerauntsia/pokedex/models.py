from django.db import models
from django.conf import settings


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    izena_ingelesez = models.CharField(max_length=256, verbose_name="Izena ingelesez")
    izena_euskaraz = models.CharField(max_length=256, verbose_name="Izena euskaraz")
    izena_euskaraz_azalpena = models.CharField(
        max_length=256, verbose_name="Euskarazko izenaren azalpen laburra"
    )
    deskribapena = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "Pokemon - %d" % (self.id)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemonak"
