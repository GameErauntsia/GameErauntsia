from django.db import models
from django.contrib.auth.models import User
from photologue.models import Photo
     
class UserProfile(models.Model):
    url = models.URLField()
    bio = models.TextField(max_length=256)
    irudia = models.ForeignKey(Photo,null=True,blank=True)
    user = models.ForeignKey(User, unique=True)
