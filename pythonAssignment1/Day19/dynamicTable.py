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

count = 0
for r in range(1, noOfRows+1):
    status = driver.find_element(By.XPATH, '//table[@id="resultTable"]//tbody//tr['+str(r)+']/td[5]').text
    print(status)
    if status == 'Enabled':
        count += 1

print('Total number of users:', noOfRows)
print('Number of enables users:', count)
print('Number of disabled users:', (noOfRows - count))

driver.close()





