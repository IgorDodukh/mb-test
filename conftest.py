import os
import time
from datetime import datetime
from pathlib import Path

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from scr.data.constants import Dir, SupportedBrowser


@pytest.fixture(scope="session")
def browser(request):
    driver = define_browser(request)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def define_browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == SupportedBrowser.CHROME:
        options = Options()
        options.headless = True
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == SupportedBrowser.FIREFOX:
        # TODO: did not complete debug for Firefox. Can't handle shadow root properly.
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise KeyError(f"Web Browser '{browser_name}' is not supported now.")


@pytest.fixture(autouse=True, scope="function")
def open_homepage(browser):
    """
    Automatically navigate to the main page before each test
    """
    load_dotenv()
    base_url = os.environ.get('WEB_URL')
    browser.get(base_url)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['browser']
            take_screenshot(driver)


def take_screenshot(driver):
    time.sleep(1)
    path = Path(__file__).parent.parent.parent.parent.joinpath(Dir.ARTEFACTS).joinpath(f"{datetime.now()}_result.jpg")
    driver.save_screenshot(path.absolute().as_posix())


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="chrome, firefox")
