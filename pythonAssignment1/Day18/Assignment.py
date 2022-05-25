from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_object = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_object)

driver.get('https://testautomationpractice.blogspot.com/')

# close alert window at click me
driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()
alert_window = driver.switch_to.alert
alert_window.accept()


# New window
# driver.switch_to.frame('wikipedia')
driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input').send_keys('selenium')
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()

time.sleep(10)
results = driver.find_elements(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-results"]//a')

print(len(results))


for result in results:
    result.click()

