from cssocialuser.models import CSAbstractSocialUser
from django.db import models
from django.contrib.auth.models import UserManager
from django.core.mail import send_mail
from django.conf import settings
from photologue.models import Photo
from django.utils.translation import ugettext as _

MEMBER_PHOTO_SLUG=getattr(settings,'PROFILE_PHOTO_DEFAULT_SLUG','no-profile-photo')

class GamerUser(CSAbstractSocialUser):
    nickname = models.CharField(max_length=64,null=True,blank=True)
    is_gamer = models.BooleanField(default=False)
    ytube_channel = models.CharField(max_length=150,null=True,blank=True)
    last_updated = models.DateTimeField(auto_now_add=True,editable=False)
    date_joined = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=True)

    objects = UserManager()

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            try:
                return Photo.objects.get(title_slug=MEMBER_PHOTO_SLUG)    
            except:
                return None 

        
    def get_profile(self):
        return self

    def getFullName(self):
        return self.get_full_name() or self.username  

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