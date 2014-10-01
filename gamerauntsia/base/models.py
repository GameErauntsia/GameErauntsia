from django.conf import settings
from django.core.mail import send_mail
from django_simple_forum.models import Post, Topic
from django.db.models.signals import post_save

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
        message = 'Gai berri bat sortu dute: \n\n%sforoa/%s/%s\n\n' % (settings.HOST,instance.forums.all().order_by('-id')[0].slug,instance.id)
        creator = instance.forums.all().order_by('-id')[0].creator
        creator.email_user(subject='[Game Erauntsia - '+instance.title+']', message=message, from_email=settings.DEFAULT_FROM_EMAIL)


post_save.connect(send_topic_email, sender=Topic)
post_save.connect(send_post_email, sender=Post)