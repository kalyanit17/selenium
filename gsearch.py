import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,ElementNotVisibleException

def init_driver():
 driver = webdriver.Chrome("C:\chromedriver.exe")
 driver.wait = WebDriverWait(driver,5)
 return driver
 
def lookup(driver,query):
 driver.get("http://www.google.com")
 
 try:
  box = driver.wait.until(EC.presence_of_element_located((By.NAME,"q")))
  button = driver.wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
  box.send_keys(query)
  try:
   button.click()
  except ElementNotVisibleException:
   search_btn = driver.wait.until(EC.visibility_of_element_located((By.NAME,"btnG")))
   search_btn.click()
 except TimeoutException:
  print "Box or Button not found in google.com"
  
if __name__ == "__main__":
 driver = init_driver()
 lookup(driver,"Selenium")
 time.sleep(5)
 driver.quit()
 


