from selenium.webdriver.common.by import By

from scr.pom.locators.home_locators import HomeLocators
from scr.pom.pages.base_page import BasePage
from scr.data.constants import MainMenu, OurModelsMenu, ShadowRoot, HatchMenu, Menu, Const


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_cookies_banner(self):
        self.wait_for_element_presence(ShadowRoot.COOKIE_BANNER)
        shadow_root = self.get_shadow_root(ShadowRoot.COOKIE_BANNER)
        element = shadow_root.find_element(By.CSS_SELECTOR, HomeLocators.ACCEPT_COOKIES_BUTTON)
        element.click()

    # TODO: optimise methods below into a single method by creating a mapping between menu type and related locators

    def select_menu(self, menu_item: MainMenu):
        shadow_root = self.get_shadow_root(ShadowRoot.MENU)
        element = shadow_root.find_element(By.CSS_SELECTOR, HomeLocators.MAIN_MENU.format(menu_item))
        element.click()

    def select_submenu(self, menu_item: OurModelsMenu):
        shadow_root = self.get_shadow_root(ShadowRoot.SUB_MENU)
        element = shadow_root.find_element(By.CSS_SELECTOR, HomeLocators.OUR_MODELS_MENU.format(menu_item))
        element.click()

    def select_sub_model_menu(self, menu_item: HatchMenu):
        shadow_root = self.get_shadow_root(ShadowRoot.SUB_MENU)
        element = shadow_root.find_element(By.CSS_SELECTOR, HomeLocators.SUB_MODELS_LIST.format(menu_item))
        element.click()
