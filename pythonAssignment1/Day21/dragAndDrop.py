from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/okumue/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()

# Rome/Italy
source_element = driver.find_element(By.XPATH, '//div[@id="box6"]')
target_element = driver.find_element(By.ID, "box106")

# Stockholm/Sweden
source_element1 = driver.find_element(By.ID, "box2")
target_element1 = driver.find_element(By.ID, "box102")

# Spain/Madrid
source_element2 = driver.find_element(By.ID, "box7")
target_element2 = driver.find_element(By.ID, "box107")

# Norway/Oslo
source_element3 = driver.find_element(By.ID, "box1")
target_element3 = driver.find_element(By.ID, "box101")

# Denmark/Copenhagen
source_element4 = driver.find_element(By.ID, "box4")
target_element4 = driver.find_element(By.ID, "box104")

# South Korea/Seoul
source_element5 = driver.find_element(By.ID, "box5")
target_element5 = driver.find_element(By.ID, "box105")

# United States/Washington
source_element6 = driver.find_element(By.ID, "box3")
target_element6 = driver.find_element(By.ID, "box103")

act = ActionChains(driver)
act.drag_and_drop(source_element, target_element).perform() # drag and drop operation
act.drag_and_drop(source_element1, target_element1).perform()
act.drag_and_drop(source_element2, target_element2).perform()
act.drag_and_drop(source_element3, target_element3).perform()
act.drag_and_drop(source_element4, target_element4).perform()
act.drag_and_drop(source_element5, target_element5).perform()
act.drag_and_drop(source_element6, target_element6).perform()





