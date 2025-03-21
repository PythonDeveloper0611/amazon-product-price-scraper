from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver service
service = Service("C:\\Users\\Admin\\PycharmProjects\\MyProjects\\chromedriver.exe")

# Set up Chrome options
options = Options()
options.headless = False  # Set to True for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.naukri.com")  # Replace with the target URL
print("Page title:", driver.title)

# Add any scraping logic here

# Keep the browser open for 10 seconds before closing
time.sleep(10)
driver.quit()
