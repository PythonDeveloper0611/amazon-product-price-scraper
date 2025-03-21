import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_amazon_price(url):
    headers = {
        "User-Agent": UserAgent().random,  # Random User-Agent to avoid detection
        "Accept-Language": "en-US,en;q=0.5"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch page. Status Code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Try multiple possible price classes
    price_selectors = [
        "span.a-price-whole",  # Normal price
        "span.a-offscreen",  # Discounted price
        "span#priceblock_ourprice",  # Price for some products
        "span#priceblock_dealprice"  # Deal price
    ]

    price = None
    for selector in price_selectors:
        price_tag = soup.select_one(selector)
        if price_tag:
            price = price_tag.text.strip()
            break

    if price:
        print(f"✅ Mobile Price: ₹{price}")
    else:
        print("❌ Price not found. Check the XPath or product page.")


# 🔹 Replace with actual Amazon product URL
amazon_product_url = "https://amzn.in/d/0KciFeQ"  # Example mobile link
get_amazon_price(amazon_product_url)
