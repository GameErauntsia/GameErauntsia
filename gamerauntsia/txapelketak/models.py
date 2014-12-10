from django.db import models
from django.conf import settings
from photologue.models import Photo
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.gameplaya.models import GamePlaya
from datetime import datetime
from django.template import defaultfilters as filters
from mptt.models import MPTTModel, TreeForeignKey

MOTA = (
    ('0','Kanporaketa'),
    ('1','Liga'),
    ('2','Konbinatua'),
)

MODALITATEA = (
    ('0','Bakarka'),
    ('1','Taldeka'),
)

EGOERA = (
    ('0','Izen ematea'),
    ('1','Partidak sortzen'),
    ('2','Txapelketa jokuan'),
    ('3','Bukatuta'),
)

class Txapelketa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan kategoria honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True)
    arauak = models.TextField(max_length=256,null=True,blank=True)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    mota = models.CharField(max_length=1, choices=MOTA, default='0')
    modalitatea = models.CharField(max_length=1, choices=MODALITATEA, default='0')
    status = models.CharField(max_length=1, choices=EGOERA, default='0')

    jokalariak = models.ManyToManyField(GamerUser,related_name="jokalariak",verbose_name="Inskripzioa",null=True,blank=True)
    irabazlea = models.ForeignKey(GamerUser,related_name="irabazlea",verbose_name="Irabazlea")

    jokoa = models.ForeignKey(Jokoa)
    erabiltzailea = models.ForeignKey(GamerUser,related_name="erabiltzailea",verbose_name="Egilea")

    publikoa_da = models.BooleanField(default=True) 
    pub_date = models.DateTimeField('Publikazio data', default=datetime.now)
    insk_date = models.DateTimeField('Izen ematea', default=datetime.now)

    def get_partaideak(self,order=None):
        if order:
            return Partaidea.objects.filter(txapelketa=self).order_by(order)
        return Partaidea.objects.filter(txapelketa=self)

    def partaideak_count(self):
        return get_partaideak().count()

    def get_partidak(self):
        return Partida.objects.filter(txapelketa=self).order_by('date')

    def get_desk_txikia(self):
        if len(self.desk) > 150:
            return filters.striptags(self.desk)[:150]+'...'
        return filters.striptags(self.desk)

    def get_absolute_url(self):
        return '%stxapelketak/%s' % (settings.HOST, self.slug)

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

    def is_group(self):
        if len(self.jokalariak.all()) > 1:
            return True
        return False

    def get_photo(self):
        if self.is_group():
            if self.irudia:
                return self.irudia
            else:
                try:
                    return Photo.objects.get(slug=GROUP_PHOTO_SLUG)    
                except:
                    return None
        else:
            return self.jokalariak.all()[0].get_photo()

    def get_izena(self):
        if not self.izena:
            if len(self.jokalariak.all()) == 1:
                return u'%s' % (self.jokalariak.all()[0].getFullName())
            else:
                return u'%s' % (", ".join([p.getFullName() for p in self.jokalariak.all()]))
        return u'%s' %(self.izena)

    class Meta:
        verbose_name = "Partaidea"
        verbose_name_plural = "Partaideak"
        
    def __unicode__(self):
        return self.get_izena()

class Partida(MPTTModel):  
    partaideak = models.ManyToManyField(Partaidea,null=True,blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
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

    def get_partaide_list(self):
        if self.partaideak.all():
            return " VS ".join([p.get_izena() for p in self.partaideak.all()])
        else:
            return u'???'

    class MPTTMeta:
        order_insertion_by = ['jardunaldia']

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidak"
        
    def __unicode__(self):
        return u'%s' % (self.get_izena())