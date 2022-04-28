from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.google.com/')
driver.maximize_window()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Selenium")
search_box.submit()
