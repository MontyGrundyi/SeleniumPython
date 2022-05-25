from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

# DOB
driver.find_element(By.XPATH, '//input[@id="dob"]').click()  # Opens date picker element

datePickerMonth = Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]'))
datePickerMonth.select_by_visible_text('Dec')  # Month

datePickerYear = Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]'))
datePickerYear.select_by_visible_text('1998')

# day
days = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]//tbody/tr/td/a')
print(len(days))

for day in days:
    if day.text == "31":
        day.click()
        break
