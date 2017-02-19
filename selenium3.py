from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import re

class AwberTesting(unittest.TestCase):
 
 @classmethod
 def setUp(cls):
  cls.driver = webdriver.Chrome("C:\\chromedriver.exe")
  
 def test_title(self):
  self.driver.get("https://www.aweber.com/")
  self.assertEqual(self.driver.title,"Email Marketing | AWeber")

 def test_pricing(self):
  self.driver.get("https://www.aweber.com/")
  self.driver.find_element_by_link_text("Pricing").click()
  pricing_table = self.driver.find_element_by_class_name("feature-table")
  prices = pricing_table.find_elements_by_class_name("feature-row-header")
  prices = [ int(re.match(r'^\$(\d+)',price.text).group(1)) for price in prices if re.match(r'(^\$\d+)',price.text) ]
  self.assertIn(49,prices)
  self.assertIn(69,prices)
  self.assertIn(149,prices)
  
 def test_default_monthly(self):
  self.driver.get("https://www.aweber.com/order.htm")
  monthly_button = self.driver.find_element_by_id("monthly")
  self.assertFalse(monthly_button.is_selected())
  
 def test_search(self):
  self.driver.get("https://www.aweber.com/search.htm")
  search_text = self.driver.find_element_by_id("query")
  search_text.send_keys("Meet the Team")
  search_text.send_keys(Keys.RETURN)
  
 @classmethod
 def tearDown(cls):
  cls.driver.quit()
