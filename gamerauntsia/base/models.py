from django.conf import settings
from django.core.mail import send_mail
from django_simple_forum.models import Post, Topic
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment

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
        ct = ContentType.objects.get_for_id(instance.content_type)
        obj = ct.get_object_for_this_type(pk=instance.object_pk)
        if obj.__class__.__name__ == 'Berria':
            message += '%sbloga/%s\n\n' % (settings.HOST,obj.slug)
        else:
            message += '%sgameplayak/%s\n\n' % (settings.HOST,obj.slug)
        creators = Comment.objects.filter(object_pk=instance.object_pk,content_type=instance.content_type).values('user__email').distinct()
        for creator in creators:
            if not instance.user.email == creator['creator__email'] and instance.user.email_notification:
                send_mail('[Game Erauntsia - Iruzkin berria]', message, settings.DEFAULT_FROM_EMAIL, [creator['user__email']])


post_save.connect(send_topic_email, sender=Topic)
post_save.connect(send_post_email, sender=Post)
post_save.connect(send_comment_email, sender=Comment)