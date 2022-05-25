import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

# Login
driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()
time.sleep(3)

# Admin -->user management --> users
driver.find_element(By.ID, 'menu_admin_viewAdminModule').click()
driver.find_element(By.ID, 'menu_admin_UserManagement').click()
driver.find_element(By.ID, 'menu_admin_viewSystemUsers').click()

#  Total rows in the table
noOfRows = len(driver.find_elements(By.XPATH, '//table[@id="resultTable"]//tbody//tr'))
print('total number of rows in the table', noOfRows)

for r in range(1, noOfRows+1):
    role = driver.find_element(By.XPATH, '//table[@id="resultTable"]//tbody/tr['+str(r)+']/td[3]').text
    username = driver.find_element(By.XPATH, '//table[@id="resultTable"]//tbody/tr['+str(r)+']/td[2]').text
    if role == 'ESS':
        print(username, '              ', role)
    # print(' ')
