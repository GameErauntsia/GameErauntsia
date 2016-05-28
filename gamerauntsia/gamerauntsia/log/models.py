from django.db import models
from django_simple_forum.models import Category, Forum, Topic, Post

from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.gamer.models import GamerUser


class Log(models.Model):
    tituloa = models.CharField(max_length=100, null=True, blank=True)
    deskripzioa = models.TextField(verbose_name="Deskripzioa", null=True, blank=True)
    mota = models.CharField(max_length=100, null=True, blank=True)
    fetxa = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(GamerUser, related_name='log')
    berria = models.ForeignKey(Berria, related_name='log', null=True, blank=True, default=None)
    gameplaya = models.ForeignKey(GamePlaya, related_name='log', null=True, blank=True, default=None)
    post = models.ForeignKey(Post, related_name='log', null=True, blank=True, default=None)
    forum = models.ForeignKey(Forum, related_name='log', null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Log'

    def __unicode__(self):
        return u'%s - %s' % (self.tituloa, self.user)
