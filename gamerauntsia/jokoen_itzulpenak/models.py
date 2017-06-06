from django.db import models
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from datetime import datetime
from photologue.models import Photo
from django.utils.html import mark_safe

IPS_STATUS = (
    ('0', 'Erdizka'),
    ('1', 'Probatzeko'),
    ('2', 'Amaituta'),
)

class Itzulpena(models.Model):
    izena = models.CharField(max_length=150, verbose_name="Fitxategi izena")
    status = models.CharField(max_length=1, choices=IPS_STATUS, default='0',verbose_name="Egoera")
    ipsfile = models.FileField(upload_to='ips')
    instalazioa = models.TextField(blank=True)
    publikoa_da = models.BooleanField(default=False,verbose_name="Publikoa da")

    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)

    class Meta:
        verbose_name = "Itzulpen fitxategia"
        verbose_name_plural = "Itzulpen fitxategiak"

    def get_absolute_url(self):
        return "%s" % self.ipsfile.url

    def __unicode__(self):
        return u'%s' % (self.izena)


class EuskarazkoJokoa(models.Model):
    jokoa = models.ForeignKey(Jokoa)
    plataformak = models.ManyToManyField(Plataforma)

    itzulpena = models.ForeignKey(Itzulpena, blank=True, null=True)
    garatzaileak_itzulia = models.BooleanField(default=False, verbose_name="Garatzaileak itzulia")
    online_url = models.URLField(blank=True, verbose_name="Online itzulpen proiektua")

    publikoa_da = models.BooleanField(default=False,verbose_name="Publikoa da")
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)

    class Meta:
        verbose_name = "Euskarazko jokoa"
        verbose_name_plural = "Euskarazko jokoak"

    def __unicode__(self):
        return u'%s %s' % (self.jokoa.izena, self.jokoa.bertsioa)

    def is_ge_translation(self):
        return self.itzulpena and True or False
    is_ge_translation.boolean = True

    def is_ge_translation_icon(self):
        return self.is_ge_translation() and mark_safe('<i class="glyphicon glyphicon-file"></i> Fitxategia %s' % self.itzulpena.get_status_display().lower()) or ''


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
