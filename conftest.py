import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    '''
    This function will automatically parse the arguments from pytest command lines
    Use request.config.getoption("--argmentname") for getting the arguments'
    '''

    parser.addoption(
        "--basebrowser",
        action="store",
        default='Chrome',
        help="Browsers supported Chrome,Safari and Firefox"
    )
    



@pytest.fixture(scope="module")
def driver(request):
    print('Working on '+request.config.getoption("--basebrowser") + 'Browser')
    chrome_options = ChromeOptions()
    chrome_options.add_extension(extension='qlearly.crx')
    driver = Chrome(ChromeDriverManager().install(),options=chrome_options) #ChromeDriverManager will automatically install the right version of chrome web driver
    yield driver
    driver.quit()