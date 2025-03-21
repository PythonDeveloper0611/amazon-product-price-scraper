from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
print("Window Size : ", driver.get_window_size())
print("Window Position : ", driver.get_window_position())
time.sleep(5)
driver.quit()

