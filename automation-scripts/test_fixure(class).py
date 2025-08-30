import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

@pytest.fixture(scope="class")
def launchbrowser(request):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    request.cls.driver = webdriver.Chrome(service=service)
    yield
    request.cls.driver.quit()

@pytest.mark.usefixtures("launchbrowser")
class test_redbus:
    def test_enterurl(self):
        self.driver.get("https://demo.automationtesting.in/Index.html")
