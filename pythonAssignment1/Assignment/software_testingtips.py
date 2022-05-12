from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--disable-notifications')

serv_obj = Service("C:/Users/okumue/Downloads/chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj, chrome_options=option)

driver.get('https://www.softwaretestinghelp.com/test-automation-interview-questions/')

questions = driver.find_elements(By.XPATH, "//*[contains(text(),'Q #')]")
print(len(questions))

for question in questions:
    print(question.text)

driver.quit()
