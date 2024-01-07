 #2) What are XPath Axes?

'''Answer: An XPath axes define the node-set relative to the current (context) node.
It is used to locate the node that is relative to the node on that tree.'''



'''
syntax-example:
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/child::tag_name")
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')])
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/descending::tag_name")
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/following::tag_name")
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/preceding::tag_name")

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

driver_path = r"C:\\Users\\SHIVA\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
driver =  webdriver.Chrome(service=service)

driver.get("https://money.rediff.com/index.html")
driver.maximize_window()
time.sleep(3)


# xpath Axes is used to locate the element if the xpath fails
#  Node relative to the node in the tree
#self>>parent>>ancestor
#
#


#self
text = driver.find_element(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/self::a").text
print(text)


# #parents
# parents = driver.find_element(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/parent::li").text
# print(parents)


#child


# ancestor
ancestor = driver.find_elements(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/child::li")
print(ancestor)

# ancestor S&P BSE 500 30971.04 +79.24 (+0.26%)
ancestor1 = driver.find_element(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul").text
print(ancestor1)


#total num of links in page  links are  209
links = driver.find_elements(By.TAG_NAME,"a")
print("links are ",len(links))


# descendant node

Descendant_node = driver.find_element(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/descendant::*").text
print(len(Descendant_node))


#following node

following = driver.find_element(By.XPATH,"//a[contains(text(),'S&P BSE 500')]/ancestor::ul/following::*").text
print(len(following))

#following _sibling
following_sibling = driver.find_element(By.XPATH,"//a[contains(.,'S&P BSE Sensex')]/ancestor::ul/following-sibling::*").text
print(len(following_sibling))

#Preceding::above nodes
following_sibling = driver.find_element(By.XPATH,"//a[contains(.,'S&P BSE Sensex')]/ancestor::ul/preceding::*").text
print(len(following_sibling))


