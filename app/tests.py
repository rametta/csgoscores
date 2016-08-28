from django.test import TestCase

# run tests: python manage.py test

# Test Pages
class PagesTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_search(self):
        r = self.client.get('/search/')
        self.assertEqual(r.status_code, 200)
