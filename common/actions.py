from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

MAX_EXPLICIT_SYNC_TIME = 10

def click(driver,by_locator):
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

# this function asserts comparison of a web element's text with passed in text.
def get_element_text(driver,by_locator):
    web_element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    return web_element.text

# this function performs text entry of the passed in text, in a web element whose locator is passed to it.
def enter_text(driver,by_locator, text):
    return WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

# this function checks if the web element whose locator has been passed to it, is enabled or not and returns
# web element if it is enabled.
def is_enabled(driver,by_locator):
    return WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))

# this function checks if the web element whose locator has been passed to it, is visible or not and returns
# true or false depending upon its visibility.
def is_visible(driver,by_locator):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    return bool(element)

# this function moves the mouse pointer over a web element whose locator has been passed to it.
def hover_to(driver,by_locator):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    ActionChains(driver).move_to_element(element).perform()

def get_child_objects(driver,locator_type,property):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(getattr(By,locator_type),property))
    return element

def get_child_objects_from_locator(driver,by_locator):
    element = WebDriverWait(driver, MAX_EXPLICIT_SYNC_TIME).until(expected_conditions.visibility_of_element_located(by_locator))
    return element

def sendkeys(driver,input_keys):

    ''' 
    Supported Special keys:

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




