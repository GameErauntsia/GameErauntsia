from django.db import models
from django_forum_app.models import Category, Forum, Topic, Post

from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.gamer.models import GamerUser


class Log(models.Model):
    tituloa = models.CharField(max_length=100, null=True, blank=True)
    deskripzioa = models.TextField(verbose_name="Deskripzioa", null=True, blank=True)
    mota = models.CharField(max_length=100, null=True, blank=True)
    fetxa = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(GamerUser, related_name='log', on_delete=models.PROTECT)
    berria = models.ForeignKey(Berria, related_name='log', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    gameplaya = models.ForeignKey(GamePlaya, related_name='log', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, related_name='log', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    forum = models.ForeignKey(Forum, related_name='log', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Log'

    def __str__(self):
        return u'%s - %s' % (self.tituloa, self.user)
