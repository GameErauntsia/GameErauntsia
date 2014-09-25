from django.db import models
from gamerauntsia.gameplaya.models import *
from gamerauntsia.jokoa.models import *

class AutoGamePlaya(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(unique=True,db_index=True, help_text="Eremu honetan game play honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    iraupena_min = models.IntegerField(max_length=2, default=0)
    iraupena_seg = models.IntegerField(max_length=2, default=0)

    argazkia = models.ForeignKey(Photo)
    bideoa = models.CharField(max_length=100, help_text="Eremu honetan bideoaren URL kodea itsatsi behar duzu. Adb.: c21XAuI3aMo")
    
    jokoa = models.ForeignKey(Jokoa, related_name='autogameplay', null=False,blank=False)
    plataforma = models.ForeignKey(Plataforma, related_name='autogameplay', null=False,blank=False)
    zailtasuna = models.ForeignKey(Zailtasuna, related_name='autogameplay', null=False,blank=False)
    kategoria = models.ManyToManyField(Kategoria, related_name='autogameplay', null=False,blank=False)
    
    erabiltzailea = models.ForeignKey(GamerUser)

    class Meta:    
        verbose_name = "Auto gameplaya"
        verbose_name_plural = "Auto gameplayak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)