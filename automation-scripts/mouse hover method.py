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

# Chrome Options
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chr_options)

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

# Wait and hover on "Men"
men = wait.until(EC.visibility_of_element_located((By.ID, "ui-id-5")))
action.move_to_element(men).perform()

# Wait and hover on "Tops"
tops = wait.until(EC.visibility_of_element_located((By.ID, "ui-id-17")))
action.move_to_element(tops).perform()

# Wait and click "Jackets"
jackets = wait.until(EC.visibility_of_element_located((By.ID, "ui-id-19")))
action.move_to_element(jackets).click().perform()
time.sleep(3)

search = driver.find_element(By.ID, "search")
action.click(search).key_down(Keys.SHIFT).send_keys("clothes").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()