from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class SearchProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_search_product(self):
        driver = self.driver
        driver.get("https://www.flipkart.com/")
        self.assertIn("E-commerce", driver.title)
        search_box = driver.find_element_by_name("search")
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()