import pytest
from selenium import webdriver

# Using the pytest_addoption() function to introduce custom commandline parameters while running tests
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Mention the browser names from the following to run your tests: Chrome, Firefox")

# Setup fixture with scope mentioned given as Class, hence it will only run once for each Class
@pytest.fixture(scope='class')
def SetUp(request):
    browserName = request.config.getoption("--browser")
    if browserName.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get('https://v1.practicesoftwaretesting.com/#/')
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()
