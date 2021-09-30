
import common.actions as actions
import common.locators as locators
import common.global_data as global_data
import pytest

@pytest.fixture()
def extension(driver):
    # open_extension_home_page
    driver.switch_to.window(driver.current_window_handle)
    driver.get(global_data.extension_url)
    actions.click(driver,locators.qlearly_Locators.BTN_SKIP_DETAILS_SCREEN)
    actions.click(driver, locators.qlearly_Locators.BTN_INTRO_SKIP_DETAILS_SCREEN)

def test_default_columns(extension,driver):
    col_obj =locators.qlearly_Locators.CLM_LST_COLUMN_NAME_DETAILS_SCREEN
    columns= driver.find_elements(col_obj[0],col_obj[1])
    for each_col in columns:
        assert each_col.get_property('value') in global_data.DEFAULT_COL_NAMES


def test_add_bookmarks(driver):

    for each_bookmark in global_data.list_for_bookmark.keys():
        # add book marks
        actions.click(driver, actions.get_add_button_element(driver,
                                                             locators.qlearly_Locators.CLM_LST_COLUMN_NAME_DETAILS_SCREEN,
                                                             'Bookmark'), byelemnt=True)
        actions.enter_text(driver, locators.qlearly_Locators.EDT_ENTRY_TITLE_CREATE_NEW,each_bookmark)
        actions.enter_text(driver, locators.qlearly_Locators.EDT_ENTRY_WEBSITE_URL_CREATE_NEW, global_data.list_for_bookmark[each_bookmark])
        actions.click(driver, locators.qlearly_Locators.BTN_CREATE_NEW)

        # Validate if websites and bookmark names are added on the page
        actions.is_visible(driver, locators.qlearly_Locators.TXT_BOOKMARK_NAME_ALIKE,replacement_property=each_bookmark)
        actions.is_visible(driver,locators.qlearly_Locators.TXT_BOOKMARK_URL_ALIKE,replacement_property=global_data.list_for_bookmark[each_bookmark])



