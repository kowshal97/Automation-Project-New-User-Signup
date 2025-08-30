from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains,Keys
import time

from weblib.selenium_tools import click

# Chrome Options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chr_options)

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

select_date = "20-dec-2022"
dates = select_date.split("-")
driver.find_element(By.ID,"onward_call").click()
td = driver.find_elements(By.XPATH, "//div[@id = 'rb-calendar_onward_cal']//td")

for ele in td:
    if ele.text == dates[0]:
        ele.click()
        break