#Test cases

#open browser >> Open url >> enter user name and password >> Click login and signin

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

class browser:
    def __init__(self):
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        while (True):
            pass
