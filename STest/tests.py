from selenium import webdriver 
import unittest

from selenium.webdriver.common.keys import Keys
import time


#kaysir
#from selenium.webdriver.common.keys import keys
#import time

class PageTest(unittest.TestCase):
	def setUp(self):
	 	self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 	self.browser.get('http://localhost:8000/')
	 	self.assertIn('Comment',self.browser.title)

	def check_rows_in_list(self,row_text):
		table = self.browser.find_element_by_id('list')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Comment', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('Stress Tips Buddy Box', headerText)

		input1 = self.browser.find_element_by_id('comment_author')
		self.assertEqual(input1.get_attribute('placeholder'), 'Input your name')
		input1.click()
		time.sleep(1)
		input1.send_keys('Joice Drilon')
		time.sleep(1)
		
		input2 = self.browser.find_element_by_id('email')
		self.assertEqual(input2.get_attribute('placeholder'), 'Input your email')
		input2.click()
		time.sleep(1)
		input2.send_keys('joice@gmail.com')
		time.sleep(1)

		input3 = self.browser.find_element_by_id('comment')
		self.assertEqual(input3.get_attribute('placeholder'), 'Input your comment')
		input3.click()
		time.sleep(1)
		input3.send_keys('This is the breakfree')
		time.sleep(1)
		
		submit = self.browser.find_element_by_id('submit')
		submit.click()
		time.sleep(2)

		table = self.browser.find_element_by_id('list')
		rows = table.find_element_by_tag_name('tr')
	


#kay sir apr 13	
'''
from selenium.webdriver.common.keys import Keys
import time

from django.test import LiveServerTestCase #apr 16 2021

#import unittest

#class PageTest(unittest.TestCase):   #apr 16 2021
class PageTest(LiveServerTestCase):	
	def setUp(self):
	 self.browser = webdriver.Firefox()

#if __name__ == '__main__':  #apr 16 2021
	unittest.main()

	def setUp(self): 
		self.browser = webdriver.Firefox()
	
	#def tearDown(self):
		#self.browser.quit()

	def check_rows_in_listtable(self,row_text):
		# table = self.browser.find_element_by_id('listtable')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn(row_text, [row.text for row in rows])

		start_time = time.time() # 4-16-2021 30:45 14:36
		while time.time() start_time
		#di pa tapos



	def test_start_list_and_retrieve_it(self):
		#self.browser.get('http://localhost:8000') #apr 16,2021
		self.browser.get(self.live_server_url)

		self.asserIn('Contact Tracing List', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Tracing', headerText)
		inputbox = self.browser.find_element_by_id('personEntry')
		self.assertEqual(inputbox.get_attribute('placeholder','You have contact'))
		
		carrier = self.browser.find_element_by_id('newPatient')
		carrier.click()
		time.sleep(1) 
		carrier.send_keys('Jesper Johansson')
		time.sleep(1)
		carResidence = self.browser.find_element_by_id('carResidence')
		carResidence.click()
		time.sleep(1)
		carResidence.send_keys('Smeerensburg, North Pole')
		time.sleep(1)
		inPerson = self.browser.find_element_by_id('personEntry')
		inPerson = click()
		time.sleep(1)
		inPerson.send_keys('Mickey Mouse')
		time.sleep(1)
		inPlace = self.browser.find_element_by_id('placeEntry')
		time.sleep(1)
		inPlace.click()
		time.sleep(1)
		inPlace.send_keys('Disney Wonderland')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)
		self.check_rows_in_listable('1:Mickey Mouse')#in Disney Wonderland
		#The
		inPerson = self.browser.find_element_by_id('personEntry')
		time.sleep(1)
		inPerson.click()
		time.sleep(1)
		inPerson.send_keys('Red Shoes White')
		inPlace = self.browser.find_element_by_id('placeEntry')
		time.sleep(1)
		inPlace.click()
		inPlace.send_keys("King White's Palace")
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)
		btnConfirm.click()
		time.sleep(2)
		self.check_rows_in_listtable('1: Mickey Mouse')# in Disney Wonderland
		self.check_rows_in_listtable('2: Red Shoes White')
		#the page should updates and shows 2 names on the list
		table = self.browser.find_element_by_id('listtable')
		rows = table.find_elements_by_tag_name('tr')

		#self.assertIn('1: Mickey Mouse in Disney Wonderland', [row.text for row in])

		#dipa tapos


'''

if __name__ == '__main__':
	unittest.main()

#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:8000')
