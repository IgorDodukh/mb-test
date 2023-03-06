from selenium.webdriver.common.by import By

from scr.data.constants import ShadowRoot
from scr.pom.locators.model_locators import ModelLocators
from scr.pom.pages.base_page import BasePage


class ModelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_title(self):
        self.wait_for_element_presence(ShadowRoot.MODEL_PAGE)
        shadow_root = self.get_shadow_root(root_type=ShadowRoot.MODEL_PAGE)
        return shadow_root.find_element(By.CSS_SELECTOR, ModelLocators.PAGE_TITLE).text

    def select_build_your_car_button(self):
        shadow_root = self.get_shadow_root(root_type=ShadowRoot.MODEL_PAGE)
        element = shadow_root.find_element(By.CSS_SELECTOR, ModelLocators.BUILD_YOUR_CAR_BUTTON)
        element.click()
