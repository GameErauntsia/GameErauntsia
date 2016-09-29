from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from gamerauntsia.gamer.models import GamerUser
import datetime
from django.utils import timezone
import telebot

class Bazkidea(models.Model):
    user = models.ForeignKey(GamerUser)
    paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    expire_date = models.DateTimeField(default=timezone.localtime(timezone.now().replace(year=timezone.now().year + 1)))

    class Meta:
        verbose_name = "Bazkidea"
        verbose_name_plural = "Bazkideak"

    def __unicode__(self):
        return u'#%d %s' % (self.id, self.user.username)


def send_member_msg(sender,instance,**kwargs):
    if kwargs['created']:
        tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
        message = '[#%s Bazkidea]\n%skudeatu/bazkidetza/bazkidea/%s' % (instance.id, settings.HOST, instance.id)
        tb.send_message(settings.ADMIN_CHAT_ID, message)

post_save.connect(send_member_msg, sender=Bazkidea)
