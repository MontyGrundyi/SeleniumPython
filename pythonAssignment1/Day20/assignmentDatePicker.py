import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

# Choose the correct option
driver.find_element(By.XPATH, "//input[@id='product_549']").click()

# first name
driver.find_element(By.XPATH, "//input[@id='travname']").send_keys('ABC')
# last name
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys('DEF')


# DOB
driver.find_element(By.XPATH, "//input[@id='dob']").click()

# time.sleep(5)
# Month
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text('Oct')

# Year
datepicker_year = Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]'))
datepicker_year.select_by_visible_text('2001')

# Day
days = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
print(len(days))

for day in days:
    if day.text == '23':
        day.click()
        break

# Gender
driver.find_element(By.XPATH, '//input[@id="sex_1"]').click()

# Number of additional passengers:
# driver.find_element(By.XPATH, '//input[@id="addmorepax"]').click()
# additionalPassenger = Select(driver.find_element(By.XPATH, '//select[@name="addpaxno"]'))
# additionalPassenger.select_by_visible_text('add 1 more passenger (100%)')

# Travel Details
# Trip type
driver.find_element(By.XPATH, '//input[@id="traveltype_1"]').click()

# From city / Origin
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys('NBO')

# Destination
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys('Paris')

# Departure date
driver.find_element(By.XPATH, "//input[@id='departon']").click()

mnth = Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]'))
mnth.select_by_visible_text('Jun')

yr = Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]'))
mnth.select_by_visible_text('2022')

# day
dys = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')

for dy in dys:
    if dy.text == '1':
        dy.click()
        break



