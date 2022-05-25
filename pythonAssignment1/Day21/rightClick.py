# Right click

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

act = ActionChains(driver)
button = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")

act.context_click(button).perform()
