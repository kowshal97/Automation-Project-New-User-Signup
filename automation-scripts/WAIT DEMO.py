from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chr_options)

# Step 1: Go to login page
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()



driver.find_element(By.ID,"email").send_keys("kowshal@gmail.com")
driver.find_element(By.ID,"enterimg").click()

#wait sleep
#time.sleep(2)

#wait implicit wait - implicit waiting,webdriver polls the DOM webpage
#where are not available immediately and need some time to load
driver.implicitly_wait(3)

#wait explicit wait - hey allow your code to halt program execution
#will make some time to load
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='First Name']"))).send_keys("kowshal")


