from selenium import webdriver
import argparse
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException,NoSuchElementException,TimeoutException

parser = argparse.ArgumentParser(description="My first selenium1")
parser.add_argument("-u","--url",dest="url",help="url to scrape")

url="http://thedemosite.co.uk/addauser.php"
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get(url)
driver.find_element_by_name("username").send_keys("kalyan_tella")
driver.find_element_by_name("password").send_keys("Gyp.s8m")
driver.find_element_by_name("FormsButton2").click()
driver.find_element_by_link_text("4. Login").click()

driver.find_element_by_name("username").send_keys("kalyan_tella")
driver.find_element_by_name("password").send_keys("Gyp.s8m")
driver.find_element_by_name("FormsButton2").click()

assert "Successful Login" in driver.page_source, "Unsuccessful login attempt" 

driver.find_element_by_link_text("2. The Database").click()
driver.find_element_by_link_text("add a User").click()

driver.find_element_by_name("username").send_keys("xyzdsfsafsadfsafsafsd")
driver.find_element_by_name("password").send_keys("sdkjfsdf")
driver.find_element_by_name("FormsButton2").click()

try:
 WebDriverWait(driver,10).until(EC.alert_is_present(),'new alert is present')
except TimeoutException:
 print "No alert present"
 
try:
 alert = driver.switch_to_alert()
 assert "Username too short" in alert.text,"Username length is fine" 
 alert.accept()
except NoAlertPresentException:
 print "No alert present"


time.sleep(5)
driver.close()