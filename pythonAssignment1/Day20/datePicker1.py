import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()

driver.switch_to.frame(0) # switch to frame
# mm/dd/yyyy passing date using send keys

# driver.find_element(By.XPATH, '//input[@id="datepicker"]').send_keys('09/30/2021')

year = '1988'
month = 'December'
day = '29'

# Click on the datepicker
driver.find_element(By.XPATH, '//input[@id="datepicker"]').click()

while True:
    mon = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-month"]').text
    yr = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-year"]').text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH, '//span[contains(text(),"Next")]').click()  # Next arrow
        driver.find_element(By.XPATH, '//span[contains(text(),"Prev")]').click()  # Prev arrow

# Select date
dates = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]//tbody//tr/td/a')

for elem in dates:
    if elem.text == day:
        elem.click()
        break

