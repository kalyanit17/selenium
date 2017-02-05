from selenium import webdriver
import time

url = "http://newtours.demoaut.com/mercuryreservation.php"

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get(url)

assert "Mercury Tours" in driver.title, "This is not a Mercury Tours site"

driver.find_element_by_name("userName").send_keys("test")
driver.find_element_by_name("password").send_keys("test")
driver.find_element_by_name("login").click()

driver.find_element_by_link_text("registration form").click()
time.sleep(10)

driver.close()

