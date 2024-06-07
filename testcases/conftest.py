import pytest
from selenium import webdriver


@pytest.fixture()
# @pytest.fixture(params=["chrome", "edge"])  # running test in 2 or more browsers
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param                # for running params prpvided
    print(f"Launching {browser} browser")
    if browser == 'chrome':
        my_driver = webdriver.Chrome()
        my_driver.maximize_window()
    elif browser == 'firefox':
        my_driver = webdriver.Firefox()
        my_driver.maximize_window()
    elif browser == 'edge':
        my_driver = webdriver.Edge()
        my_driver.maximize_window()
    url = "https://practicetestautomation.com/practice-test-login/"
    my_driver.get(url)
    yield my_driver
    print(f"Closing {browser} browser")
    my_driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
