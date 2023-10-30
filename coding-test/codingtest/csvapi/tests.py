from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class MyViewTestCase(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
