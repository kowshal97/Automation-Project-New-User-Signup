from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Index.html")

email_text = driver.find_element(By.ID, 'email')
email_text.send_keys("leo@gmail.com")
driver.find_element(By.ID, "enterimg").click()

first_name = driver.find_element(By.XPATH,"//input[@placeholder  = 'First Name' ]")
first_name.send_keys("leo")
last_name = driver.find_element(By.XPATH,"//input[@placeholder  = 'Last Name' ]")
last_name.send_keys("luxsi")

#to click any one option like male or female
driver.find_element(By.XPATH,"//input[@value ='Male']" ).click()

#to click any one options from the hobbies
list = driver.find_elements(By.XPATH, "//input[@type ='checkbox']")

#to check any one boxes
for items in list:
    val = items.get_attribute("value")
    print(val)
    if val == "Cricket":
        items.click()
        time.sleep(5)

#to check all the boxes
#interests = ["Movies", "Cricket", "Hockey"]
#for item in interests:
    #driver.find_element(By.XPATH, f"//input[@value='{item}']").click()

time.sleep(5)