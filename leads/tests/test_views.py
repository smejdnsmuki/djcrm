from django.test import TestCase
from django.urls import reverse

# We make a new folder 'tests' in the app and inside it '__init__.py'. We move the original test.py in it and
# rename it to test_views.py because it will be determined to test the views.

class LandingPageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        # print(response.content)
        # print(response.status_code)
        self.assertEqual(response.status_code, 200) # comparing status_code == 200

    def test_template_name(self):
        response = self.client.get(reverse('landing-page'))
        self.assertTemplateUsed(response, 'landing.html')