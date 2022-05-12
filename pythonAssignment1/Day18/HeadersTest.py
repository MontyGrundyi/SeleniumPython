from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

menu = driver.find_elements(By.XPATH, '//div[@class="header-menu"]//a')
for item in menu:
    if item.text == 'Books':
        item.click()


