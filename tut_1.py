from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#driver = webdriver.Chrome(r"C:\\Users\\SHIVA\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver_path = r"C:\\Users\\SHIVA\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)


username_input = None
password_input = None

while username_input is None or password_input is None:
    try:
        username_input = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        password_input = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
    except:
        time.sleep(1)

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
time.sleep(5)

##capture the title and
