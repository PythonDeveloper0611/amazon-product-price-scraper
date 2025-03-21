from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("https://www.instagram.com")
driver.maximize_window()

# Wait for elements to load
time.sleep(5)

# Locate username and password fields (update class names if needed)
username_input = driver.find_element(By.NAME, "username")  # Using NAME instead of CLASS_NAME
password_input = driver.find_element(By.NAME, "password")

# Enter username and password
username_input.send_keys("englishacscentacademy")
password_input.send_keys("*38anDU#")

# Press Enter to log in
password_input.send_keys(Keys.ENTER)

# Wait for login to process
time.sleep(10)

# Close the browser
driver.quit()
