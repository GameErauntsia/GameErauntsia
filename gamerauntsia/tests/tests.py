import os
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.getb.models import Atala
from gamerauntsia.jokoa.models import Plataforma, Jokoa
from gamerauntsia.gameplaya.models import Zailtasuna, Kategoria, GamePlaya
from gamerauntsia.berriak.models import Gaia, Berria
from photologue.models import Photo
from django.core.files.base import ContentFile

RES_DIR = os.path.join(os.path.dirname(__file__), '../res')
LANDSCAPE_IMAGE_PATH = os.path.join(RES_DIR, 'test_photologue_landscape.jpg')

class BasicTest(TestCase):
    def setUp(self):
        user = GamerUser.objects.create_user('urtzai', 'uodriozola@gmail.com', 'urtzaipass')
        photo = Photo(title='GETB atala irudia', slug='gtb-atala-irudia', is_public=True)
        photo.image.save('test_photologue_landscape.jpg', ContentFile(open(LANDSCAPE_IMAGE_PATH, 'rb').read()))
        photo.save()
        Atala.objects.create(izenburua='GETB atala', slug='getb-atala', desk='Lehen atala duzue honako hau.', argazkia=photo,  publikoa_da=True)

        plataforma = Plataforma.objects.create(izena='Play Station 4', slug='play-station-4')
        jokoa = Jokoa.objects.create(izena='Call of Duty', bertsioa='4', slug='call-of-duty-4', logoa=photo, publikoa_da=True)
        zailtasuna = Zailtasuna.objects.create(izena='Zaila', slug='zaila')
        kategoria = Kategoria.objects.create(izena='FPS', slug='fps', desk="First Person Shooter")
        gameplaya = GamePlaya(izenburua='Barrebusa 1', slug='barrebusa-1', desk="Espero dut gustuko izatea.", argazkia=photo, bideoa='c21XAuI3aMo',
                                 jokoa=jokoa, plataforma=plataforma, zailtasuna=zailtasuna, erabiltzailea=user, publikoa_da=True, status='1')
        gameplaya.save()
        gameplaya.kategoria.add(kategoria)
        gameplaya.save()

        gaia = Gaia.objects.create(izena='Berriak', slug='berriak')
        berria = Berria(izenburua='Switch argitaratu da', slug='switch-argitaratu-da', desk="Nintendoren kontsola berria argitaratu da.", erabiltzailea=user, argazkia=photo,
                              jokoa=jokoa, publikoa_da=True, status='1')
        berria.save()
        berria.gaia.add(gaia)
        berria.save()

    def test_index(self):
        c = Client()
        url = reverse('index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getb_index(self):
        c = Client()
        url = reverse('getb_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getb_atala(self):
        c = Client()
        url = reverse('getb_atala', kwargs={'slug': 'getb-atala'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_berriak_index(self):
        c = Client()
        url = reverse('berriak_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_berriak_gaia(self):
        c = Client()
        url = reverse('gaia', kwargs={'slug': 'berriak'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_berriak_berria(self):
        c = Client()
        url = reverse('berria', kwargs={'slug': 'switch-argitaratu-da'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_index(self):
        c = Client()
        url = reverse('gameplay_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_category(self):
        c = Client()
        url = reverse('gameplay_category', kwargs={'kategoria': 'fps'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_level(self):
        c = Client()
        url = reverse('gameplay_level', kwargs={'maila': 'zaila'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_game(self):
        c = Client()
        url = reverse('gameplay_game', kwargs={'jokoa': 'call-of-duty-4'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_platform(self):
        c = Client()
        url = reverse('gameplay_platform', kwargs={'plataforma': 'play-station-4'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameplayak_gameplaya(self):
        c = Client()
        url = reverse('gameplay', kwargs={'slug': 'barrebusa-1'})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_jokoa_index(self):
        c = Client()
        url = reverse('game_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_bazkidetza_index(self):
        c = Client()
        url = reverse('bazkidetza')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_komunitatea_index(self):
        c = Client()
        url = reverse('komunitatea')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
