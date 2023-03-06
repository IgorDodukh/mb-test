import os
import time
from datetime import datetime
from pathlib import Path

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from scr.data.constants import Dir


@pytest.fixture(scope="session")
def browser():
    load_dotenv()
    base_url = os.environ.get('WEB_URL')

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    # TODO: did not debug for Firefox
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    driver.get(base_url)
    yield driver
    driver.quit()


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
