from django.db import models
from django.conf import settings
from django.core.mail import send_mail, mail_admins
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from gamerauntsia.utils.social import post_to_twitter
from django_comments.models import Comment
from django.db.models import Count
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya
from django_bootstrap_calendar.models import CalendarEvent
from gamerauntsia.log.models import Log
import telebot

class Terminoa(models.Model):
    term_eu = models.TextField()
    term_es = models.TextField(null=True,blank=True)
    term_en = models.TextField(null=True,blank=True)
    jokoak = models.ManyToManyField(Jokoa, blank=True)
    jokoa = models.ForeignKey(Jokoa, related_name="jokoa")

    class Meta:
        verbose_name = "Terminoa"
        verbose_name_plural = "Terminoak"

    def __unicode__(self):
        return u'%s' % (self.term_eu)


def send_comment_email(sender,instance,**kwargs):
    if kwargs['created']:
        recipient_list = []
        message = 'Iruzkin berri bat utzi dute zuk iruzkindutako '
        messagelog = 'Iruzkin berria egin dute '
        ct = ContentType.objects.get_for_id(instance.content_type.id)
        obj = ct.get_object_for_this_type(pk=instance.object_pk)
        try:
            if obj.__class__.__name__ == 'Berria':
                message += 'artikulu honetan: \n\n%sbloga/%s\n\n' % (settings.HOST,obj.slug)
                messagelog += 'artikulu honetan: \n\n%sbloga/%s\n\n' % (settings.HOST,obj.slug)
            elif obj.__class__.__name__ == 'Txapelketa':
                message += 'txapelketa honetan: \n\n%stxapelketak/%s\n\n' % (settings.HOST,obj.slug)
                messagelog += 'txapelketa honetan: \n\n%stxapelketak/%s\n\n' % (settings.HOST,obj.slug)
            elif obj.__class__.__name__ == 'GamePlaya':
                message += 'gameplay honetan: \n\n%sgameplayak/%s\n\n' % (settings.HOST,obj.slug)
                messagelog += 'gameplay honetan: \n\n%sgameplayak/%s\n\n' % (settings.HOST,obj.slug)
            creators = Comment.objects.filter(object_pk=instance.object_pk,content_type=instance.content_type).values('user__email').distinct()
            l = Log()
            l.mota = 'Iruzkin'
            l.tituloa = "Iruzkin berria"
            l.deskripzioa = messagelog
            l.save()

            for creator in creators:
                if not instance.user.email == creator['user__email'] and instance.user.email_notification:
                    send_mail('[Game Erauntsia - Iruzkin berria]', message, settings.DEFAULT_FROM_EMAIL, [creator['user__email']])
        except:
            send_mail('[Game Erauntsia]', str(instance.id)+' iruzkina ezin izan da bidali!\n\nMezua honako hau zen: "'+message+'"', settings.DEFAULT_FROM_EMAIL, ['ikerib@gmail.com'])

def send_newuser_msg(sender,instance,**kwargs):
    if kwargs['created']:
        try:
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            message = '[Erabiltzailea]\n%skudeatu/gamer/gameruser/%s' % (settings.HOST,instance.id)
            tb.send_message(settings.ADMIN_CHAT_ID, message)
        except:
            pass

def send_article_msg(sender,instance,**kwargs):
    if instance.publikoa_da and instance.status == '0':
        try:
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            message = '[Artikulua]\n%skudeatu/berriak/berria/%s' % (settings.HOST,instance.id)
            tb.send_message(settings.EDITOR_CHAT_ID, message)
        except:
            pass

def send_gp_msg(sender,instance,**kwargs):
    if instance.publikoa_da and instance.status == '0':
        try:
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            message = '[GamePlaya]\n%skudeatu/gameplaya/gameplaya/%s' % (settings.HOST,instance.id)
            tb.send_message(settings.EDITOR_CHAT_ID, message)
        except:
            pass

def send_game_msg(sender,instance,**kwargs):
    if kwargs['created'] and not instance.publikoa_da:
        try:
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            message = '[Jokoa]\n%skudeatu/jokoa/jokoa/%s' % (settings.HOST,instance.id)
            tb.send_message(settings.EDITOR_CHAT_ID, message)
        except:
            pass


def send_agenda_tweet(sender,instance,**kwargs):
    if kwargs['created']:
        post_to_twitter(instance)

post_save.connect(send_comment_email, sender=Comment)
post_save.connect(send_newuser_msg, sender=GamerUser)
post_save.connect(send_article_msg, sender=Berria)
post_save.connect(send_gp_msg, sender=GamePlaya)
post_save.connect(send_game_msg, sender=Jokoa)
post_save.connect(send_agenda_tweet, sender=CalendarEvent)
