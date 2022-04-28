import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")

# 1) Locator matching with a single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Macbook")

# 2) Locator matching with a multiple webelements
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)


# 3) Element not available zero will be returned
# driver.find_element(By.LINK_TEXT, "Log").click()

# find_element() - returns a multiple webelements
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))

# 2) Locator matching with a multiple webelements
# elements = driver.find_elements(By.XPATH, "//div[@class='header-menu']//a")
# print(len(elements))
#
# print(elements[0].text)
# for element in elements:
#     print(element.text)

# 3) Element not available throws the exception "NoSuchElementException
elements = driver.find_elements(By.LINK_TEXT, "Log")
print(len(elements))

time.sleep(5)
driver.quit()

