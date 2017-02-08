from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = "http://newtours.demoaut.com/mercuryreservation.php"

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get(url)

assert "Mercury Tours" in driver.title, "This is not a Mercury Tours site"

driver.find_element_by_name("userName").send_keys("test")
driver.find_element_by_name("password").send_keys("test")
driver.find_element_by_name("login").click()

driver.find_element_by_link_text("registration form").click()
select = Select(driver.find_element_by_name("country"))
select.select_by_visible_text("INDIA")
driver.find_element_by_name("email").send_keys("testuser1")
driver.find_element_by_name("password").send_keys("Gyp.s8m1")
driver.find_element_by_name("confirmPassword").send_keys("Gyp.s8m1")
driver.find_element_by_name("register").click()

driver.find_element_by_link_text("Flights").click()
radio_buttons = driver.find_elements_by_name("tripType")
for radio in radio_buttons:
 if radio.get_attribute("value") == "oneway":
  if not radio.is_selected():
   radio.click()
  else:
   print "one way trip already selected"

for radio in radio_buttons:
 if radio.get_attribute("value") == "oneway":
  if not radio.is_selected():
   radio.click()
  else:
   print "one way trip already selected"

drop_down_dict = { "passCount" : "2", "fromPort" : "London", "fromMonth" : "2", "fromDay" : "3", "toPort" : "Paris", "toMonth" : "3" }

for k in drop_down_dict.keys():
 select = Select(driver.find_element_by_name(k))
 select.select_by_value(drop_down_dict[k])

select 
time.sleep(10)
driver.close()

