import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import os

location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')

    # Download files in the desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver  # enables us to call the driver instance outside the function


my_driver = chrome_setup()
my_driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
my_driver.maximize_window()
time.sleep(5)
alert = my_driver.switch_to.alert
alert.dismiss()
my_driver.implicitly_wait(10)
my_driver.find_element(By.XPATH, '//*[@id="table-files"]/tbody/tr[1]/td[5]/a').click()
