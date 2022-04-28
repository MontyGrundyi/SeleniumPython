from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()

# is_displayed() is_enables()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status", search_box.is_displayed())  # True
print("Display Status", search_box.is_enabled())  # True

# is_selected
gender = driver.find_element(By.XPATH, "//div[@id='gender']")
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
# print(gender.is_selected())
print("Default radio button status...")
print("Male Selected:", rd_male.is_selected())  # False
print("Female Selected:", rd_female.is_selected())  # False

rd_male.click()  # Select male radio button
print("After selecting male radio button...")
print("Male radio button", rd_male.is_selected())  # True
print("Female Selected:", rd_female.is_selected())

rd_female.click()  # Select male radio button
print("After selecting female radio button...")
print("Male radio button", rd_male.is_selected())  # False
print("Female Selected:", rd_female.is_selected())  # True

driver.quit()
