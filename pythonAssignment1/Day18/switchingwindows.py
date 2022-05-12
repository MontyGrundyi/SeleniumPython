from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
window_IDs = driver.window_handles

# Approach 1
# parent_windowID = window_IDs[0]
# child_windowID = window_IDs[1]
#
# print('Parent window ID', parent_windowID)  # 25D5084A440D036342DD6FCAAE2841D1
# print('Child window ID', child_windowID)  # F18FD50AE67EAFB66A268C1081698F27
#
# driver.switch_to.window(child_windowID)
# print('Child window title', driver.title)
#
# driver.switch_to.window(parent_windowID)
# print('Child window title', driver.title)
#
# driver.close()

# Approach 2
# for winID in window_IDs:
#     driver.switch_to.window(winID)
#     print(driver.title)

# Closing specific browser windows

for winID in window_IDs:
    driver.switch_to.window(winID)
    if driver.title == 'OrangeHRM':
        driver.close()
