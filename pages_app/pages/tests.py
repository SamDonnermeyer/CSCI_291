# pages/tests.py
from django.test import SimpleTestCase

# Create Simple Test
class SimpleTests(SimpleTestCase):
    ## Home Page ##
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    ## About Page ##
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
