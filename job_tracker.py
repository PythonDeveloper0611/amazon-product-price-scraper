import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium ChromeDriver with WebDriver Manager
chrome_options = Options()
# REMOVE headless mode for debugging
# chrome_options.add_argument("--headless")  # Comment this out to see the browser
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
chrome_options.add_argument("--window-size=1920,1080")  # Ensure elements load properly

service = Service(ChromeDriverManager().install())  # Auto-download ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)  # Explicit wait

# Naukri Job Search URL
SEARCH_TERM = "Data Analyst"
LOCATION = "Hyderabad"
URL = f"https://www.naukri.com/{SEARCH_TERM.replace(' ', '-')}-jobs-in-{LOCATION.lower()}"

print(f"🔍 Fetching jobs from: {URL}")
driver.get(URL)
time.sleep(5)  # Wait for page load

# Debug: Save the page source to check the job listing class names
with open("naukri_page.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)
print("📄 Page source saved to naukri_page.html. Check for correct class names.")

# Scroll to load more jobs
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Find job listings
jobs = []
try:
    # ✅ UPDATED: Use XPath instead of class name
    job_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[contains(@class, 'jobTuple')]")))
    print(f"✅ Found {len(job_cards)} jobs on the page.")

    for job in job_cards[:10]:  # Scrape top 10 job listings
        try:
            title = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").text
            company = job.find_element(By.XPATH, ".//a[contains(@class, 'comp-name')]").text
            location = job.find_element(By.XPATH, ".//li[contains(@class, 'location')]").text
            link = job.find_element(By.XPATH, ".//a[contains(@class, 'title')]").get_attribute("href")
            jobs.append([title, company, location, link])
        except Exception as e:
            print(f"⚠️ Error extracting job details: {e}")
            continue
except Exception as e:
    print(f"❌ No jobs found or error: {e}")

# Save to CSV
csv_filename = "naukri_job_listings.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])
    writer.writerows(jobs)

print(f"\n✅ Job listings saved to {csv_filename}\n")

# Read and Print CSV Data
print("📄 Extracted Job Listings:\n")
with open(csv_filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Close the browser
driver.quit()
