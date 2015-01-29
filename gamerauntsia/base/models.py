from django.db import models
from django.conf import settings
from django.core.mail import send_mail, mail_admins
from django_simple_forum.models import Post, Topic
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django_comments.models import Comment
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gameplaya.models import GamePlaya

class Terminoa(models.Model):
    term_eu = models.CharField(max_length=64)
    term_es = models.CharField(max_length=64,null=True,blank=True)
    term_en = models.CharField(max_length=64,null=True,blank=True)

    class Meta:
        verbose_name = "Terminoa"
        verbose_name_plural = "Terminoak"

    def __unicode__(self):
        return u'%s' % (self.term_eu)


def send_post_email(sender,instance,**kwargs):
    if kwargs['created']:
        recipient_list = []
        message = 'Mezu berri bat utzi dute zuk idatzitako gai hauetan: \n\n'
        for forum in instance.topic.forums.all():
        	message += '%sforoa/%s/%s\n\n' % (settings.HOST,forum.slug,instance.topic.id)
        creators = Post.objects.filter(topic=instance.topic).values('creator__email').distinct()
        for creator in creators:
            if not instance.creator.email == creator['creator__email'] and instance.creator.email_notification:
                send_mail('[Game Erauntsia - '+instance.topic.title+']', message, settings.DEFAULT_FROM_EMAIL, [creator['creator__email']])

def send_topic_email(sender,instance,**kwargs):
    if kwargs['created']:
        message = 'Gai berri bat sortu dute: \n\n%skudeatu/django_simple_forum/topic/%s' % (settings.HOST,instance.id)
        for forum in instance.forums.all():
            creator = forum.creator
            creator.email_user(subject='[Game Erauntsia - '+instance.title+']', message=message, from_email=settings.DEFAULT_FROM_EMAIL)

def send_comment_email(sender,instance,**kwargs):
    if kwargs['created']:
        recipient_list = []
        message = 'Iruzkin berri bat utzi dute zuk iruzkindutako artikulu honetan: \n\n'
        ct = ContentType.objects.get_for_id(instance.content_type.id)
        obj = ct.get_object_for_this_type(pk=instance.object_pk)
        if obj.__class__.__name__ == 'Berria':
            message += '%sbloga/%s\n\n' % (settings.HOST,obj.slug)
        elif obj.__class__.__name__ == 'Txapelketa':
            message += '%stxapelketak/%s\n\n' % (settings.HOST,obj.slug)
        else:
            message += '%sgameplayak/%s\n\n' % (settings.HOST,obj.slug)
        creators = Comment.objects.filter(object_pk=instance.object_pk,content_type=instance.content_type).values('user__email').distinct()
        for creator in creators:
            if not instance.user.email == creator['user__email'] and instance.user.email_notification:
                send_mail('[Game Erauntsia - Iruzkin berria]', message, settings.DEFAULT_FROM_EMAIL, [creator['user__email']])

def send_newuser_email(sender,instance,**kwargs):
    if kwargs['created']:
        message = 'Erabiltzaile bat sortu dute: \n\n%skudeatu/gamer/gameruser/%s' % (settings.HOST,instance.id)
        mail_admins(instance.username+' erabiltzailea', message)

def send_article_email(sender,instance,**kwargs):
    if kwargs['created']:
        message = 'Artikulu berri bat sortu dute: \n\n%skudeatu/berriak/berria/%s' % (settings.HOST,instance.id)
        mail_admins(instance.izenburua, message)

def send_gp_email(sender,instance,**kwargs):
    if kwargs['created']:
        message = 'GamePlay berri bat sortu dute: \n\n%skudeatu/gameplaya/gameplaya/%s' % (settings.HOST,instance.id)
        mail_admins(instance.izenburua, message)


post_save.connect(send_topic_email, sender=Topic)
post_save.connect(send_post_email, sender=Post)
post_save.connect(send_comment_email, sender=Comment)
post_save.connect(send_newuser_email, sender=GamerUser)
post_save.connect(send_article_email, sender=Berria)
post_save.connect(send_gp_email, sender=GamePlaya)