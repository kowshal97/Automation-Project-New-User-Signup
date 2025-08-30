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
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

parent = driver.current_window_handle
print(parent)
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()

#To find how many child windows are there
win = driver.window_handles
for window in win:
    print(window)
    if window!=parent:
        driver.switch_to.window(window)
driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()
time.sleep(2)
driver.close()
driver.quit()