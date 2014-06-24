from django.db import models
from django.contrib.auth.models import User
from photologue.models import Photo

class Base(models.Model):
    izenburua = models.CharField(max_length=64)
    azpi_izenburua = models.CharField(max_length=64)
    desk = models.TextField(max_length=256)
    
    class Meta:    
        verbose_name = "basea"
        verbose_name_plural = "basea"

    def __unicode__(self):
        return u'%s' % (self.izenburua)
     
class UserProfile(models.Model):
    url = models.URLField()
    bio = models.TextField(max_length=256)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    user = models.ForeignKey(User, unique=True)
