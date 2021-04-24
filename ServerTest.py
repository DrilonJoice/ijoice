from selenium import webdriver
import unittest
#kaysir
#from selenium.webdriver.common.keys import keys
#import time

class PageTest(unittest.TestCase):
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 self.assertIn('Comment',self.browser.title)

#kay sir apr 13	
'''
	def check_rows_in_listtable(self,row_text):
		table = self.browser.find_element_by_id('listtable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
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
		inPerson.send_keys('Micke Mouse')
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
		self.check_rows_in_listable('1:Mickey Mouse in Disney Wonderland')
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
		#dipa tapos


'''

if __name__ == '__main__':
	unittest.main()

#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:8000')
