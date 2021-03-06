from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import getpass
import time
 
def page_loaded(driver):
	return driver.find_element_by_tag_name("body") != None
 
# Taking inputs from the console
print("Logging Details for Facebook:\n")
input_email_id = input("Enter Username: ")
input_pwd = input("Enter Password: ")
 
# Opening the web browser
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_loaded)
 
# print(driver.page_source)
 
# Finding email and password fields and sending the keys
email = driver.find_element_by_id("email")
email.send_keys(input_email_id)
pwd = driver.find_element_by_id("pass")
pwd.send_keys(input_pwd)
 
time.sleep(3)
 
driver.get("https://www.facebook.com/events/birthdays")
 
box_count = len(driver.find_elements_by_class_name("innerWrap"))
 
for x in range(0, box_count):
	text_box = driver.find_element_by_tag_name('textarea')
	text_box.send_keys("Happy Birthday!! \n")	# The birthday message
	
	time.sleep(3)
 
driver.close()
