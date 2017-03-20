from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class BasicTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('urtzai', 'uodriozola@gmail.com', 'urtzaipass')

    def test_index(self):
        c = Client()
        url = reverse('index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
