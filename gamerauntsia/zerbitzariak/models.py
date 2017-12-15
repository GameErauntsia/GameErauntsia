from django.db import models
from gamerauntsia.gamer.models import GamerUser

ROL = (
        ('n', 'Normal'),
        ('v', 'VIP'),
        ('a', 'Administrator'),
    )

class MC_Whitelist(models.Model):
    mc_user = models.CharField(max_length=64,verbose_name='MC Erabiltzailea')
    uuid = models.CharField(max_length=64, verbose_name='UUID',null=True,blank=True)
    user = models.ForeignKey(GamerUser,verbose_name='GE Erabiltzailea',null=True,blank=True, on_delete=models.DO_NOTHING)
    rol = models.CharField(max_length=1, default='n',choices=ROL)

    created = models.DateTimeField('Sortze data', auto_now_add=True)

    class Meta:
        verbose_name = "MC Erabiltzailea"
        verbose_name_plural = "MC Erabiltzaileak"
        
    def __unicode__(self):
        return u'%s' % (self.mc_user)
