from django.db import models
from photologue.models import Photo

SOFTWARE_AUKERAK = (
        ('C', 'Copyright'),
        ('FR', 'Doakoa'),
        ('OS', 'Kode Irekia'),
    )

class Plataforma(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan plataforma honen URL helbidea zehazten ari zara.")
    icon = models.ForeignKey(Photo,null=True,blank=True)
    
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformak"
        
    def __unicode__(self):
        return u'%s' % (self.izena)	

class Jokoa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True, help_text="Eremu honetan joko honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256,null=True,blank=True)
    bertsioa = models.CharField(max_length=64,null=True,blank=True)
    lizentzia = models.CharField(max_length=2, default='C',choices=SOFTWARE_AUKERAK)
    
    logoa = models.ForeignKey(Photo,null=True,blank=True)
    url = models.CharField(max_length=64, help_text="Eremu honetan joko honen atariko URL helbidea zehazten ari zara." )
    wiki = models.CharField(max_length=64, null=True, blank=True, help_text="Eremu honetan joko honen wikipediako URL helbidea zehaztu mesedez." )
      
    def admin_thumbnail(self):
        if self.logoa:
            return u'<img src="%s" />' % self.logoa.get_admin_thumbnail_url()
        else:
            return '(Irudirik ez)'
        admin_thumbnail.short_description = 'Thumb'
        admin_thumbnail.allow_tags = True

    class Meta:
        verbose_name = "Jokoa"
        verbose_name_plural = "Jokoak"
        
    def __unicode__(self):
        return u'%s %s' % (self.izena, self.bertsioa)
