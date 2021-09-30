from selenium.webdriver.common.by import By

class qlearly_Locators():
    # DETAILS_SCREEN
    CLM_LST_COLUMN_NAME_DETAILS_SCREEN = (By.XPATH,"//div[@class='white_box fullheight dragable-element ui-sortable-handle']//input[@class='column-input']")
    BTN_SKIP_DETAILS_SCREEN = (By.XPATH, "//button[@id='choose_bn_skip']")
    BTN_INTRO_SKIP_DETAILS_SCREEN = (By.XPATH,"//a[@class='introjs-button introjs-skipbutton']")
    BTN_LST_ADD_BOARD_DETAILS_SCREEN = (By.XPATH,"//div//button[@class='btn theme_btn btn-block']")
    TXT_BOOKMARK_URL_ALIKE = (By.XPATH, "//a[@href='~#REPLACE_PROPERTY#~']") # here ~#REPLACE_PROPERTY#~ will be website name
    TXT_BOOKMARK_NAME_ALIKE = (By.XPATH,"//p[contains(text(),'~#REPLACE_PROPERTY#~')]")

    # CREATE_NEW Screen
    EDT_ENTRY_TITLE_CREATE_NEW = (By.ID, "entry_title")
    EDT_ENTRY_WEBSITE_URL_CREATE_NEW = (By.ID, "entry_website_url")
    BTN_CREATE_NEW = (By.XPATH,"//button[contains(text(),'CREATE')]")




