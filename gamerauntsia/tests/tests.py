from django.test import TestCase

class BasicTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('urtzai', 'uodriozola@gmail.com', 'urtzaipass')


    def test_index(self):
        c = Client()
        url = reverse('index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
