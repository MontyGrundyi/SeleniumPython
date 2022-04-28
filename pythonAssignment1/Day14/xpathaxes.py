from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self = driver.find_element(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]").text
# print(self)
# driver.close()

# parent
# parent = driver.find_element(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]/ancestor::tr").text
# print(parent)
# driver.close()

# # Descendants
# descendant = driver.find_elements(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]/ancestor::tr/descendant::*")
# print(len(descendant))

# following-sibling
# following_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Bajaj Holdings & "
#                                                    "Inv')]/ancestor::tr/following-sibling::tr")
# print(len(following_sibling))

# following
# following = driver.find_elements(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]/ancestor::tr/following::*")
# print(len(following))

# preceding
# preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]/ancestor::tr/preceding::tr")
# print(len(preceding))

# preceding-sibling
preceding_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'Bajaj Holdings & Inv')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_sibling)) # 77

driver.close()
