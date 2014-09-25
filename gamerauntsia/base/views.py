from django.conf import settings
from django.core.mail import send_mail
from django_simple_forum.models import Post
from django.db.models.signals import post_save

MESSAGE = 'Mezu berri bat utzi dute zuk idatzitako gai honetan: '

def send_email(sender,instance,**kwargs):
    if kwargs['created']:
        recipient_list = []
        message = MESSAGE + '%s%s%s' % (settings.HOST,instance.topic.forum.slug,instance.topic.id)
        creators = Post.objects.filter(topic=instance.topic).values('creator').distinct()
        for creator in creators:
            recipient_list.append(creator.email)

        send_mail('['+instance.topic.title+']', message, settings.DEFAULT_FROM_EMAIL, recipient_list)

post_save.connect(send_email, sender=Post)



