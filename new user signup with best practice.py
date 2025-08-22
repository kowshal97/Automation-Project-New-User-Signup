# register_user.py
# Author: Kowshal Sugunarajah
# Description: Automates the new user registration process on AutomationExercise.com using Selenium.
# Referenced websites: https://automationexercise.com, https://selenium.dev

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_browser():
    """
    Launches Chrome browser using webdriver manager with options.
    Returns:
        driver (WebDriver): An instance of the Chrome WebDriver.
    """
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def verify_homepage(driver):
    """
    Verifies if the homepage has loaded correctly.
    """
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    time.sleep(1)

    try:
        home_banner = driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']")
        if home_banner.is_displayed():
            print("Home page is displayed.")
        else:
            print("Home page is NOT displayed.")
    except Exception as e:
        print(f"Error verifying homepage: {e}")


def fill_signup_form(driver):
    """
    Fills the initial signup form with name and email.
    """
    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("leo")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("leodas@gmail.com")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    time.sleep(3)


def complete_registration_form(driver):
    """
    Completes the detailed registration form including address, date of birth, and preferences.
    """
    # Select gender
    driver.find_element(By.ID, "id_gender1").click()

    # Verify entered data
    assert driver.find_element(By.XPATH, "//input[@value='leo']").is_displayed(), "Name not visible"
    assert driver.find_element(By.XPATH, "//input[@value='leodas@gmail.com']").is_displayed(), "Email not visible"

    # Password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@data-qa='password']"))
    ).send_keys("kowshal123")

    # Date of birth
    Select(driver.find_element(By.ID, "days")).select_by_visible_text("17")
    Select(driver.find_element(By.ID, "months")).select_by_visible_text("November")
    Select(driver.find_element(By.ID, "years")).select_by_visible_text("1997")

    # Preferences
    driver.find_element(By.XPATH, "//label[@for='newsletter']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "optin"))
    ).click()

    # Address
    driver.find_element(By.ID, "first_name").send_keys("leo")
    driver.find_element(By.ID, "last_name").send_keys("das")
    driver.find_element(By.ID, "company").send_keys("Amazon")
    driver.find_element(By.ID, "address1").send_keys("2492 Florentine Place, Pickering")
    driver.find_element(By.ID, "address2").send_keys("Ontario")

    Select(driver.find_element(By.ID, "country")).select_by_visible_text("Canada")
    driver.find_element(By.ID, "state").send_keys("Ontario")
    driver.find_element(By.ID, "city").send_keys("Toronto")
    driver.find_element(By.ID, "zipcode").send_keys("916600")
    driver.find_element(By.ID, "mobile_number").send_keys("64798041119")

    # Submit form
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
    print("Registration form submitted.")


def main():
    """
    Main function to run the automated registration process.
    """
    driver = setup_browser()
    try:
        verify_homepage(driver)
        fill_signup_form(driver)
        complete_registration_form(driver)
    except Exception as e:
        print(f" An error occurred during registration: {e}")


if __name__ == "__main__":
    main()
