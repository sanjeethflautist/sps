import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
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
    



@pytest.fixture(scope="function")
def browser(request):
    print('Working on '+request.config.getoption("--basebrowser") + 'Browser')
    chrom_options = ChromeOptions()
    chrom_options.add_extension(extension='saka.crx')
    driver = Chrome(ChromeDriverManager().install(),options=chrom_options) #ChromeDriverManager would automatically install the latest version of chrome web driver
    driver.implicitly_wait(20)
    driver.get('amazon.com')
    driver..
    
    yield driver
    driver.quit()