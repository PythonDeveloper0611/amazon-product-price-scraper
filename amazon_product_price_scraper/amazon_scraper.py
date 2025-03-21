import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_amazon_price(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.headless = False  # Set headless to False

    # Set up Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the Amazon product page
        driver.get(url)

        # Wait for the price element to load
        wait = WebDriverWait(driver, 10)

        # Try different strategies to find the price element
        price_element = None
        price_ids = ["priceblock_ourprice", "priceblock_dealprice", "price_inside_buybox"]
        
        for price_id in price_ids:
            try:
                price_element = wait.until(EC.presence_of_element_located((By.ID, price_id)))
                if price_element:
                    break
            except:
                continue

        if not price_element:
            raise Exception("Price element not found")

        # Extract the price text
        price = price_element.text

        return price
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python amazon_scraper.py <Amazon product URL>")
        sys.exit(1)

    product_url = sys.argv[1]
    price = get_amazon_price(product_url)

    if price:
        print(f"The price of the product is: {price}")
    else:
        print("Failed to retrieve the price.")