from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import common.locators as locators

# max wait time
MAX_EXPLICIT_SYNC_TIME = 5

# this function clicks on web element
def click(driver,locator,mark_as_failed_if_not_visible=True,mark_as_failed_if_not_enabled=True,byelemnt=False):
    if byelemnt:
        locator.click()
    elif is_visible(driver,locator,mark_as_failed_if_not_visible):
        if is_enabled(driver,locator,mark_as_failed_if_not_enabled):
            WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator)).click()


# this function asserts comparison of a web element's text with passed in text.
def get_element_text(driver,locator):
    web_element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator))
    return web_element.text

# this function performs text entry of the passed in text, in a web element whose locator is passed to it.
def enter_text(driver,locator, text):
    return WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

# this function checks if the web element whose locator has been passed to it, is enabled or not and returns
# web element if it is enabled.
def is_enabled(driver,locator,mark_as_failed_if_not_enabled=True):
    if is_visible(driver, locator, mark_as_failed_if_not_enabled):
        return WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator))

# this function checks if the web element whose locator has been passed to it, is visible or not and returns
# true or false depending upon its visibility.
def is_visible(driver,locator,mark_as_failed_if_not_visible=True,replacement_property=None):
    if replacement_property!=None:
        loc_temp = locator[1].replace('~#REPLACE_PROPERTY#~',replacement_property)
        locator = (locator[0],loc_temp)
    obj_visibility = bool(WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator)))
    if mark_as_failed_if_not_visible:
        assert obj_visibility == True
    return obj_visibility

# this function moves the mouse pointer over a web element whose locator has been passed to it.
def hover_to(driver,locator):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator))
    ActionChains(driver).move_to_element(element).perform()

def get_child_objects(driver,locator_type,property):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(getattr('By',locator_type),property))
    return element

def get_child_objects_from_locator(driver,locator):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(locator))
    return element

def get_add_button_element(driver,column_locator,given_column_name):
    column_elements=driver.find_elements(column_locator[0],column_locator[1])
    column_index = get_column_index(column_elements,given_column_name)
    add_button_locator = driver.find_elements(locators.qlearly_Locators.BTN_LST_ADD_BOARD_DETAILS_SCREEN[0],locators.qlearly_Locators.BTN_LST_ADD_BOARD_DETAILS_SCREEN[1])
    return add_button_locator[column_index+1]


def get_column_index(column_elements, val):
    idx = -1
    for each_col in column_elements:
        if val == each_col.get_property('value'):
            idx = idx + 1
            break
    if idx == -1:
        print('No matching column found')
    return idx



def sendkeys(driver,input_keys):
    '''
    # Supported Special keys:

    NULL,CANCEL,HELP,BACKSPACE,BACK_SPACE,TAB,CLEAR,RETURN,ENTER,SHIFT,LEFT_SHIFT,CONTROL,LEFT_CONTROL,ALT,LEFT_ALT,PAUSE,ESCAPE,SPACE,PAGE_UP,PAGE_DOWN,END,HOME,LEFT,ARROW_LEFT,UP,ARROW_UP,RIGHT,ARROW_RIGHT,
    DOWN,ARROW_DOWN,INSERT,DELETE,SEMICOLON,EQUALS
    
    # number pad keys
    NUMPAD0,NUMPAD1,NUMPAD2,NUMPAD3,NUMPAD4,NUMPAD5,NUMPAD6,NUMPAD7,NUMPAD8,NUMPAD9,MULTIPLY,ADD,SEPARATOR,SUBTRACT,DECIMAL,DIVIDE
    
    # Function keys
    F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,META,COMMAND


    Examples:
    sendkeys(driver,'CONTROL+D')  #Sends cntr+D on the the open webdriver
    sendkeys(driver,'RETURN')  #Sends ENTER key on the the open webdriver
    sendkeys(driver,'+')  #Sends + key on the the open webdriver
    sendkeys(driver,'CONTROL+ALT+DELET')  #Sends cntr+alt+del keys on the the open webdriver
    '''

    actions = ActionChains(driver)

    key_obj = Keys()
    key_literal = ''
    for eachkeys in input_keys.split('+'):
        if '~#~'+eachkeys+'~#~' in '~#~NULL~#~CANCEL~#~HELP~#~BACKSPACE~#~BACK_SPACE~#~TAB~#~CLEAR~#~RETURN~#~ENTER~#~SHIFT~#~LEFT_SHIFT~#~CONTROL~#~LEFT_CONTROL~#~ALT~#~LEFT_ALT~#~PAUSE~#~ESCAPE~#~SPACE~#~PAGE_UP~#~PAGE_DOWN~#~END~#~HOME~#~LEFT~#~ARROW_LEFT~#~UP~#~ARROW_UP~#~RIGHT~#~ARROW_RIGHT~#~DOWN~#~ARROW_DOWN~#~INSERT~#~DELETE~#~SEMICOLON~#~EQUALS~#~NUMPAD0~#~NUMPAD1~#~NUMPAD2~#~NUMPAD3~#~NUMPAD4~#~NUMPAD5~#~NUMPAD6~#~NUMPAD7~#~NUMPAD8~#~NUMPAD9~#~MULTIPLY~#~ADD~#~SEPARATOR~#~SUBTRACT~#~DECIMAL~#~DIVIDE~#~F1~#~F2~#~F3~#~F4~#~F5~#~F6~#~F7~#~F8~#~F9~#~F10~#~F11~#~F12~#~META~#~COMMAND~#~':

            key_literal = key_literal + getattr(key_obj, eachkeys)
        else:
            key_literal = key_literal + eachkeys
    
    actions.send_keys(eachkeys)
    
    actions.perform()




