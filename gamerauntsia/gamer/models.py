from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import UserManager, Group
from django.core.mail import send_mail
from django.db import models
from photologue.models import Photo
from django.contrib.auth.validators import UnicodeUsernameValidator
from gamerauntsia.jokoa.models import Jokoa


MEMBER_PHOTO_SLUG = getattr(settings, 'PROFILE_PHOTO_DEFAULT_SLUG', 'no-profile-photo')
DEFAULT_PHOTO = Photo.objects.get(slug=MEMBER_PHOTO_SLUG)
PLATFORM = (
    ('steam', 'Steam'),
    ('origin', 'Origin'),
    ('lol', 'League of Legends'),
    ('uplay', 'Uplay'),
    ('xbox', 'XBOX'),
    ('ps4', 'PS4'),
    ('wii', 'Wii'),
    ('archeage', 'Archeage'),
    ('wow', 'World of Warcraft'),
    ('bnet', 'Battlenet'),
    ('minecraft', 'Minecraft'),
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


class GamerUser(AbstractUser):
    nickname = models.CharField(max_length=64, null=True, blank=True)
    telegram_id = models.IntegerField(verbose_name="Telegram kodea", null=True, blank=True)
    is_gamer = models.BooleanField(default=False)
    top_jokoak = models.ManyToManyField(Jokoa, blank=True)
    signature = models.TextField(verbose_name="Foro sinadura", null=True, blank=True)
    devices = models.TextField(verbose_name="Mugikor gailuaen IDak", null=True, blank=True)
    ytube_channel = models.CharField(max_length=150, null=True, blank=True)
    twitch_channel = models.CharField(max_length=150, null=True, blank=True, verbose_name="Twitch kanala")
    email_notification = models.BooleanField(default=True, verbose_name="Eztabaidak")
    buletin_notification = models.BooleanField(default=True, verbose_name="Buletinak")
    motherboard = models.CharField(verbose_name="Txartel nagusia", max_length=150, null=True, blank=True)
    processor = models.CharField(verbose_name="Prozesagailua", max_length=150, null=True, blank=True)
    graphics = models.CharField(verbose_name="Txartel grafikoa", max_length=150, null=True, blank=True)
    soundcard = models.CharField(verbose_name="Soinu txartela", max_length=150, null=True, blank=True)
    ram = models.CharField(verbose_name="RAM Memoria", max_length=150, null=True, blank=True)
    harddrive = models.CharField(verbose_name="Disko gogorra", max_length=150, null=True, blank=True)
    harddrive2 = models.CharField(verbose_name="Bigarren disko gogorra", max_length=150, null=True, blank=True)
    mouse = models.CharField(verbose_name="Sagua", max_length=150, null=True, blank=True)
    keyboard = models.CharField(verbose_name="Teklatua", max_length=150, null=True, blank=True)
    speakers = models.CharField(verbose_name="Bozgorailuak", max_length=150, null=True, blank=True)

    karma = models.IntegerField(verbose_name="Karma", default=0)

    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField('Telefonoa', max_length=25, blank=True, null=True)

    fullname = models.CharField('Izen abizenak', max_length=200, blank=True,null=True)
    bio = models.TextField('Biografia', null=True,blank=True)
    photo = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.SET_NULL)

    twitter_id = models.CharField(max_length=100, blank=True,null=True)
    facebook_id = models.CharField(max_length=100, blank=True,null=True)
    openid_id = models.CharField(max_length=100, blank=True,null=True)
    googleplus_id = models.CharField(max_length=100, blank=True,null=True)

    last_updated = models.DateTimeField(auto_now_add=True, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            try:
                return DEFAULT_PHOTO
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

    def getamaitutakoak(self):
        return AmaitutakoJokoak.objects.filter(user=self)

    def likes_game(self, game):
        if game in self.top_jokoak.all():
            return True
        return False

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def get_bazkidea(self):
        from gamerauntsia.bazkidetza.models import Bazkidea
        try:
            return Bazkidea.objects.get(user=self, is_active=True)
        except:
            return None

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

    def article_count(self,from_date):
        return self.berriak.filter(status='1',pub_date__gte=from_date).count()

    def gp_count(self,from_date):
        return self.gameplayak.filter(status='1',pub_date__gte=from_date).count()

    def post_count(self,from_date):
        return self.post_posts.filter(created__gte=from_date).count()

    def comment_count(self,from_date):
        return self.comment_comments.filter(is_public=True,submit_date__gte=from_date).count()

    def tournament_count(self,from_date):
        return self.jokalariak.filter(publikoa_da=True, pub_date__gte=from_date).count()

    def get_karma(self,days):
        from_date = datetime.now() + timedelta(-days)
        karma = (self.article_count(from_date) * ARTICLE_KARMA) + \
                (self.gp_count(from_date) * GP_KARMA) + \
                (self.post_count(from_date) * POST_KARMA) + \
                (self.comment_count(from_date) * COMMENT_KARMA) + \
                (self.tournament_count(from_date) * TOURNAMENT_KARMA) or 0

        # Puntuazio biderkatzailea
        if self.has_complete_profile():
            karma *= PROFILE_KARMA

        # Puntuazio finkoa
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

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.fullname

    def get_fullname(self):
        if self.fullname:
            return self.fullname
        else:
            return u'%s' % (self.get_full_name()) or self.username

    def get_absolute_url(self):
        return "/komunitatea/%s" % (self.username)

    def __str__(self):
        return u'%s' % self.username

    class Meta:
        verbose_name = 'GE Erabiltzailea'
        verbose_name_plural = 'GE Erabiltzaileak'


class JokuPlataforma(models.Model):
    plataforma = models.CharField(max_length=10, choices=PLATFORM)
    nick = models.CharField(max_length=64)
    user = models.ForeignKey(GamerUser, related_name='plataforma', on_delete=models.PROTECT)

    def __str__(self):
        return u'%s - %s' % (self.plataforma, self.nick)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformak'


class AmaitutakoJokoak(models.Model):
    izenburua = models.CharField(max_length=150)
    urtea = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(GamerUser, related_name='amaitutakoak', on_delete=models.PROTECT)
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)

    def __str__(self):
        return u'%s' % (self.izenburua)

    class Meta:
        verbose_name = 'Amaiatutakoak'
        verbose_name_plural = 'Amaiatutakoak'
