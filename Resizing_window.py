from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
time.sleep(5)
driver.quit()
