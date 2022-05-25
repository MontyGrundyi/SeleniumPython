from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, '//span[@class="ui-slider-handle ui-corner-all ui-state-default"][1]')
max_slider = driver.find_element(By.XPATH, '//span[@class="ui-slider-handle ui-corner-all ui-state-default"][2]')

print("Location of sliders before moving...............")
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 545, 'y': 250}
