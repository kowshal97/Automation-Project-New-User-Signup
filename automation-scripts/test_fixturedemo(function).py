import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

@pytest.fixture(scope="function")
def launchbrowser():
    global driver
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    time.sleep(2)
    yield
    driver.quit()



def test_printurl(launchbrowser):
    driver.get("https://demo.automationtesting.in/Index.html")
    print(driver.current_url)

