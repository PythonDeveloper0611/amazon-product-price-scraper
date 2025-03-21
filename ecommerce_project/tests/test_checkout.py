from selenium import webdriver
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_checkout(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        product_link = driver.find_element_by_partial_link_text("mobile")
        product_link.click()
        add_to_cart_button = driver.find_element_by_id("add-to-cart")
        add_to_cart_button.click()
        checkout_button = driver.find_element_by_id("checkout")
        checkout_button.click()
        self.assertIn("Order Summary", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()