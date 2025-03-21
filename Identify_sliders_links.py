from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
driver.maximize_window()

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Close the login popup if it appears
try:
    close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]")))
    close_btn.click()
except:
    print("No login popup found!")

# Wait for sliders to appear and get them
sliders = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._1yQHx8._2UnIQ_._3ak8Rd._2y8Yzt")))

# Wait for all links and fetch them
links = driver.find_elements(By.TAG_NAME, "a")

# Print slider and link details
print(f"There are {len(sliders)} sliders on the webpage..!")
print(f"There are total {len(links)} links on the webpage..!")

# Print first 5 link URLs for verification
for link in links[:5]:
    print(link.get_attribute("href"))

driver.quit()
