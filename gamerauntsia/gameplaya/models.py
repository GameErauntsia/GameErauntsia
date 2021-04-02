from django.db import models
from django.conf import settings
from photologue.models import Photo
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from gamerauntsia.gamer.models import GamerUser
from django.utils import timezone
from django.template import defaultfilters as filters
from django.template.loader import get_template
from django.template import Context
from django.template.defaultfilters import truncatechars

STATUS = (
    ('0', 'Zirriborroa'),
    ('1', 'Publikoa'),
)


class Kategoria(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan kategoria honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256, null=True, blank=True)
    irudia = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategoriak"

    def __str__(self):
        return u'%s' % (self.izena)


class Zailtasuna(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan zailtasun honen URL helbidea zehazten ari zara.")

    class Meta:
        verbose_name = "Zailtasuna"
        verbose_name_plural = "Zailtasunak"

    def __str__(self):
        return u'%s' % (self.izena)

class BideoPlataforma(models.Model):
    izena = models.CharField(max_length=64)
    embed_url = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Bideo plataforma"
        verbose_name_plural = "Bideo plataformak"
    def __str__(self):
        return u"%s" % (self.izena)

class GamePlaya(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, db_index=True,
                            help_text="Eremu honetan game play honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    iraupena_min = models.IntegerField(default=0)
    iraupena_seg = models.IntegerField(null=False, blank=False, default=0)

    argazkia = models.ForeignKey(Photo, on_delete=models.PROTECT)
    bideoa = models.CharField(max_length=100, null=True, blank=True,
                              verbose_name="Bideoaren URL kodea",
                              help_text="Bideoaren URL kodea. Youtube adb.: c21XAuI3aMo Peertube adb.: 544349f5-c7b3-4b31-92cb-a06c96eadfb6")

    jokoa = models.ForeignKey(Jokoa, related_name='gameplay', on_delete=models.PROTECT)
    plataforma = models.ForeignKey(Plataforma, related_name='gameplay', on_delete=models.PROTECT)
    zailtasuna = models.ForeignKey(Zailtasuna, related_name='gameplay', on_delete=models.PROTECT)
    kategoria = models.ManyToManyField(Kategoria, related_name='gameplay')

    erabiltzailea = models.ForeignKey(GamerUser, related_name='gameplayak', on_delete=models.PROTECT)
    publikoa_da = models.BooleanField(default=False, verbose_name="Publikatzeko prest")
    pub_date = models.DateTimeField('publikazio data', default=timezone.now)
    mod_date = models.DateTimeField('modifikazio data', default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS, default='0')
    shared = models.BooleanField(default=False,
                                 help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.")
    bideo_plataforma = models.ForeignKey(BideoPlataforma, on_delete=models.PROTECT, null=True, verbose_name="Bideo plataforma")

    def get_title(self):
        return self.izenburua

    def get_desk_index(self):
        if len(self.desk) > 400:
            return filters.striptags(self.desk)[:400] + '...'
        return filters.striptags(self.desk)

    def get_desk_txikia(self):
        if len(self.desk) > 150:
            return filters.striptags(self.desk)[:150] + '...'
        return filters.striptags(self.desk)

    def get_type(self):
        return str(self.__class__.__name__).lower()

    def get_puntuak(self):
        if self.puntuak == 0:
            return 0
        return round(self.puntuak / self.botoak, .5)

    def get_rating(self):
        return int(self.get_puntuak() * 2)

    def get_bideo_url(self):
        if self.bideo_plataforma:
            return self.bideo_plataforma.embed_url.replace("{{id}}", self.bideoa)
        else:
            return u"https://www.youtube.com/embed/%s" % (self.bideoa)

    def get_url(self):
        url = ''
        if self.bideoa.startswith('http://vimeo.com'):
            url = self.bideoa.replace('http://vimeo.com/', '')
        elif self.bideoa.startswith('http://youtu.be'):
            url = self.bideoa.replace('http://youtu.be/', '')
        return url

    def get_absolute_url(self):
        return '%sgameplayak/%s' % (settings.HOST, self.slug)

    def getTwitText(self):
        if self.erabiltzailea.twitter_id:
            return truncatechars(self.izenburua, 60) + ' @%s 2dz ' % (self.erabiltzailea.twitter_id) +  self.get_absolute_url()
        else:
            return truncatechars(self.izenburua, 100) + ' ' + self.get_absolute_url()

    def getTootText(self):
        if self.erabiltzailea.mastodon_id:
            return truncatechars(self.izenburua, 230) + ' @%s 2dz ' % (self.erabiltzailea.mastodon_id) + self.get_absolute_url()
        else:
            return truncatechars(self.izenburua, 250) + ' ' + self.get_absolute_url()

    def getTelegramText(self):
        return self.izenburua + ' ' + self.erabiltzailea.getFullName() + " 2dz " + self.get_absolute_url()

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

    def save(self, *args, **kwargs):
        if not self.izenburua[0].isupper():
            self.izenburua[0].upper()
        if not self.desk[0].isupper():
            self.desk[0].upper()
        super(GamePlaya, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Gameplaya"
        verbose_name_plural = "Gameplayak"

    def __str__(self):
        return u'%s' % (self.izenburua)
