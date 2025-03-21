import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import config  # Import Amazon login credentials

# Set up Chrome options to avoid detection
chrome_options = Options()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
chrome_options.add_argument("--start-maximized")  # Maximize browser
chrome_options.add_argument("--incognito")  # Use Incognito mode

# Set up WebDriver
service = Service(r"C:\Users\Admin\WebDriver\chromedriver.exe")  # Update your ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)


# Function to perform Amazon login
def amazon_login():
    driver.get('https://www.amazon.com/')
    time.sleep(5)

    try:
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ap_email')))
        email_input.send_keys(config.AMAZON_EMAIL)
        driver.find_element(By.ID, 'continue').click()
        time.sleep(2)

        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ap_password')))
        password_input.send_keys(config.AMAZON_PASSWORD)
        driver.find_element(By.ID, 'signInSubmit').click()
        time.sleep(5)

        print("✅ Logged in successfully!")
    except Exception as e:
        print(f"❌ Error during login: {e}")


# Function to solve CAPTCHA manually
def solve_captcha():
    try:
        if "auth-captcha-guess" in driver.page_source:
            captcha_input = input("🔴 Enter CAPTCHA manually: ")
            captcha_field = driver.find_element(By.ID, 'auth-captcha-guess')
            captcha_field.send_keys(captcha_input)
            driver.find_element(By.ID, 'signInSubmit').click()
            time.sleep(10)
    except Exception:
        print("✅ No CAPTCHA detected.")


# Function to scrape product details
def scrape_product_details(url):
    driver.get(url)
    time.sleep(3)  # Wait for initial load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()
    except:
        title = "Title not found"

    try:
        price = driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
    except:
        price = "Price not available"

    try:
        reviews = driver.find_element(By.ID, "acrCustomerReviewText").text.strip()
    except:
        reviews = "No reviews"

    try:
        availability = driver.find_element(By.ID, "availability").text.strip()
    except:
        availability = "Availability unknown"

    return title, price, reviews, availability


# Function to store data in SQLite database
def store_data(title, price, reviews, availability):
    connection = sqlite3.connect('amazon_scraper.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        price TEXT NOT NULL,
                        reviews TEXT NOT NULL,
                        availability TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    cursor.execute("INSERT INTO products (title, price, reviews, availability) VALUES (?, ?, ?, ?)",
                   (title, price, reviews, availability))

    connection.commit()
    cursor.close()
    connection.close()


# Function to retrieve and display stored data
def display_stored_data():
    connection = sqlite3.connect('amazon_scraper.db')
    cursor = connection.cursor()

    cursor.execute("SELECT title, price, reviews, availability, created_at FROM products ORDER BY created_at DESC")
    rows = cursor.fetchall()

    print("\n📢 Stored Product Data:")
    for row in rows:
        print("🔹 Title:", row[0])
        print("   💰 Price:", row[1])
        print("   ⭐ Reviews:", row[2])
        print("   🛒 Availability:", row[3])
        print("   ⏳ Added On:", row[4])
        print("-" * 80)

    cursor.close()
    connection.close()


# Main function
def main():
    amazon_login()
    solve_captcha()

    product_urls = [
        'https://amzn.in/d/3TVn2aU',
        'https://amzn.in/d/ej78LcR',
        'https://amzn.in/d/2uMp6ss',
        'https://amzn.in/d/7wb2I2G'
    ]

    for url in product_urls:
        title, price, reviews, availability = scrape_product_details(url)
        store_data(title, price, reviews, availability)
        print(f"✅ Scraped and stored: {title} - Price: {price}")

    display_stored_data()  # Show stored data on screen

    driver.quit()
    print("🚀 Scraping completed!")


if __name__ == '__main__':
    main()
