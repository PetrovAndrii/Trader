import time
from random import randint
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from constants.sharing import SharingConstants
from constants.ideas import IdeasConstants
from constants.charts import ChartsConstants
from constants.scripting import ScriptingConstants
from constants.workspace import WorkspacesConstants


class SharingHelper:

    def __init__(self, app):
        self.app = app

    def share_ideas_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(SharingConstants.SHARE_IDEAS_BUTTON_CSS_SELECTOR).click()
        time.sleep(1)

    def share_charts_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(SharingConstants.SHARE_CHART_TOOLBAR_BUTTON_CSS_SELECTOR).click()
        time.sleep(2)
        if wd.find_elements_by_css_selector(SharingConstants.BOOTBOX_BODY_CSS_SELECTOR):
            element = wd.find_element_by_css_selector(SharingConstants.BOOTBOX_BODY_CSS_SELECTOR)
            return print(element.text)
        else:
            pass

    def share_workspace_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(SharingConstants.SHARE_WSP_TOOLBAR_BUTTON_CSS_SELECTOR).click()
        if wd.find_elements_by_css_selector(SharingConstants.BOOTBOX_BODY_CSS_SELECTOR):
            element = wd.find_element_by_css_selector(SharingConstants.BOOTBOX_BODY_CSS_SELECTOR)
            return print(element.text)
        else:
            pass

    def browse_ideas(self):
        wd = self.app.wd
        new_window_url = wd.find_element_by_xpath(SharingConstants.BROWSE_IDEAS_TOOLBAR_BUTTON_XPATH).get_attribute("href")
        wd.get(new_window_url)
        # wd.find_element_by_xpath(SharingConstants.BROWSE_IDEAS_TOOLBAR_BUTTON_XPATH).click()
        try:
            Alert(wd).accept()
        except (UnexpectedAlertPresentException, NoAlertPresentException):
            pass
        time.sleep(3)

    def browse_scripts(self):
        wd = self.app.wd
        new_window_url = wd.find_element_by_xpath(SharingConstants.BROWSE_SCRIPTS_TOOLBAR_BUTTON_XPATH).get_attribute("href")
        wd.get(new_window_url)
        # wd.find_element_by_xpath(SharingConstants.BROWSE_SCRIPTS_TOOLBAR_BUTTON_XPATH).click()
        try:
            Alert(wd).accept()
        except (UnexpectedAlertPresentException, NoAlertPresentException):
            pass
        time.sleep(3)

    def snapshot(self):
        wd = self.app.wd
        wd.find_element_by_xpath(SharingConstants.SNAPSHOT_BUTTON_XPATH).click()
        time.sleep(5)
        element = wd.find_element_by_xpath(SharingConstants.SNAPSHOT_IMAGE_LOADER_XPATH)
        if element.is_displayed():
            pass
        else:
            result_load_snapshot = wd.find_element_by_xpath(SharingConstants.SNAPSHOT_IMAGE_SUCCESS_XPATH)
            return result_load_snapshot.text

    def make_snapshot_chart(self):
        self.snapshot()

    def make_snapshot_workspace(self):
        wd = self.app.wd
        wd.find_element_by_xpath(SharingConstants.SNAPSHOT_WSP_BUTTON_XPATH).click()
        time.sleep(5)
        element = wd.find_element_by_xpath(SharingConstants.SNAPSHOT_IMAGE_LOADER_XPATH)
        if element.is_displayed():
            pass
        else:
            result_load_snapshot = wd.find_element_by_xpath(SharingConstants.SNAPSHOT_IMAGE_SUCCESS_XPATH)
            return result_load_snapshot.text

    def make_snapshot_scripts(self):
        self.snapshot()

    def write_idea_name(self, idea_name):
        wd = self.app.wd
        wd.find_element_by_css_selector(SharingConstants.IDEA_NAME_FIELD_CSS_SELECTOR).click()
        wd.find_element_by_css_selector(SharingConstants.IDEA_NAME_FIELD_CSS_SELECTOR).clear()
        wd.find_element_by_css_selector(SharingConstants.IDEA_NAME_FIELD_CSS_SELECTOR).send_keys(idea_name)

    def write_description(self, description_text):
        wd = self.app.wd
        wd.find_element_by_id(SharingConstants.DESCRIPTION_AREA_ID).click()
        wd.find_element_by_id(SharingConstants.DESCRIPTION_AREA_ID).clear()
        wd.find_element_by_id(SharingConstants.DESCRIPTION_AREA_ID).send_keys(description_text)

    def publish_idea(self):
        wd = self.app.wd
        wd.find_element_by_id(SharingConstants.PUBLISH_BUTTON_ID).click()

    def open_manage_shared_ideas_scripts(self):
        wd = self.app.wd
        self.share_ideas_button()
        wd.find_element_by_css_selector(SharingConstants.MANAGE_SHARED_TOOLBAR_BUTTON_CSS_SELECTOR).click()

    def check_shared_ideas(self, name_shared_ideas):
        wd = self.app.wd
        time.sleep(3)
        self.open_manage_shared_ideas_scripts()
        time.sleep(3)
        name = wd.find_element_by_xpath('//*[contains(text(), "' + name_shared_ideas + '")]')
        return name.text

    def import_random_workspace_button(self):
        wd = self.app.wd
        self.app.wait_element_located_xpath(IdeasConstants.WORKSPACE_VIEW_XPATH)
#        time.sleep(3)
        links = wd.find_elements_by_xpath(IdeasConstants.WORKSPACE_VIEW_XPATH)
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        name = link.find_element_by_xpath(IdeasConstants.IDEAS_TITLE_XPATH)
        name1 = str(name.text)
        self.import_button_from_opened_ideas()
        return name1.upper()

    def import_button_from_opened_ideas(self):
        wd = self.app.wd
        # scroll to element
        element = wd.find_element_by_xpath(IdeasConstants.IDEAS_FOOTER_IMPORT_XPATH)
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_xpath(IdeasConstants.IDEAS_FOOTER_IMPORT_XPATH).click()

    def import_random_chart_button(self):
        wd = self.app.wd
        time.sleep(3)
        links = wd.find_elements_by_xpath(IdeasConstants.CHARTS_VIEW_THUMBNAIL_XPATH)
        link = links[randint(0, len(links) - 1)]
        link.click()
        name = link.find_element_by_xpath(IdeasConstants.IDEAS_TITLE_XPATH)
        name1 = str(name.text)
        self.import_button_from_opened_ideas()
        return name1.upper()

    def return_imported_name(self):
        wd = self.app.wd
        time.sleep(15)
        name = wd.find_element_by_xpath(WorkspacesConstants.WORKSPACE_OPEN_BUTTON_XPATH)
        return name.text

    def open_scripting_tab(self):
        wd = self.app.wd
        if not wd.find_elements_by_class_name(ChartsConstants.TRADING_PANEL_OPEN_CLASS_NAME):
            self.app.common.open_trading_panel()
            wd.find_element_by_class_name(ScriptingConstants.SCRIPTING_TAB_CLASS_NAME).click()
        else:
            wd.find_element_by_class_name(ScriptingConstants.SCRIPTING_TAB_CLASS_NAME).click()

    def open_user_smart_script(self):
        wd = self.app.wd
        wd.find_element_by_class_name(ScriptingConstants.OPEN_SCRIPT_BUTTON_CLASS_NAME).click()

    def open_my_smart_scripts_tab(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ScriptingConstants.MY_SMART_SCRIPTS_TAB_CSS_SELECTOR).click()

    def smart_script_share_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ScriptingConstants.MENU_KABOB_BUTTON_CSS_SELECTOR).click()
        wd.find_element_by_xpath(ScriptingConstants.SHARE_BUTTON_DROPDOWN_XPATH).click()

    def import_random_scripts_button(self):
        wd = self.app.wd
        element = wd.find_element_by_class_name(ScriptingConstants.NO_SEARCH_RESULTS_CLASS_NAME)
        if element.is_displayed():
            print('No Search Results')
        else:
            time.sleep(3)
            links = wd.find_elements_by_xpath(ScriptingConstants.SCRIPT_VIEW_THUMB_NAIL_XPATH)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("arguments[0].scrollIntoView(true);", link)
            link.click()
            name = link.find_element_by_xpath(IdeasConstants.IDEAS_TITLE_XPATH)
            name1 = name.text
            wd.find_element_by_xpath(IdeasConstants.IDEAS_FOOTER_IMPORT_XPATH).click()
            return name1

    def return_imported_script_name(self):
        wd = self.app.wd
        time.sleep(3)
        if wd.find_elements_by_class_name(ScriptingConstants.NO_SEARCH_RESULTS_CLASS_NAME):
            print('No Search Results')
        else:
            self.app.wait_element_located_class_name(ScriptingConstants.SCRIPT_LIST_ITEM_CLASS_NAME)
            self.open_my_smart_scripts_tab()
            # to get a new script, sort by new ones and take the second script from the list
            #  (the first one as a favorite for sharing)
            self.click_sort_button()
            self.sort_by_newest()
            time.sleep(3)
            name = wd.find_element_by_xpath(ScriptingConstants.SCRIPT_LIST_INNER_CONTAINER_XPATH)
            return name.text

    def click_sort_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ScriptingConstants.SORT_BUTTON_CSS_SELECTOR).click()

    def sort_by_newest(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ScriptingConstants.SORT_LIST_ITEM_NEWEST_CSS_SELECTOR).click()

    def sort_by_oldest(self):
        wd = self.app.wd
        self.click_sort_button()
        wd.find_element_by_css_selector(ScriptingConstants.SORT_LIST_ITEM_OLDEST_CSS_SELECTOR).click()

    def remove_random_sharing_ideas(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath(IdeasConstants.DELETE_WORKSPACE_BUTTON):
            links = wd.find_elements_by_xpath(IdeasConstants.DELETE_WORKSPACE_BUTTON)
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            return print('HAVE NOT IDEAS FOR DELETE')

    def get_shared_ideas_scripts_list(self):
        wd = self.app.wd
        count = []
        time.sleep(5)
        for element in wd.find_elements_by_xpath(IdeasConstants.DELETE_WORKSPACE_BUTTON):
            count.append(element)
        return count

    def random_view_on_social_hub(self):
        wd = self.app.wd
        time.sleep(5)
        if wd.find_elements_by_xpath(IdeasConstants.SOCIAL_HUB_LINK_XPATH):
            links = wd.find_elements_by_xpath(IdeasConstants.SOCIAL_HUB_LINK_XPATH)
            link = links[randint(0, len(links) - 1)]
            link.click()
            try:
                Alert(wd).accept()
            except (UnexpectedAlertPresentException, NoAlertPresentException):
                pass
            time.sleep(5)
        else:
            return print('HAVE NOT IDEAS FOR VIEW')

    def button_share_into_social_on_footer(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath(IdeasConstants.SHARE_INTO_SOCIAL_BUTTON_FOOTER_XPATH)
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_xpath(IdeasConstants.DETAIL_IDEA_FOOTER_XPATH).click()

    def button_share_into_social_on_ideas(self):
        wd = self.app.wd
        wd.find_element_by_xpath(IdeasConstants.SHARE_IDEAS_INTO_SOCIAL_BUTTON_XPATH).click()

    def open_workspace_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath(WorkspacesConstants.WORKSPACE_LIST_OPEN_BUTTON_XPATH).click()

    def open_setting_active_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.ACTIVE_WORKSPACE_BUTTON_ID).click()
        wd.find_element_by_xpath(WorkspacesConstants.SETTING_ACTIVE_WORKSPACE_BUTTON_XPATH).click()

    def click_share_button_on_ws_settings(self):
        wd = self.app.wd
        self.app.wait_element_located_xpath(WorkspacesConstants.SHARE_BUTTON_SETTING_WS_XPATH)
        wd.find_element_by_xpath(WorkspacesConstants.SHARE_BUTTON_SETTING_WS_XPATH).click()

    def share_workspace_from_settings(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(WorkspacesConstants.ITEM_SHARE_CSS_SELECTOR).click()
