import pytest as pytest

from selenium import webdriver


# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.webdriver import WebDriver
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    # help="my option: type1 or type2")


@pytest.fixture(scope="class")
# request is instance, tie up the request instance to
# the test_e2e.py class instance( UseFixtures)
# request is an instance

# Donot want to use yield statement as causing issue which is not in Rahul shetty dictionary
# browser_name = request.config.getoption("browser_name")
# if browser_name == "chrome":
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    elif browser_name == "firefox":
        print("FF driver")
    elif browser_name == "IE":
        print("IE driver")

    # S = Service("D:\\chromedriver.exe")
    # driver: WebDriver = webdriver.Chrome(service=S)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
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


# driver.close()
