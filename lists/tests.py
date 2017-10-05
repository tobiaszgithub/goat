from django.test import TestCase
from django.urls.base import resolve
from lists.views import home_page
from django.http.request import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
            response = self.client.get('/')
            self.assertTemplateUsed(response, 'home.html')