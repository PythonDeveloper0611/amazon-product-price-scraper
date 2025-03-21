from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
print("Page Title...", driver.title)
print("Current URL...", driver.current_url)
time.sleep(5)
driver.quit()

