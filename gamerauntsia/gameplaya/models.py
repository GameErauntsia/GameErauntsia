from django.db import models
from django.contrib.auth.models import User

from photologue.models import Photo
from gamerauntsia.jokoa.models import Jokoa
from datetime import datetime
from gamerauntsia.utils import post_to_twitter
from django.db.models.signals import post_save

class Gaia(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, help_text="Eremu honetan gai honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    
    class Meta:
        verbose_name = "gaia"
        verbose_name_plural = "gaiak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)
	
class Zailtasuna(models.Model):
    izena = models.CharField(max_length=64)
	
    class Meta:    
        verbose_name = "zailtasuna"
        verbose_name_plural = "zailtasunak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)

class GamePlaya(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, help_text="Eremu honetan tutorial honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    iraupena_min = models.IntegerField(max_length=2,default=0)
    iraupena_seg = models.IntegerField(max_length=2, null=False,blank=False,default=0)
    botoak = models.IntegerField(default=0)
    puntuak = models.FloatField(default=0)

    argazkia = models.ForeignKey(Photo,null=True,blank=True)
    bideoa = models.CharField(max_length=100,null=True,blank=True, help_text="Eremu honetan bideoaren URL kodea itsatsi behar duzu. Adb.: 41669968")
    
    jokoa = models.ForeignKey(Jokoa)
    zailtasuna = models.ForeignKey(Zailtasuna)
    gaia = models.ManyToManyField(Gaia)
    
    erabiltzailea = models.ForeignKey(User)
    publikoa_da = models.BooleanField() 
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
    
    class Meta:    
        verbose_name = "gameplaya"
        verbose_name_plural = "gameplayak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)
        
#post_save.connect(post_to_twitter, sender=GamePlaya)    
