from cssocialuser.models import CSAbstractSocialUser
from django.db import models
from django.contrib.auth.models import UserManager, Group
from django.core.mail import send_mail
from django.conf import settings
from photologue.models import Photo
from gamerauntsia.jokoa.models import Jokoa
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

ARTICLE_KARMA = 10
GP_KARMA = 15
POST_KARMA = 2
COMMENT_KARMA = 1
TOURNAMENT_KARMA = 10
MC_KARMA = 30
PC_KARMA = 5
PROFILE_KARMA = 15
STAFF_KARMA = 20

class GamerUser(CSAbstractSocialUser):
    nickname = models.CharField(max_length=64,null=True,blank=True)
    is_gamer = models.BooleanField(default=False)
    top_jokoak = models.ManyToManyField(Jokoa,null=True,blank=True)
    signature = models.TextField(verbose_name="Foro sinadura",null=True,blank=True)
    ytube_channel = models.CharField(max_length=150,null=True,blank=True)
    email_notification = models.BooleanField(default=True, verbose_name="Eztabaidak")
    buletin_notification = models.BooleanField(default=True, verbose_name="Buletinak")

    #ALTER TABLE `gamer_gameruser` ADD `motherboard` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `processor` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `graphics` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `soundcard` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `ram` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `harddrive` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `harddrive2` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `mouse` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `keyboard` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL , ADD `speakers` VARCHAR(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL ;
    motherboard = models.CharField(verbose_name="Txartel nagusia",max_length=150,null=True,blank=True)
    processor = models.CharField(verbose_name="Prozesagailua",max_length=150,null=True,blank=True)
    graphics = models.CharField(verbose_name="Txartel grafikoa",max_length=150,null=True,blank=True)
    soundcard = models.CharField(verbose_name="Soinu txartela",max_length=150,null=True,blank=True)
    ram = models.CharField(verbose_name="RAM Memoria",max_length=150,null=True,blank=True)
    harddrive = models.CharField(verbose_name="Disko gogorra",max_length=150,null=True,blank=True)
    harddrive2 = models.CharField(verbose_name="Bigarren disko gogorra",max_length=150,null=True,blank=True)
    mouse = models.CharField(verbose_name="Sagua",max_length=150,null=True,blank=True)
    keyboard = models.CharField(verbose_name="Teklatua",max_length=150,null=True,blank=True)
    speakers = models.CharField(verbose_name="Bozgorailuak",max_length=150,null=True,blank=True)

    karma = models.IntegerField(verbose_name="Karma",default=0)

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

    def is_mc_gamer(self):
        from gamerauntsia.zerbitzariak.models import MC_Whitelist
        return MC_Whitelist.objects.filter(user=self).exists()

    def has_mc_platform(self):
        return self.plataforma.filter(plataforma='minecraft').exists()

    def has_platforms(self):
        return self.plataforma.all().exists()

    def has_complete_profile(self):
        if (self.photo and self.photo.slug != MEMBER_PHOTO_SLUG) and self.has_platforms():
            return True
        return False

    def computer_data(self):
        if self.motherboard or self.processor or self.graphics or self.soundcard or self.ram or self.harddrive or self.mouse or self.keyboard or self.speakers:
            return True
        else:
            return False

    def article_count(self):
        return self.berriak.all().count()

    def gp_count(self):
        return self.gameplayak.all().count()

    def post_count(self):
        return self.post_posts.all().count()

    def comment_count(self):
        return self.comment_comments.all().count()

    def tournament_count(self):
        return self.jokalariak.all().count()

    def get_karma(self):
        karma = (self.article_count() * ARTICLE_KARMA) + \
                (self.gp_count() * GP_KARMA) + \
                (self.post_count() * POST_KARMA) + \
                (self.comment_count() * COMMENT_KARMA) + \
                (self.tournament_count() * TOURNAMENT_KARMA) or 0

        #Puntuazio biderkatzailea
        if self.has_complete_profile():
            karma *= PROFILE_KARMA

        #Puntuazio finkoa
        if self.is_mc_gamer():
            karma += MC_KARMA
        if self.computer_data():
            karma += PC_KARMA
        if self.is_staff:
            karma += STAFF_KARMA

        return karma

    def belongs_group(user, group_name):
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            return True
        else:
            return False


    def __unicode__(self):
        return u'%s' % self.username


    class Meta:
        verbose_name = 'GE Erabiltzailea'
        verbose_name_plural = 'GE Erabiltzaileak'


class JokuPlataforma(models.Model):
    plataforma = models.CharField(max_length=10, choices=PLATFORM)
    nick = models.CharField(max_length=64)
    user = models.ForeignKey(GamerUser,related_name='plataforma')

    def __unicode__(self):
        return u'%s - %s' % (self.plataforma,self.nick)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformak'
