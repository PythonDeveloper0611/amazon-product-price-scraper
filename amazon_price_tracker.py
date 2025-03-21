from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from tabulate import tabulate

# ✅ Ask user for product details
product_name = input("Enter the product name: ")
min_price = int(input("Enter the minimum price: "))
max_price = int(input("Enter the maximum price: "))

# ✅ Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ✅ Open Amazon and search for the product
amazon_url = "https://www.amazon.in/"
driver.get(amazon_url)

# ✅ Find search bar and enter product name
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys(product_name)
search_box.send_keys(Keys.RETURN)

# ✅ Wait for products to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot")))

# ✅ Extract product details
products = []
product_elements = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")

for product in product_elements:
    try:
        title = product.find_element(By.CSS_SELECTOR, "h2 a").text
        price_element = product.find_element(By.CSS_SELECTOR, ".a-price-whole")
        price = int(price_element.text.replace(",", ""))  # Convert to int
        link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")

        # ✅ Filter by price range
        if min_price <= price <= max_price:
            products.append([title, price, link])

    except:
        continue  # Skip if price or title is missing

# ✅ Close browser
driver.quit()

# ✅ Save results to an Excel file and display table
if products:
    df = pd.DataFrame(products, columns=["Title", "Price", "Link"])
    df.to_excel("amazon_products.xlsx", index=False)

    print("\n✅ Product details saved to 'amazon_products.xlsx'")
    print("\n📄 Extracted Products:\n")
    print(tabulate(df, headers="keys", tablefmt="grid"))  # Show formatted table
else:
    print("\n⚠️ No products found within the given price range.")
