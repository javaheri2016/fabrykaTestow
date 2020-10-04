import unittest
from selenium import webdriver
from homeworks.taps_shop.config.test_settings import TestSettings
from homeworks.taps_shop.tests.page_objects import main_page, cart_page, order_page
import time


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process_correct(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.submitted_order(self.driver))

    def test2_process_incorrect_data(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.incorrect_email_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_page.incorrect_data_error(self.driver))


if __name__ == '__main__':
    unittest.main()
