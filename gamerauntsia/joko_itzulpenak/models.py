from django.db import models
from django.utils import timezone
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from django.utils import timezone
from django.conf import settings

PROIEKTU_EGOERAK = [
    ('0', 'Lanean'),
    ('1', 'Laguntza bila'),
    ('2', 'Bukatuta'),
    ('3', 'Eguneratzeke'),
]

PARTE_HARTZAILE_MOTAK = [
    ('0', 'Itzultzailea'),
    ('1', 'Zuzentzailea'),
    ('2', 'Laguntzailea'),
    ('3', 'Probatzailea'),
]

ITZULPEN_JATORRIAK = [
    ('0', 'Jatorrizkoa euskaraz'),
    ('1', 'Garatzaileen itzulpena'),
    ('2', 'Zaleen itzulpena'),
]


class JokoItzulpena(models.Model):
    jokoa = models.ForeignKey(Jokoa, on_delete=models.CASCADE)
    plataformak = models.ManyToManyField(Plataforma)
    sortze_data = models.DateField(default=timezone.now, null=True, blank=True)
    erabilgarritasun_data = models.DateField(null=True, blank=True)
    publikoa_da = models.BooleanField(default=True, verbose_name="Publikoa da")
    ofiziala_da = models.BooleanField(default=False, verbose_name="Ofiziala da")
    jatorria = models.CharField(max_length=1, choices=ITZULPEN_JATORRIAK, default='0')

    def get_jatorria(self):
        if self.jatorria == '2' and self.ofiziala_da:
            return "Zaleen itzulpen ofiziala"
        else:
            return self.get_jatorria_display()

    def get_mota(self):
        if hasattr(self, 'itzulpenproiektua'):
            return "itzulpenproiektua"
        elif hasattr(self, 'kanpokoitzulpena'):
            return "kanpokoitzulpena"
        return None

    def get_url(self):
        if self.get_mota() == 'itzulpenproiektua':
            return self.itzulpenproiektua.get_url()
        else:
            return self.kanpokoitzulpena.url


class ItzulpenProiektua(JokoItzulpena):
    egoera = models.CharField(max_length=1, choices=PROIEKTU_EGOERAK, default='0')
    slug = models.SlugField(db_index=True, unique=True)
    deskribapena = models.TextField(max_length=256, null=True, blank=True)
    external_url = models.CharField(max_length=150, null=True, blank=True)
    arduraduna = models.ForeignKey(GamerUser, null=True, blank=True, on_delete=models.PROTECT,
                                   related_name='arduraduna')
    parte_hartzaileak = models.ManyToManyField(GamerUser, through='ItzulpenProiektuParteHartzailea')
    parte_hartzaileak_oharra = models.TextField(max_length=256, null=True, blank=True)
    instalazioa = models.TextField(null=True, blank=True)
    ohar_teknikoak = models.TextField(null=True, blank=True)
    eguneratze_data = models.DateField(default=timezone.now, null=True, blank=True)

    def get_url(self):
        return "/itzulpenak/proiektuak/%s" % (self.slug)

    def get_absolute_url(self):
        return '%sitzulpenak/proiektuak/%s' % (settings.HOST, self.slug)

    def __str__(self):
        return u'Itzulpen proiektua - %s' % (self.jokoa.izena)

    class Meta:
        verbose_name = "Itzulpen proiektua"
        verbose_name_plural = "Itzulpen proiektuak"


class ItzulpenFitxategia(models.Model):
    proiektua = models.ForeignKey(ItzulpenProiektua, on_delete=models.CASCADE)
    izena = models.CharField(max_length=150)
    deskribapen_laburra = models.CharField(max_length=300, verbose_name="Deskribapen laburra")
    fitxategia = models.FileField(null=True, blank=True, upload_to='itzulpen_fitxategiak')
    url = models.CharField(max_length=150, null=True, blank=True)
    sortze_data = models.DateTimeField(default=timezone.now)

    def get_download_url(self):
        if self.fitxategia:
            return self.fitxategia.url
        else:
            return self.url

    class Meta:
        verbose_name = "Itzulpen fitxategia"
        verbose_name_plural = "Itzulpen fitxategiak"


class ItzulpenProiektuParteHartzailea(models.Model):
    proiektua = models.ForeignKey(ItzulpenProiektua, on_delete=models.CASCADE)
    erabiltzailea = models.ForeignKey(GamerUser, on_delete=models.CASCADE)
    mota = models.CharField(max_length=1, choices=PARTE_HARTZAILE_MOTAK, default='0')

    class Meta:
        verbose_name = "Proiektuko parte hartzailea"
        verbose_name_plural = "Proiektuko parte hartzaileak"


class KanpokoItzulpena(JokoItzulpena):
    url = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return u'Kanpoko itzulpena - %s' % (self.jokoa.izena)

    class Meta:
        verbose_name = "Kanpoko itzulpena"
        verbose_name_plural = "Kanpoko itzulpenak"
