from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://kenyatalk.com/index.php')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="top"]/div[1]/nav/div/div[3]/div[1]/a[1]/span').click()
driver.find_element(By.NAME, 'login').send_keys('gsolomon186@gmail.com')
driver.find_element(By.ID, '_xfUid-2-1650358621').send_keys('Alfedok@uon')
driver.find_element(By.XPATH, '//*[@id="js-XFUniqueId118"]/div/div[2]/div/form/div[1]/dl/dd/div/div[2]/button/span').click()
