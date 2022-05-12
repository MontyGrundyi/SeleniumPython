import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()

# 1. Select specific checkboxes
# driver.find_element(By.XPATH, "//input[@id='monday']").click() # identifying one element

# 2. Selecting multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and  contains(@id,'day')]")
print(len(checkboxes))

# Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach 2
for checkbox in checkboxes:
    checkbox.click()

# 3. Selecting specific checkboxes among multiples
# for checkbox in checkboxes:
#     day_name = checkbox.get_attribute('id')
#     if day_name == 'monday' or day_name == 'sunday':
#         checkbox.click()

# 4. Selecting the last two elements:
# range(5,7) ---> 6,7
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# 5. Selecting the first two elements
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()

time.sleep(5)
# 6. clearing all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


#  Automation framework
# tools = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @class='custom-control-input']")
# print(len(tools))
#
# for i in range(len(tools)):
#     if i < 7:
#         tools[i].click()
