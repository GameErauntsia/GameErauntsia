from django.db import models
from django.conf import settings
from photologue.models import Photo
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.gamer.models import GamerUser
from datetime import datetime
from gamerauntsia.utils import post_to_twitter
from django.db.models.signals import post_save

class Kategoria(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, help_text="Eremu honetan kategoria honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategoriak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)
	
class Zailtasuna(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, help_text="Eremu honetan zailtasun honen URL helbidea zehazten ari zara.")

    class Meta:    
        verbose_name = "zailtasuna"
        verbose_name_plural = "zailtasunak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)

class GamePlaya(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(unique=True,db_index=True, help_text="Eremu honetan game play honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    iraupena_min = models.IntegerField(max_length=2,default=0)
    iraupena_seg = models.IntegerField(max_length=2, null=False,blank=False,default=0)

    argazkia = models.ForeignKey(Photo)
    bideoa = models.CharField(max_length=100, help_text="Eremu honetan bideoaren URL kodea itsatsi behar duzu. Adb.: c21XAuI3aMo")
    
    jokoa = models.ForeignKey(Jokoa, related_name='gameplay')
    zailtasuna = models.ForeignKey(Zailtasuna, related_name='gameplay')
    kategoria = models.ManyToManyField(Kategoria, related_name='gameplay')
    
    erabiltzailea = models.ForeignKey(GamerUser)
    publikoa_da = models.BooleanField(default=True) 
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)
    
    def get_puntuak(self):
        if self.puntuak == 0:
            return 0
        return round(self.puntuak/self.botoak, .5)

    def get_rating(self):
        return int(self.get_puntuak()*2)
    
    def get_url(self):
        url = ''
        if self.bideoa.startswith('http://vimeo.com'):
            url = self.bideoa.replace('http://vimeo.com/','')
        elif self.bideoa.startswith('http://youtu.be'):
            url = self.bideoa.replace('http://youtu.be/','')
    	return url

    def get_absolute_url(self):
        return '/gameplayak/%s' % self.slug
    
    class Meta:    
        verbose_name = "gameplaya"
        verbose_name_plural = "gameplayak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)
        
#post_save.connect(post_to_twitter, sender=GamePlaya)    
