from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demo.automationtesting.in/Index.html")

#locators
#By.ID
#By.NAME
#BY.TAGNAME
#By.CSS_SELECTOR
#By.CLASS_NAME
#By.LINK_TEXT
#.partial_link_text
#By.xpath

email_text = driver.find_element(By.ID,"email")
email_text.send_keys("test@gmail.com")
driver.find_element(By.ID,"enterimg").click()

time.sleep(10)