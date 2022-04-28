from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()

# Relative path driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys('T-Shirt')
# driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys('T-Shirt') # or
# operator

driver.find_element(By.XPATH, "//input[@id='search_query_top' and @name='search_query']") # or operator
driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()
driver.close()


