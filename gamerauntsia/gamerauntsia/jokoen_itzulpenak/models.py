from django.db import models
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from datetime import datetime
from photologue.models import Photo

IPS_STATUS = (
    ('0', 'Erdizka'),
    ('1', 'Probatzeko'),
    ('2', 'Amaituta'),
)

class Itzulpena(models.Model):
    izena = models.CharField(max_length=150, verbose_name="Izena")
    status = models.CharField(max_length=1, choices=IPS_STATUS, default='0',verbose_name="Egoera")
    plataforma = models.ForeignKey(Plataforma)
    jokoa = models.ForeignKey(Jokoa)
    ipsfile = models.FileField(upload_to='ips')

    publikoa_da = models.BooleanField(default=False,verbose_name="Publikoa da")

    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)

    class Meta:
        verbose_name = "Itzulpen fitxategia"
        verbose_name_plural = "Itzulpen fitxategiak"

    def get_absolute_url(self):
        return "%s" % self.ipsfile.url

    def __unicode__(self):
        return u'%s %s' % (self.jokoa.izena, self.jokoa.bertsioa)


class EuskarazkoJokoa(models.Model):
    jokoa = models.ForeignKey(Jokoa)
    plataforma = models.ForeignKey(Plataforma)

    publikoa_da = models.BooleanField(default=False,verbose_name="Publikoa da")
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)

    class Meta:
        verbose_name = "Euskarazko jokoa"
        verbose_name_plural = "Euskarazko jokoak"

    def __unicode__(self):
        return u'%s %s' % (self.jokoa.izena, self.jokoa.bertsioa)


class Euskalinkak(models.Model):
    izena = models.CharField(max_length=150, verbose_name="Izena")
    url = models.URLField()

    irudia = models.ForeignKey(Photo)

    publikoa_da = models.BooleanField(default=False,verbose_name="Publikoa da")
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)

    class Meta:
        verbose_name = "Euskal lotura"
        verbose_name_plural = "Euskal loturak"

    def __unicode__(self):
        return u'%s' % (self.izena)