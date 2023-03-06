from datetime import datetime
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scr.data.constants import ShadowRoot, Dir


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element_presence(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def get_shadow_root(self, root_type: ShadowRoot):
        """
        To find and debug locators for shadow-root in browser use console with the query below:
        document.querySelector('{SHADOW_ROOT_LOCATOR}').shadowRoot.querySelector('{WEB_ELEMENT_LOCATOR}')
        """
        return self.driver.execute_script(f"return document.querySelector('{root_type}').shadowRoot")

    def save_full_page_screenshot(self):
        """
        Better works in headless mode. Selenium will take a screenshot of the full current page.
        NOT RECOMMENDED to use on the big web pages. Screenshot size might be too big.
        """
        body_height = self.driver.execute_script('return document.body.scrollHeight')
        self.driver.set_window_size(1920, body_height)
        path = Path(__file__).parent.parent.parent.parent.joinpath(Dir.ARTEFACTS).joinpath(
            f"{datetime.now()}_result.jpg")
        self.driver.save_screenshot(path.absolute().as_posix())
        self.driver.set_window_size(1920, 1080)
