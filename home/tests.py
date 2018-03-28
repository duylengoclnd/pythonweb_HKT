from django.test import TestCase,SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_status_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

# Create your tests here.
