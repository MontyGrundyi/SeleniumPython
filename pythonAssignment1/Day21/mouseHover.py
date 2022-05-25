from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

# Login
driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
driver.find_element(By.ID, 'btnLogin').click()

act = ActionChains(driver)

admin = act.move_to_element(driver.find_element(By.XPATH, "//b[contains(text(),'Admin')]")).click().perform()
usermgmt = act.move_to_element(driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")).click().perform()
users = act.move_to_element(driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")).click().perform()

