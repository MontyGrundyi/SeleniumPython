from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

driver.get('https://kenyatalk.com/index.php')
driver.maximize_window()
driver.find_element(By.XPATH, "//span[contains(text(),'New posts')]").click()
links = driver.find_elements(By.XPATH, "//body[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]//a")
print(len(links))

for index, link in enumerate(links):
    # pass
    print(index, link.text)


# def every_second_element(links):
#     second_value = []
#     for i in range(1, len(links), 2):
#         second_value.append(links[i])
#         print(second_value)
#     return second_value
