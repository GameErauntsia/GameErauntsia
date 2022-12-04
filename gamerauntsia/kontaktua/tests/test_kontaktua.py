from django.test import TestCase
from django.test import Client
from django.urls import reverse


class KontaktuaTest(TestCase):
    def test_kontaktua_index(self):
        c = Client()
        response = c.get(reverse("kontaktua"))
        self.assertEqual(response.status_code, 200)
