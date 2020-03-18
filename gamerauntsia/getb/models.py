from django.db import models
from django.conf import settings
from photologue.models import Photo
from django.utils import timezone
from django.template import defaultfilters as filters
from django.template.loader import get_template
from django.template import Context

STATUS = (
    ('0', 'Zirriborroa'),
    ('1', 'Publikoa'),
)


class Atala(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, db_index=True,
                            help_text="Eremu honetan game play honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    iraupena_min = models.IntegerField(default=0)
    iraupena_seg = models.IntegerField(null=False, blank=False, default=0)

    argazkia = models.ForeignKey(Photo, on_delete=models.PROTECT)
    bideoa = models.CharField(max_length=100, null=True, blank=True,
                              help_text="Eremu honetan Youtube bideoaren URL kodea itsatsi behar duzu. Adb.: c21XAuI3aMo")

    publikoa_da = models.BooleanField(default=False, verbose_name="Publikatzeko prest")
    pub_date = models.DateTimeField('publikazio data', default=timezone.now)
    mod_date = models.DateTimeField('modifikazio data', default=timezone.now)
    shared = models.BooleanField(default=False,
                                 help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.")

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

    def get_url(self):
        url = ''
        if self.bideoa.startswith('http://vimeo.com'):
            url = self.bideoa.replace('http://vimeo.com/', '')
        elif self.bideoa.startswith('http://youtu.be'):
            url = self.bideoa.replace('http://youtu.be/', '')
        return url

    def get_absolute_url(self):
        return '%sgetb/%s' % (settings.HOST, self.slug)

    def getTwitText(self):
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
                'img_url': settings.HOST + self.argazkia.get_blog_url()
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
        super(Atala, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Atala"
        verbose_name_plural = "Atalak"

    def __str__(self):
        return u'%s' % (self.izenburua)
