# Amazon Product Price Scraper

This project scrapes product prices from Amazon using the Chrome browser with Selenium in Python.

## Requirements

- Python 3.x
- Selenium
- webdriver-manager
- pytest

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/amazon_product_price_scraper.git
    cd amazon_product_price_scraper
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the `amazon_scraper.py` file with the Amazon product URL you want to scrape.

2. Run the script:
    ```bash
    python amazon_scraper.py
    ```

## Running Tests

1. Update the `tests/test_amazon_scraper.py` file with the Amazon product URL you want to scrape.

2. Run the tests:
    ```bash
    pytest
    ```

## Note

Scraping websites may violate the terms of service of the website. Use this script responsibly and only for educational purposes.