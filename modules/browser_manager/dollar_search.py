from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from .chrome_manager import ChromeBrowserManager

class DollarSearchAutomation(ChromeBrowserManager):
  def search(self, query: str) -> None:
        self.open_site('https://www.google.com')
        input_text = self.find_element(By.NAME, 'q')
        input_text.send_keys(query)
        input_text.send_keys(Keys.ENTER)

        response_element = None
        try:
          response_element = self.find_dynamic_element(
              By.CSS_SELECTOR,
              '#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt > span.DFlfde.SwHCTb'
          )
        except TimeoutException:
          print('Não foi possível encontrar um resultado')

        if response_element is not None:
           print(response_element.text)