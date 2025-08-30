from selenium import webdriver
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
driver.get("https://demo.automationtesting.in/Index.html")

# Step 2: Enter email and click "Enter"
sign_up = driver.find_element(By.ID, "email")
sign_up.send_keys("leo@gmail.com")
driver.find_element(By.ID, "enterimg").click()

# Optional wait to allow page load
time.sleep(2)

# Step 3: Handle Skills dropdown
dropbox = driver.find_element(By.XPATH, "//select[@id = 'Skills']")
sel = Select(dropbox)

# Select 6th option (index 6 — note: index starts at 0)
#sel.select_by_index(6)
#select by value
#sel.select_by_value("Ruby")
#to select by visisble text
sel.select_by_visible_text("Software")

#to gonew url
driver.get("https://www.google.com/")
#TO GO BACK
driver.back()
#to refresh
driver.refresh()
#to go forword
driver.forward()