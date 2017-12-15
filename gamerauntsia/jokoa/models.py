from django.db import models
from django.conf import settings
from photologue.models import Photo
from django.utils import timezone

SOFTWARE_AUKERAK = (
        ('C', 'Copyright'),
        ('FR', 'Doakoa'),
        ('OS', 'Kode Irekia'),
    )

class Plataforma(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan plataforma honen URL helbidea zehazten ari zara.")
    icon = models.ForeignKey(Photo,null=True,blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformak"

    def __unicode__(self):
        return u'%s' % (self.izena)

class Jokoa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan joko honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True, verbose_name="Deskribapena")
    bertsioa = models.CharField(max_length=64,null=True,blank=True,help_text="Joko saga bat bada, zehaztu hemen bertsioa.")
    lizentzia = models.CharField(max_length=2, default='C',choices=SOFTWARE_AUKERAK)

    logoa = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)
    steam_id = models.IntegerField(null=True,blank=True, help_text="Jokoa Steam plataforman aurki badaiteke, jokoaren fitxaren URLan agertzen den zenbakia. Adibidez: 236110")
    trailer = models.CharField(max_length=64,null=True,blank=True, verbose_name="Youtube trailerra",help_text="Steam ID zenbakia jarrita badago, ez da beharrezkoa. Bestela, Youtube bideoaren KODEA itsatsi. Adibidez: bkgzXpKbVGE")
    url = models.CharField(max_length=64, help_text="Eremu honetan joko honen atariko URL helbidea zehazten ari zara." )
    wiki = models.CharField(max_length=64, null=True, blank=True, help_text="Eremu honetan joko honen wikipediako URL helbidea zehaztu mesedez." )

    publikoa_da = models.BooleanField(default=False)
    mod_date = models.DateTimeField('modifikazio data', default=timezone.now)

    def get_title(self):
        return "%s %s" % (self.izena,self.bertsioa)

    def get_absolute_url(self):
        return "%sjokoak/%s" % (settings.HOST,self.slug)


    def get_photo(self):
        if self.logoa:
            return self.logoa
        else:
            return None

    class Meta:
        verbose_name = "Jokoa"
        verbose_name_plural = "Jokoak"

    def __unicode__(self):
        return u'%s %s' % (self.izena, self.bertsioa)
