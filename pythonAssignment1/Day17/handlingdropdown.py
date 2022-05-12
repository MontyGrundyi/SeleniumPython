import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

dropdown_element = driver.find_element(By.ID, 'input-country')
drop_down = Select(dropdown_element)

#  selecting an option from the dropdown
# drop_down.select_by_visible_text('Togo') # most preferred method
# drop_down.select_by_value('211')
# drop_down.select_by_index('211')

# Capture all the options and print them
all_options = drop_down.options
print(len(all_options))

# for count, option in enumerate(all_options):
#     print(count, option.text)

# Select an option without using a built-in method

for option in all_options:
    if option == 'Kenya':
        option.click()
        break



# alloptions = driver.find_elements(By.XPATH, '//*[@id="input-country"]/option')

# time.sleep(5)
# driver.quit()
