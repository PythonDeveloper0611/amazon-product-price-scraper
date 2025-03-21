from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Ask user to enter credentials
USERNAME = input("Enter your Instagram username: ")
PASSWORD = input("Enter your Instagram password: ")

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
chrome_options.add_argument("--start-maximized")  # Open in maximized window

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# ✅ Wait for username and password fields
wait = WebDriverWait(driver, 15)
username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

# Enter login credentials
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

# ✅ Wait for "Save Login Info" popup and click "Save Info"
try:
    save_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save Info')]")))
    save_login_button.click()
    print("✅ Clicked 'Save Info' successfully!")
except:
    print("⚠️ 'Save Login Info' popup not found or already handled.")

# ✅ Keep the browser open
print("✅ Login successful! Browser will remain open.")
input("Press Enter to close the browser...")
driver.quit()
