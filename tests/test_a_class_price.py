import pytest

from scr.data.constants import MainMenu, ModelsMenu, HatchMenu, FuelType
from scr.data.test_data import PriceRange
from scr.pom.pages.configurator_page import ConfiguratorPage
from scr.pom.pages.home_page import HomePage
from scr.pom.pages.model_page import ModelPage


class TestAClassPrice:

    @pytest.fixture(autouse=True)
    def pre_test(self, browser):
        self.home_page = HomePage(browser)
        self.config_page = ConfiguratorPage(browser)
        self.model_page = ModelPage(browser)
        self.home_page.close_cookies_banner()

    def test_validate_a_class_price(self):
        self.home_page.select_menu(MainMenu.OUR_MODELS)
        self.home_page.select_submenu(ModelsMenu.HATCHBACKS)
        self.home_page.select_sub_model_menu(HatchMenu.A_CLASS)

        actual_title = self.model_page.get_page_title()
        assert actual_title == "The new A-Class Hatchback", f"Page title '{actual_title}' does not match expected"

        self.model_page.select_build_your_car_button()
        self.config_page.filter_by_fuel(FuelType.DIESEL)

        self.config_page.save_full_page_screenshot()
        self.config_page.define_boundary_car_prices()
        self.config_page.write_price_results_to_file()

        assert self.config_page.max_price <= PriceRange.MAX_EXPECTED, f"Current max price exceeds expected price range"
        assert self.config_page.min_price >= PriceRange.MIN_EXPECTED, f"Current min price exceeds expected price range"
