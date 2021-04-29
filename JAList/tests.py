from django.test import TestCase
from django.http import HttpRequest
#from django.http import HttpResponse
from django.template.loader import render_to_string
#from django.urls import resolve
#from JAList.models import Item

# Create your tests here.

class MyPageTest(TestCase):

	def test_mypage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'comment.html')

	def test_save_POST_request(self):
		response = self.client.post('/',data={'comment_author':'new_author'})
		self.assertIn('new_author', response.content.decode())
		self.assertTemplateUsed(response,'comment.html')
	








'''
#kay sir 04-13-2021

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)


'''


'''

#kay sir 04-13-2021
	def test_save_post_request(self):
		response = self.client.post('/',data={'personEntry': 'frenzy'} )
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'frenzy')

		
#april 15 2021

		#self.assertEqual(response.status_code, 302)
		#self.assertEqual(response['location'], '/')		

		#self.assertIn('frenzy', response.content.decode())
		#self.assertTemplateUsed(response,'comment.html')

		#self.assertIn('New entry', response.content.decode())
		#self.assertTemplateUsed(response,'comment.html')
		#response = self.client.post('/', data={'personEntry': 'New entry'})
				
	def	test_redirect_post_self:

		response = self.client.post('/',data={'personEntry': 'frenzy'} )
	
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')		
	
	def test_template_displays_list(self):
		Item.objects.create(text='List item 1')
		Item.objects.create(text='List item 2')
		response = self.client.get('/')
		self.assertIn('List item 1', response.content.decode())
		self.assertIn('List item 2', response.content.decode())
		
		
'''


'''
#kay sir 4-13-2021

from CTList.models import Item

class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(),2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')




'''



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