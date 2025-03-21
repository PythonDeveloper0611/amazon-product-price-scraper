from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.co.in")
    driver.maximize_window()
    time.sleep(15)  # Allow page to load

    # Find the search box and enter text
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Automation with Python")

    # Press Enter after typing
    search_box.send_keys(Keys.RETURN)

    time.sleep(15)  # Allow time for results to load

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Ensure WebDriver quits properly
    driver.quit()
    print("Driver closed successfully.")
