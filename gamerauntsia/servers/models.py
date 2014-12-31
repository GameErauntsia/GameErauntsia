from django.db import models
from gamerauntsia.gamer.models import GamerUser

ROL = (
        ('n', 'Normal'),
        ('v', 'VIP')
        ('a', 'Administrator'),
    )

class MC_Whitelist(models.Model):
    mc_user = models.CharField(max_length=64)
    user = models.ForeignKey(GamerUser,null=True,blank=True)
    rol = models.CharField(max_length=1, default='n',choices=ROL)

    class Meta:
        verbose_name = "MC Erabiltzailea"
        verbose_name_plural = "MC Erabiltzaileak"
        
    def __unicode__(self):
        return u'%s' % (self.mc_user)