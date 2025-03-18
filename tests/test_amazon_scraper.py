import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def browser():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    yield driver
    
    # Close the browser
    driver.quit()

def test_amazon_price_scraper(browser):
    product_url = "https://amzn.in/d/gC1Ice1"  # Replace this with the Amazon product URL you want to scrape

    # Open Amazon product page
    browser.get(product_url)

    # Wait for the page to load
    time.sleep(10)

    # Find the price element
    price_element = browser.find_element(By.ID, "priceblock_ourprice")
    price = price_element.text

    # Check if the price is not empty
    assert price != "", "Price should not be empty"