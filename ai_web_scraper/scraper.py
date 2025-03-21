from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

print("Initializing WebDriver...")  # Debugging

# Set up Chrome WebDriver service
service = Service("C:\\Users\\Admin\\PycharmProjects\\MyProjects\\chromedriver.exe")

# Set up Chrome options
options = Options()
options.headless = False  # Set to True for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)
print("WebDriver started successfully!")

# Open website
url = "https://www.naukri.com"  # Replace with the target URL
print(f"Opening website: {url}")
driver.get(url)

print("Page title:", driver.title)

# Keep the browser open for 10 seconds before closing
time.sleep(10)
driver.quit()
print("WebDriver closed successfully!")
