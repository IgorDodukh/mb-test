from datetime import datetime
from pathlib import Path

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from scr.data.constants import ShadowRoot, FuelType, Dir
from scr.pom.locators.configuration_locators import ConfigLocators
from scr.pom.pages.base_page import BasePage


class ConfiguratorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.price_list = None
        self.min_price = None
        self.max_price = None

    def open_fuel_dropdown(self):
        self.wait_for_element_visible(ShadowRoot.CONFIGURATOR)
        shadow_root = self.get_shadow_root(root_type=ShadowRoot.CONFIGURATOR)
        element = shadow_root.find_element(By.CSS_SELECTOR, ConfigLocators.FUEL_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def select_fuel_type(self, fuel_type: FuelType):
        shadow_root = self.get_shadow_root(root_type=ShadowRoot.CONFIGURATOR)
        element = shadow_root.find_element(By.CSS_SELECTOR, ConfigLocators.FUEL_ITEMS.format(fuel_type))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        element.send_keys(Keys.ESCAPE)

    def get_car_prices(self):
        shadow_root = self.get_shadow_root(root_type=ShadowRoot.CONFIGURATOR)
        elements = shadow_root.find_elements(By.CSS_SELECTOR, ConfigLocators.PRICE_LOCATOR)
        self.price_list = list(map(lambda element: int(element.text[1:].replace(",", "")), elements))

    def define_min_price(self):
        self.min_price = min(self.price_list)

    def define_max_price(self):
        self.max_price = max(self.price_list)

    def write_price_results_to_file(self):
        filepath = Path(__file__).parent.parent.parent.parent.joinpath(Dir.ARTEFACTS).joinpath(
            f"{datetime.now()}_price_range.txt")

        with open(filepath.absolute().as_posix(), 'w') as f:
            f.write(f"min_price: {self.min_price}\n")
            f.write(f"max_price: {self.max_price}")

    def filter_by_fuel(self, fuel_type: FuelType):
        self.scroll_page_down()  # using additional scroll because scrollIntoView doesn't always work properly
        self.open_fuel_dropdown()
        self.select_fuel_type(fuel_type)

    def define_boundary_car_prices(self):
        self.get_car_prices()
        self.define_min_price()
        self.define_max_price()
