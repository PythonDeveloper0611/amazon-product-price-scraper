from selenium import webdriver
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        product_link = driver.find_element_by_partial_link_text("Laptop")
        product_link.click()
        add_to_cart_button = driver.find_element_by_id("add-to-cart")
        add_to_cart_button.click()
        cart_count = driver.find_element_by_id("cart-count")
        self.assertEqual(cart_count.text, "1")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()