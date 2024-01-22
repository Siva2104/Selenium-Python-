from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(application_link)
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.close()
