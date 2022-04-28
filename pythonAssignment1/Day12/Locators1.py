from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() # Maximize browser window

# id & name locators
# driver.find_element(By.ID, "small-searchterms").send_keys('Lenovo Thinkpad X1 Carbon Laptop')
# driver.find_element(By.NAME, "q").send_keys('Lenovo Thinkpad X1 Carbon Laptop')
# driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()

# link text & partial link text

# driver.find_element(By.LINK_TEXT, 'Register').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Reg').click()

driver.close()
# driver.quit()
