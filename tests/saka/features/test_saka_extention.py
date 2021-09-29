import time
import common.actions as actions
import common.locators as locators
from selenium.webdriver.common.keys import Keys

def test_check_if_added_bookmark_is_present_in_saka_extention(browser):
    # Set up some test case data
    URL = 'https://www.selenium.dev/selenium-ide/'

    # Navigate to the DuckDuckGo home page
    browser.get(URL)
    time.sleep(2)
    
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.COMMAND + 't')
    body.send_keys(Keys.ENTER)
    #browser.maximize_window()
    #time.sleep(2)
    #perform.sendkeys (browser,'CONTROL+d')
    #perform.sendkeys (browser,'ENTER')
    time.sleep(2)
    browser.get("chrome-extension://nbdfpcokndmapcollfpjdpjlabnibjdi/saka.html")
    #container = actions.get_child_objects_from_locator(browser,locators.saka_Locators.GUI_CONTAINER)
    #header = actions.get_child_objects(browser,'ID','search-bar')
    #print(header)
    
    

    time.sleep(10)