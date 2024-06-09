from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pathlib import Path
from typing import List, Optional


ROOT_FOLDER = Path(__file__).parent.parent.parent
CHROMEDRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


class ChromeBrowserManager:
    def __init__(self, *options: str):
        self.browser = self.make_chrome_browser(*options)

    def make_chrome_browser(self, *options: str) -> webdriver.Chrome:
        chrome_options = webdriver.ChromeOptions()

        if options is not None:
            for option in options:
                chrome_options.add_argument(option)

        chrome_service = Service(
            executable_path=CHROMEDRIVER_PATH,
        )

        browser = webdriver.Chrome(
            service=chrome_service,
            options=chrome_options
        )

        return browser

    def open_site(self, url: str) -> None:
        self.browser.get(url)

    def close_browser(self) -> None:
        self.browser.quit()

    def find_element(self, by: By, value: str) -> WebElement:
        return self.browser.find_element(by, value)
    
    def find_elements(self, by: By, value: str) -> List[WebElement]:
        return self.browser.find_elements(by, value)

    from selenium.common.exceptions import TimeoutException

    def find_dynamic_element(self, by: By, value: str, timeout: int = 5) -> Optional[WebElement]:
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return None

    def find_dynamic_elements(self, by: By, value: str, timeout: int = 5) -> List[WebElement]:
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
        except TimeoutException:
            return []


    def wait(self, seconds: int) -> None:
        self.browser.implicitly_wait(seconds)
