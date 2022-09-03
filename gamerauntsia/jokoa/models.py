from django.db import models
from django.conf import settings
from photologue.models import Photo
from django.utils import timezone

SOFTWARE_AUKERAK = (
    ('C', 'Jabeduna - ordainpekoa'),
    ('FR', 'Jabeduna - doakoa'),
    ('OS', 'Librea edo irekia'),
)


class Generoa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan etiketa honen URL helbidea zehazten ari zara.")

    class Meta:
        verbose_name = "Generoa"
        verbose_name_plural = "Generoak"

    def __str__(self):
        return u'%s' % (self.izena)


class Plataforma(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan plataforma honen URL helbidea zehazten ari zara.")
    icon = models.ForeignKey(Photo, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformak"

    def __str__(self):
        return u'%s' % self.izena


class Garatzailea(models.Model):
    izena = models.CharField(max_length=64)
    desk = models.TextField(max_length=256, null=True, blank=True, verbose_name="Deskribapena")
    slug = models.SlugField(db_index=True, unique=True)
    url = models.CharField(max_length=64)
    logoa = models.ForeignKey(Photo, on_delete=models.PROTECT)
    sorrera_data = models.DateField(blank=True, null=True)
    itxiera_data = models.DateField(blank=True, null=True)
    plataformak = models.ManyToManyField(Plataforma)
    ytube_channel = models.CharField(max_length=150, null=True, blank=True, verbose_name="Youtube kanala")
    twitter_id = models.CharField(max_length=100, blank=True, null=True)
    facebook_id = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField('Telefonoa', max_length=25, blank=True, null=True)

    class Meta:
        verbose_name = "Garatzailea"
        verbose_name_plural = "Garatzaileak"

    def __str__(self):
        return self.izena

    def get_available_platforms(self):
        platforms = []
        for plataforma in self.plataformak.all():
            platforms.append(plataforma.izena)
        platforms.sort()
        return ', '.join(platforms)


class Jokoa(models.Model):
    izena = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, unique=True,
                            help_text="Eremu honetan joko honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256, null=True, blank=True, verbose_name="Deskribapena")
    bertsioa = models.CharField(max_length=64, null=True, blank=True,
                                help_text="Joko saga bat bada, zehaztu hemen bertsioa.")
    lizentzia = models.CharField(max_length=2, default='C', choices=SOFTWARE_AUKERAK)
    argitaratze_data = models.DateField(blank=True, null=True,
                                        help_text="Jokoa noiz argitaratu zen edo argitaratuko den.")

    logoa = models.ForeignKey(Photo, on_delete=models.PROTECT)
    karatula = models.ForeignKey(Photo, on_delete=models.PROTECT, blank=True, null=True, related_name="karatula")
    steam_id = models.IntegerField(null=True, blank=True,
                                   help_text="Jokoa Steam plataforman aurki badaiteke, jokoaren fitxaren URLan agertzen den zenbakia. Adibidez: 236110")
    trailer = models.CharField(max_length=64, null=True, blank=True, verbose_name="Youtube trailerra",
                               help_text="Steam ID zenbakia jarrita badago, ez da beharrezkoa. Bestela, Youtube bideoaren KODEA itsatsi. Adibidez: bkgzXpKbVGE")
    url = models.CharField(max_length=64, help_text="Eremu honetan joko honen atariko URL helbidea zehazten ari zara.")
    wiki = models.CharField(max_length=64, null=True, blank=True,
                            help_text="Eremu honetan joko honen wikipediako URL helbidea zehaztu mesedez.")

    garatzailea = models.ForeignKey(Garatzailea, blank=True, null=True, on_delete=models.PROTECT)
    generoak = models.ManyToManyField(Generoa, blank=True, null=True)
    publikoa_da = models.BooleanField(default=False)
    mod_date = models.DateTimeField('modifikazio data', default=timezone.now)

    def get_title(self):
        return "%s %s" % (self.izena, self.bertsioa)

    def get_absolute_url(self):
        return "%sjokoak/%s" % (settings.HOST, self.slug)

    def get_basque_available_platforms(self):
        platforms = []
        for itzulpena in self.jokoitzulpena_set.all():
            for plataforma in itzulpena.plataformak.all():
                platforms.append(plataforma.izena)
        platforms.sort()
        return ', '.join(platforms)

    def get_generoak(self):
        generoak = [g.izena for g in self.generoak.all()]
        return ', '.join(generoak)

    def get_itzulpenak(self):
        return self.jokoitzulpena_set.all()

    def get_photo(self):
        if self.logoa:
            return self.logoa
        else:
            return None

    def get_karatula(self):
        if self.karatula:
            return self.karatula
        else:
            return self.get_photo()

    class Meta:
        verbose_name = "Jokoa"
        verbose_name_plural = "Jokoak"

    def __str__(self):
        if self.bertsioa:
            return u'%s %s' % (self.izena, self.bertsioa)
        else:
            return self.izena
