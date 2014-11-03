from django.db import models
from django.conf import settings
from photologue.models import Photo
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.gameplaya.models import GamePlaya
from datetime import datetime
from django.template import defaultfilters as filters

MOTA = (
    ('0','Kanporaketa'),
    ('1','Liga'),
    ('2','Konbinatua'),
)

MODALITATEA = (
    ('0','Bakarka'),
    ('1','Taldeka'),
)

class Txapelketa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan kategoria honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    mota = models.CharField(max_length=1, choices=MOTA, default='0')
    modalitatea = models.CharField(max_length=1, choices=MODALITATEA, default='0')
    
    jokalariak = models.ManyToManyField(GamerUser,verbose_name="Inskripzioa",null=True,blank=True)
    jokoa = models.ForeignKey(Jokoa)

    publikoa_da = models.BooleanField(default=True) 
    pub_date = models.DateTimeField('Publikazio data', default=datetime.now)
    insk_date = models.DateTimeField('Izen ematea', default=datetime.now)

    def get_desk_txikia(self):
        if len(self.desk) > 150:
            return filters.striptags(self.desk)[:150]+'...'
        return filters.striptags(self.desk)

    class Meta:
        verbose_name = "Txapelketa"
        verbose_name_plural = "Txapelketak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)

class Partaidea(models.Model):  
    izena = models.CharField(max_length=64,null=True,blank=True)
    irudia = models.ForeignKey(Photo,null=True,blank=True)

    txapelketa = models.ForeignKey(Txapelketa)
    jokalariak = models.ManyToManyField(GamerUser)

    win = models.IntegerField('Irabazitakoak', default=0)
    lose = models.IntegerField('Galdutakoak', default=0)
    points = models.IntegerField('Puntuak', default=0)

    def get_izena(self):
        if not self.izena:
            if len(self.jokalariak.all()) == 1:
                return u'%s' % (self.jokalariak.all()[0].username)
            else:
                return u'%s' % (", ".join([p.username for p in self.jokalariak.all()]))
        return u'%s' %(self.izena)

    class Meta:
        verbose_name = "Partaidea"
        verbose_name_plural = "Partaideak"
        
    def __unicode__(self):
        return self.get_izena()

class Partida(models.Model):  
    partaideak = models.ManyToManyField(Partaidea,null=True,blank=True)
    parent_partida = models.ForeignKey("Partida",null=True,blank=True)
    jardunaldia = models.IntegerField('Jardunaldia', default=1)
    emaitza = models.CharField(max_length=50,null=True,blank=True)
    
    txapelketa = models.ForeignKey(Txapelketa)
    gameplaya = models.ForeignKey(GamePlaya,null=True,blank=True)
    date = models.DateTimeField('Data', default=datetime.now)

    def get_izena(self):
        if self.partaideak.all():
            return " VS ".join([p.get_izena() for p in self.partaideak.all()])
        else:
            return u'%d jardunaldia' % (self.jardunaldia)

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidak"
        
    def __unicode__(self):
        return u'%s' % (self.get_izena())