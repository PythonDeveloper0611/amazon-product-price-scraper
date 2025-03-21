from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.get("https://www.instagram.com")
driver.back()
driver.forward()
driver.refresh()
time.sleep(10)
driver.quit()
print("Performed two operations.")
print("Chrome browser was opened, opened Facebook page, moved to Instagram website, returned to Facebook website...")
print("and finally landed on Instagram Website, waited for 10 seconds and closed!")