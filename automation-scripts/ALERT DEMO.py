from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome Options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chr_options)

# Step 1: Go to login page
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

# OK Alert
driver.find_element(By.ID, "OKTab").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

# Cancel Alert
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
time.sleep(3)
driver.find_element(By.ID, "CancelTab").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)

# Prompt Alert
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
driver.find_element(By.ID, "Textbox").click()
time.sleep(2)

alert = driver.switch_to.alert  # get full alert object
print(alert.text)
time.sleep(1)
alert.send_keys("leo")  # now send_keys will work correctly
time.sleep(1)
alert.accept()
time.sleep(2)

driver.quit()
