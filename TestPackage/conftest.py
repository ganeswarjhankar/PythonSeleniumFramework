import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = None


# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.webdriver import WebDriver
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    # help="my option: type1 or type2")


# @pytest.fixture(scope="class")
# request is instance, tie up the request instance to
# the test_e2e.py class instance( UseFixtures)
# request is an instance

# Donot want to use yield statement as causing issue which is not in Rahul shetty dictionary
# browser_name = request.config.getoption("browser_name")
# if browser_name == "chrome":
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        S = Service("D:\\chromedriver.exe")
        driver = webdriver.Chrome(service=S)

        #driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        S = Service("D:\\chromedriver.exe")
        driver = webdriver.Chrome(service=S)

        #driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


# invocation of firefox
# elif browser_name == "firefox":
# S = Service("D:\\chromedriver.exe")
# driver = webdriver.Chrome(service=S)
# IE Browser invocation
# elif browser_name == "IE":
# S = Service("D:\\geckodriver.exe")
# driver = webdriver.Ie(service=S)

# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
# tear down concept
# return driver


#@pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


