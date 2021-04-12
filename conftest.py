import pytest
import json
from fixture.application import Application
import os.path


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
       fixture = Application(browser=browser, base_url=target['baseUrl'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(params=["chrome", "ie", "firefox"])
def parametrize_browser(request):
    global fixture
    global target
    browser = request.param
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    fixture = Application(browser=browser, base_url=target['baseUrl'])
    return fixture


# fixture for open a new browser for each test
@pytest.fixture()
def browser(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    fixture = Application(browser=browser, base_url=target['baseUrl'])
    request.addfinalizer(fixture.destroy)
    return fixture
