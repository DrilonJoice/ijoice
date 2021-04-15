from django.test import TestCase
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your tests here.

class MainPageTest(TestCase):
	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'sample.html')

'''
class HomePageTest(TestCase):
	def test mainpage_returns_correct view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response.'Sample.html')
'''
'''
class HomePageTest(TestCase):
	def test_homepage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'sample.html')
'''