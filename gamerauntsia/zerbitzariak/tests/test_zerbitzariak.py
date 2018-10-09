import os
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from gamerauntsia.zerbitzariak.forms import MCForm
from gamerauntsia.gamer.models import GamerUser

class ZerbitzariakTest(TestCase):
    def setUp(self):
        user = GamerUser.objects.create_user('urtzai', 'uodriozola@gmail.com', 'urtzaipass')
        user.is_superuser = True
        user.save()

    def test_minecraft_index(self):
        c = Client()
        url = reverse('minecraft_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_minecraft_mapa(self):
        c = Client()
        url = reverse('minecraft_mapa')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_mumble_index(self):
        c = Client()
        url = reverse('mumble_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_MCForm(self):
        form_data = {'mc_user': 'urtzai', 'lizentzia': True}
        form = MCForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_minecraft_add(self):
        c = Client()
        c.login(username='urtzai', password='urtzaipass')
        url = reverse('minecraft_add')
        response = c.post(url, {'mc_user': 'urtzai', 'lizentzia': True})
        self.assertEqual(response.status_code, 200)