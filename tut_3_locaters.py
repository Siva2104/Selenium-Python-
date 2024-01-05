from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

driver_path = r"C:\\Users\\SHIVA\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
driver =  webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)



driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")

driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("secret_sauce")

driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input").click()

time.sleep(5)


#link text and partial link text
#driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack").click()
time.sleep(3)
#driver.find_element(By.PARTIAL_LINK_TEXT,"Labs Backpack").click()
time.sleep(3)

#class_name is for multiple name selections
links = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
print(len(links))
time.sleep(3)

image = driver.find_elements(By.TAG_NAME,"img")
print(len(image))
time.sleep(3)



