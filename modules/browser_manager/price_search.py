from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from typing import List

from time import sleep

from .chrome_manager import ChromeBrowserManager


class PriceSearchAutomation(ChromeBrowserManager):
    def extract_product_details(self, product_card: WebElement) -> List[str]:
        name = price = shop = None
        if product_card.get_attribute('class') == 'ljqwrc':
            try:
                name = product_card.find_element(
                    By.CSS_SELECTOR, 'h3.sh-np__product-title'
                ).text
            except NoSuchElementException:
                name = 'N/A'

            try:
                price = product_card.find_element(
                    By.CSS_SELECTOR, 'span.T14wmb > b'
                ).text
            except NoSuchElementException:
                price = 'N/A'

            try:
                shop = product_card.find_element(
                    By.CSS_SELECTOR, 'div.sh-np__seller-container > span.E5ocAb'
                ).text
            except NoSuchElementException:
                shop = 'N/A'

        elif product_card.get_attribute('class') == 'sh-dgr__content':
            try:
                name = product_card.find_element(
                    By.CSS_SELECTOR, 'h3.tAxDx').text
            except NoSuchElementException:
                name = 'N/A'

            try:
                price = product_card.find_element(
                    By.CSS_SELECTOR, 'span.a8Pemb').text
            except NoSuchElementException:
                price = 'N/A'

            try:
                shop = product_card.find_element(
                    By.CSS_SELECTOR, 'div.aULzUe').text
            except NoSuchElementException:
                shop = 'N/A'

        return [name, price, shop]

    def get_all_products(self) -> List[List[str]]:
        sponsored_products = self.find_dynamic_elements(
            By.CSS_SELECTOR, '.ljqwrc'
        )

        if (len(sponsored_products) > 0):
            sponsored_product_details = [
                self.extract_product_details(product)
                for product in sponsored_products
            ]
        else:
            sponsored_product_details = []

        other_products = self.find_dynamic_elements(
            By.CSS_SELECTOR, '.sh-dgr__content'
        )
        other_product_details = [
            self.extract_product_details(product)
            for product in other_products
        ]

        return sponsored_product_details + other_product_details

    def search_product(self, query) -> List[List[str]]:
        self.open_site('https://www.google.com')
        input_text = self.find_element(By.NAME, 'q')
        input_text.send_keys(query)
        input_text.send_keys(Keys.ENTER)

        try:
            shopping_el = self.find_dynamic_element(
                By.XPATH,
                "//div[@class='crJ18e']//div[@role='listitem']//a[contains(., 'Shopping')]"
            )
            shopping_el.click()
            # input()
        except TimeoutException:
            print('Shopping element not found')
            self.close_browser()
            return

        return self.get_all_products()
