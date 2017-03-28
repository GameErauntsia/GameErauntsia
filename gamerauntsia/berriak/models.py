from django.db import models
from django.conf import settings
from django.utils import timezone
from photologue.models import Photo
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa
from django.template import defaultfilters as filters
from django.template.loader import get_template
from django.template import Context
from gamerauntsia.utils.text import make_responsive

STATUS = (
    ('0', 'Zirriborroa'),
    ('1', 'Publikoa'),
)


class Gaia(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan gai honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256, null=True, blank=True)
    irudia = models.ForeignKey(Photo, null=True, blank=True)

    class Meta:
        verbose_name = "Gaia"
        verbose_name_plural = "Gaiak"

    def __unicode__(self):
        return u'%s' % (self.izena)


class Berria(models.Model):
    izenburua = models.CharField(max_length=150)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan berri honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)

    gaia = models.ManyToManyField(Gaia)

    erabiltzailea = models.ForeignKey(GamerUser, related_name='berriak')
    argazkia = models.ForeignKey(Photo, null=True, blank=True)
    jokoa = models.ForeignKey(Jokoa, null=True, blank=True,
                              help_text="Artikulu honek joko zehaz batekin loturarik badu, adierazi hemen.")

    publikoa_da = models.BooleanField(default=False, verbose_name="Publikatzeko prest")

    status = models.CharField(max_length=1, choices=STATUS, default='0')
    pub_date = models.DateTimeField('publikazio data', default=timezone.now())
    mod_date = models.DateTimeField('modifikazio data', default=timezone.now())
    shared = models.BooleanField(default=False,
                                 help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.")

    def get_title(self):
        return self.izenburua

    def get_desk_txikia(self):
        return filters.striptags(self.desk)[:400] + '...'

    def get_desk_index(self):
        if len(self.desk) > 400:
            return filters.striptags(self.desk)[:400] + '...'
        return filters.striptags(self.desk)

    def get_absolute_url(self):
        return '%sbloga/%s' % (settings.HOST, self.slug)

    def getTwitText(self):
        if self.erabiltzailea.twitter_id:
            return self.izenburua + ' ' + self.get_absolute_url() + ' @%s 2dz' % (self.erabiltzailea.twitter_id)
        else:
            return self.izenburua + ' ' + self.get_absolute_url()

    def getTelegramText(self):
        return self.izenburua + ' ' + self.get_absolute_url()

    def getEmailText(self):
        htmly = get_template('buletina/buletina.html')
        plaintext = get_template('buletina/buletina.txt')
        d = Context(
            {
                'izenburua': self.izenburua,
                'deskribapena': self.get_desk_txikia(),
                'url': self.get_absolute_url(),
                'img_url': settings.HOST + self.argazkia.get_buletin_url()
            }
        )
        subject = settings.EMAIL_SUBJECT + ' ' + self.izenburua
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        return subject, text_content, html_content

    def getFBinfo(self):
        return self.izenburua, self.desk, self.argazkia

    def get_type(self):
        return str(self.__class__.__name__).lower()

    def save(self, *args, **kwargs):
        self.desk = make_responsive(self.desk)
        super(Berria, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "berria"
        verbose_name_plural = "berriak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)
