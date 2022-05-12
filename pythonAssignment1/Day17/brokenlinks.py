# We need to install requests package through File --->Settings--->Project interpreter--->

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in all_links:
    url = link.get_attribute('href')  # gives url
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, ' is a broken link')
        count += 1
    else:
        print(url, ' Is a valid link')

print('Total number of broken links:', count)
