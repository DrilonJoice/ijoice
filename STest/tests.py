from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



   	def wait_for_table(self, row_text):        
   	    start_time = time.time()
   	    while True:  
   	        try:                
   	            table = self.browser.find_element_by_id('tablelist')       	                 
   	            rows = table.find_elements_by_tag_name('tr')                
   	            self.assertIn(row_text, [row.text for row in rows])
   	            return
   	        except (AssertionError, WebDriverException) as e:  
   	            if time.time() - start_time > MAX_WAIT:  
                       raise e                  
   	            time.sleep(0.5)  
      
   	def setUp(self):
   	    self.browser = webdriver.Firefox()
   	def test_start_list_and_retrieve_it(self):
	    self.browser.get('http://localhost:8000')
	    #self.browser.get(self.live_server_url)
	    self.assertIn('Online Student Financial Assistance', self.browser.title)
	    headerText = self.browser.find_element_by_tag_name('h1').text
	    self.assertIn('Online Student Financial Assistance', headerText)

	    input1 = self.browser.find_element_by_id('name')
	    self.assertEqual(input1.get_attribute('placeholder'), 'Input your name')
	    input1.click()
	    time.sleep(1)
	    input1.send_keys('Joice Drilon')
	    time.sleep(1)
		
	    input2 = self.browser.find_element_by_id('school')
	    self.assertEqual(input2.get_attribute('placeholder'), 'Input your school')
	    input2.click()
	    time.sleep(1)
	    input2.send_keys('TUPC')
	    time.sleep(1)


	    submit = self.browser.find_element_by_id('submit')
	    submit.click()
	    time.sleep(2)
		
	    input3 = self.browser.find_element_by_id('ysection')
	    self.assertEqual(input3.get_attribute('placeholder'), 'Input your Year and Section')
	    input3.click()
	    time.sleep(1)
	    input3.send_keys('3rd Year - 3B')
	    time.sleep(1)
		
	    input4 = self.browser.find_element_by_id('address')
	    self.assertEqual(input4.get_attribute('placeholder'), 'Input your Address')
	    input4.click()
	    time.sleep(1)
	    input4.send_keys('BLK 27 LOT 20 Brgy. Sto. Nino')
	    time.sleep(1)
		
	    input5 = self.browser.find_element_by_id('cnumber')
	    self.assertEqual(input5.get_attribute('placeholder'), 'Input your Contact Number')
	    input5.click()
	    time.sleep(1)
	    input5.send_keys('0912345689')
	    time.sleep(1)

	    submit = self.browser.find_element_by_id('submit')
	    submit.click()
	    time.sleep(2)

		
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
