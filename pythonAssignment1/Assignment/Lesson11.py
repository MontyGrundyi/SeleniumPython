# 1. Open a Web Browser(Chrome/firefox/IE).
# 2. Open the URL https://admin-demo.nopcommerce.com/login
# 3. Provide an Email (admin@yourstore.com).
# 4. Provide the password (admin)
# 4. Click on Login.
# 5. Capture the title of the dashboard page(Actual title).
# 6. Verify title of the page: "Dashboard / nopCommerce" (Expected).
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj = Service("C:/Users/okumue/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://admin-demo.nopcommerce.com/login')
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys('admin@yourstore.com')
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys('admin')
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

actual_title = driver.title
expected_title = 'Dashboard / nopCommerce administration'

if actual_title == expected_title:
    print("Login test passed")
else:
    print("Login test failed")

driver.close()