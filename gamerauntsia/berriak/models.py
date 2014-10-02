from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from datetime import datetime
from photologue.models import Photo
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.utils.social import post_social
from django.template import defaultfilters as filters

class Gaia(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan gai honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True)
    irudia = models.ForeignKey(Photo,null=True,blank=True)

    class Meta:
        verbose_name = "Gaia"
        verbose_name_plural = "Gaiak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)

class Berria(models.Model):
    izenburua = models.CharField(max_length=150)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan berri honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)

    gaia = models.ManyToManyField(Gaia)
    
    erabiltzailea = models.ForeignKey(GamerUser)
    argazkia = models.ForeignKey(Photo,null=True,blank=True)

    publikoa_da = models.BooleanField(default=True) 
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)
    shared = models.BooleanField(default=False)

    def get_desk_txikia(self):
    	return filters.striptags(self.desk)[:400]+'...'

    def get_absolute_url(self):
        return '%sberriak/%s' % (settings.HOST, self.slug)

    def getTwitText(self):
        if self.erabiltzailea.twitter_id:
            return self.izenburua + ' ' + self.get_absolute_url() + ' @%s 2dz' % (self.erabiltzailea.twitter_id)
        else:
            return self.izenburua + ' ' + self.get_absolute_url() 
    
    
    class Meta:    
        verbose_name = "berria"
        verbose_name_plural = "berriak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)

post_save.connect(post_social, sender=Berria)
