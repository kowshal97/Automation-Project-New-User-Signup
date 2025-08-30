from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chr_options = Options()
chr_options.add_experimental_option("detach", True)
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Index.html")

#login page
sign_up = driver.find_element(By.ID, "email")
sign_up.send_keys("leo@gmail.com")
driver.find_element(By.ID, "enterimg").click()

#register page
first_name = driver.find_element(By.XPATH, "//input[@placeholder = 'First Name' ]")
first_name.send_keys("kowshal")
last_name = driver.find_element(By.XPATH, "//input[@placeholder = 'Last Name' ]")
last_name.send_keys("sugunarajah")
address = driver.find_element(By.XPATH, "//textarea[@ng-model ='Adress' ]")
address.send_keys("2492,florentine place ,pickering,ontario")
email_address = driver.find_element(By.XPATH, "//input[@type = 'email']")
email_address.send_keys("leo@gmail.com")
phone_mum = driver.find_element(By.XPATH, "//input[@type ='tel']")
phone_mum.send_keys("988888888")
driver.find_element(By.XPATH, "//input[@value ='Male']").click()

checkbox = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
for check in checkbox:
    val = check.get_attribute("value")
    if val == "Cricket":
        check.click()


time.sleep(10)