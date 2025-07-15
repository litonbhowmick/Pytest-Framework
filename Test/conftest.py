import json

from selenium.webdriver.chrome.service import Service
import os
import base64
from datetime import datetime
from selenium import webdriver
import pytest_html
import logging
import pytest


def data_parser(page_name):
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_dir, "../Main/DataResources/DynamictestData.json"))

        with open(file_path, "r") as jsonfile:
            data = json.load(jsonfile)
            return list(data.get(page_name))
    except Exception as e:
        print(f"Unexpected error: {e}")

@pytest.fixture(scope="function")
def init_driver():
    logging.basicConfig(level=logging.INFO)
    service_object = Service()
    driver = webdriver.Chrome(service=service_object)
    driver.get("https://courses.rahulshettyacademy.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Let pytest run the test first
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if test failed during the call phase
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("init_driver")
        if driver:
            screenshot_path = f"screenshots/{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report
            with open(screenshot_path, "rb") as f:
                encoded_img = base64.b64encode(f.read()).decode("utf-8")
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(encoded_img))
            report.extra = extra

@pytest.fixture
def test_logger(request):
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    # Optional: output to file too
    handler = logging.FileHandler(f"logs/{request.node.name}.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    yield logger

    handler.close()
    logger.removeHandler(handler)
