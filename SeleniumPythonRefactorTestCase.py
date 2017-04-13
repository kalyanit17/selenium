import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

class SearchText(unittest.TestCase):
 @classmethod
 def setUp(self):
  self.driver = webdriver.Chrome("C:\chromedriver.exe")
  self.wait = WebDriverWait(self.driver,10)
  self.driver.get("https://www.google.com")
  #self.driver.maximize_window()
  
 def test_search_text(self):
  self.search_field = self.driver.find_element_by_name("q")
  
  self.search_field.clear()
  self.search_field.send_keys("Selenium WebDriver Interview questions")
  
  try:
   submit_btn = self.wait.until(EC.presence_of_element_located((By.NAME,"btnG")))
  except TimeoutException:
   print "Caught TimeoutException"
   sys.exit()
   submit_btn.click()
  
  try:
   lists = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"r")))
  except TimeoutException:
   print "Caught TimeoutException"
   sys.exit()
  
  self.assertEqual(11,len(lists)) 
 
 @classmethod
 def tearDown(self):
  self.driver.close()


if __name__ == "__main__":
 unittest.main()
