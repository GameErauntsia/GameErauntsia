from cssocialuser.models import CSAbstractSocialUser
from django.db import models
from django.contrib.auth.models import UserManager
from django.core.mail import send_mail
from django.conf import settings
from photologue.models import Photo
from django.utils.translation import ugettext as _

MEMBER_PHOTO_SLUG=getattr(settings,'PROFILE_PHOTO_DEFAULT_SLUG','no-profile-photo')

PLATFORM = (
    ('steam','Steam'),
    ('origin','Origin'),
    ('lol','League of Legends'),
    ('uplay','Uplay'),
    ('xbox','XBOX'),
    ('ps4','PS4'),
    ('wii','Wii'),
    ('archeage','Archeage'),
    ('wow','World of Warcraft'),
    ('bnet','Battlenet'),
    ('minecraft','Minecraft'),
)

class GamerUser(CSAbstractSocialUser):
    nickname = models.CharField(max_length=64,null=True,blank=True)
    is_gamer = models.BooleanField(default=False)
    #ALTER TABLE `hiribiliuser_hiribiliuser` ADD `signature` LONGTEXT NULL ;
    signature = models.TextField(verbose_name="Foro sinadura")
    ytube_channel = models.CharField(max_length=150,null=True,blank=True)
    email_notification = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now_add=True,editable=False)
    date_joined = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=True)

    objects = UserManager()

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            try:
                return Photo.objects.get(slug=MEMBER_PHOTO_SLUG)    
            except:
                return None 

        
    def get_profile(self):
        return self

    def getFullName(self):
        if self.fullname:
            return self.fullname
        else:
            return self.username

    def getplatforms(self):
        return JokuPlataforma.objects.filter(user=self)  

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __unicode__(self):
        return u'%s' % self.username
  
       
    class Meta:
        verbose_name = 'GE Erabiltzailea'
        verbose_name_plural = 'GE Erabiltzaileak'     


class JokuPlataforma(models.Model):
    plataforma = models.CharField(max_length=10, choices=PLATFORM)
    nick = models.CharField(max_length=64)
    user = models.ForeignKey(GamerUser)

    def __unicode__(self):
        return u'%s - %s' % (self.plataforma,self.nick)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformak'