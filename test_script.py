from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")

    driver.find_element(By.ID, "email").send_keys("chandu.chilukamary@gmail.com")
    driver.find_element(By.NAME, "pass").send_keys("*38anDU#")
    driver.find_element(By.NAME, "login").click()

    time.sleep(10)  # Wait for page to load after login (better to use WebDriverWait)
    
    assert "login" not in driver.current_url  # Ensure we are not on the login page

    driver.quit()
