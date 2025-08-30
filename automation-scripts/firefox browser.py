from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = "edge"  # change to "firefox" or "edge"

if browser == "chrome":
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

elif browser == "firefox":
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

elif browser == "edge":
    from selenium.webdriver.edge.service import Service
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# ✅ Step 1: Go to Login Page
driver.get("https://demo.automationtesting.in/Index.html")

# ✅ Step 2: Login (to access the register page)
sign_up = driver.find_element(By.ID, "email")
sign_up.send_keys("leo@gmail.com")
driver.find_element(By.ID, "enterimg").click()

# Wait for register page to load
time.sleep(2)

# ✅ Step 3: Fill Registration Form
first_name = driver.find_element(By.XPATH, "//input[@placeholder = 'First Name']")
first_name.send_keys("kowshal")

last_name = driver.find_element(By.XPATH, "//input[@placeholder = 'Last Name']")
last_name.send_keys("sugunarajah")

address = driver.find_element(By.XPATH, "//textarea[@ng-model ='Adress']")
address.send_keys("2492, florentine place, Pickering, Ontario")

email_address = driver.find_element(By.XPATH, "//input[@type = 'email']")
email_address.send_keys("leo@gmail.com")

phone_num = driver.find_element(By.XPATH, "//input[@type ='tel']")
phone_num.send_keys("988888888")

driver.find_element(By.XPATH, "//input[@value ='Male']").click()

# ✅ Step 4: Check only "Cricket"
checkbox = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
for check in checkbox:
    val = check.get_attribute("value")
    if val == "Cricket":
        check.click()

# Wait to observe
time.sleep(10)
