from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_object = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_object)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# 1. No. of rows and columns
# no. of rows
noOfRows = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr'))
noOfColumns = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]//th'))
print(noOfRows)  # 7
print(noOfColumns)  # 4

# 2. Read specific row abd column
# masterInSelenium = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[5]/td[1]').text
# print(masterInSelenium)

# 3. Read all rows and columns
# dynamic extract:
# for r in range(2, noOfRows+1):
#     for c in range(1, noOfColumns+1):
#         data = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr['+str(r)+']/td['+str(c)+']').text
#         print(data, end='           ')   # prints all data in a row
#     print()


# 4. Read data based on condition(list book name whose author is mukesh)

for r in range(2, noOfRows + 1):
    authorName = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[2]').text
    if authorName == 'Mukesh':
        bookName = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[' + str(r) + ']/td[1]').text
        print(bookName, '     ', authorName)

driver.close()
