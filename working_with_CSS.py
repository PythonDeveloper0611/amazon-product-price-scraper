from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")  # Fixed URL format
driver.maximize_window()

# Log in using CSS Selector (ID Method) - Recommended
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("englishacscentacademy")
# driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("*38anDU#")
# driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()

# Log in using CSS Selector (Class Method) - Alternative
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("englishacscentacademy")  # Fixed class selector
driver.find_element(By.CSS_SELECTOR, "input.inputtext[type='password']").send_keys("*38anDU#")  # Select password field correctly
driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()  # Correct button selector

# Wait for the login process to complete
time.sleep(10)  # Adjust time if needed

print("Login attempt completed.")

# Close the browser
driver.quit()
