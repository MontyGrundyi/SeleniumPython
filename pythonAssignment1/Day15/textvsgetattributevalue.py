from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

driver.get('https://admin-demo.nopcommerce.com/login')
email = driver.find_element(By.XPATH, "//input[@id='Email']")
password = driver.find_element(By.XPATH, "//input[@id='Password']")

email.clear()
password.clear()
email.send_keys('abc@gmail.com')
password.send_keys('admin123')

# print(email.text) # returns inner text payment  if available
# print(email.get_attribute('value')) # returns any value of a web element
# print(password.get_attribute('value'))

button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
print("Result of text:", button.text)
print("Result of get_attribute():", button.get_attribute('type'))
driver.quit()
