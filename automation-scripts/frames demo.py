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
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

#switching to frames
driver.switch_to.frame(0)

#to find using id or name
driver.switch_to.frame("singleframe")
driver.switch_to.frame("SingleFrame")

single_frame = driver.find_element(By.XPATH , "//div[@id='Single']/iframe")
driver.switch_to.frame(single_frame)

text = driver.find_element(By.TAG_NAME, "input")
text.send_keys("leodas")
