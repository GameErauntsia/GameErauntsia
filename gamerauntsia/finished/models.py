from django.db import models
from datetime import datetime
from gamerauntsia.gamer.models import GamerUser


class Finished(models.Model):
    user = models.ForeignKey(
        GamerUser, related_name="finished", on_delete=models.PROTECT
    )
    jokoa = models.CharField(max_length=100, null=True, blank=True)
    fetxa = models.DateTimeField(auto_now_add=True, editable=False)
    nota = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ["fetxa"]

    def __str__(self):
        return self.jokoa + " - " + self.nota
