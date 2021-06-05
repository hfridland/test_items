import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose user language")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")
