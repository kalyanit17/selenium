import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class HomePageTest(unittest.TestCase):
 
 @classmethod
 def setUp(cls):
  cls.driver = webdriver.Chrome("C:\chromedriver.exe")
  cls.wait = WebDriverWait(cls.driver,10)
  cls.driver.get("https://www.google.com")
  #cls.driver.maximize_window()
  
 def test_search_textbox(self):
  self.assertTrue(self.is_element_present(By.NAME,"q"))
  
 def test_search_id(self):
  self.assertTrue(self.is_element_present(By.ID,'_eEe'))
  
 def test_search_images(self):
  images = self.driver.find_element_by_link_text("Images")
  images.click()
  
  self.assertTrue(self.is_element_present(By.NAME,"q"))
  search_text = self.driver.find_element_by_name("q")
  search_text.clear()
  search_text.send_keys("Python")
  search_text.submit()
  
 def is_element_present(self,how,what):
  try:
   self.driver.find_element(by=how,value=what)
  except NoSuchElementException:
   return False
  return True
  
 @classmethod
 def tearDown(cls):
  cls.driver.quit()
  
if __name__ == "__main__":
 unittest.main()