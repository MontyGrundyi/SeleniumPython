from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
links = driver.find_elements(By.TAG_NAME, 'a')

print(len(sliders))  # Total number of sliders
print(len(links))  # total number of links
driver.close()
