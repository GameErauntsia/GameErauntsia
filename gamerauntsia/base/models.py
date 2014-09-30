from django.conf import settings
from django.core.mail import send_mail
from django_simple_forum.models import Post
from django.db.models.signals import post_save

MESSAGE = 'Mezu berri bat utzi dute zuk idatzitako gai hauetan: \n\n'

def send_email(sender,instance,**kwargs):
    if kwargs['created']:
        recipient_list = []
        message = MESSAGE
        for forum in instance.topic.forum.all():
        	message += '%sforoa/%s/%s\n\n' % (settings.HOST,forum.slug,instance.topic.id)
        creators = Post.objects.filter(topic=instance.topic).values('creator__email').distinct()
        for creator in creators:
            if not instance.creator.email == creator['creator__email'] and instance.creator.email_notification:
                send_mail('[Game Erauntsia - '+instance.topic.title+']', message, settings.DEFAULT_FROM_EMAIL, [creator['creator__email']])

post_save.connect(send_email, sender=Post)