import time
from random import randint
from constants.workspace import WorkspacesConstants
from constants.charts import ChartsConstants


class WorkspaceChartHelper:

    def __init__(self, app):
        self.app = app

    def button_add_workspace_chart(self):
        wd = self.app.wd
        wd.find_element_by_xpath(WorkspacesConstants.ADD_WORKSPACE_BUTTON_XPATH).click()

    def manage_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_xpath(WorkspacesConstants.MANAGE_WSP_MENU_XPATH).click()
        time.sleep(3)

    def manage_workspaces_option(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(WorkspacesConstants.KEBAB_MENU_MANAGE_WSP_CSS_SELECTOR).click()

    def share_private_workspace(self):
        wd = self.app.wd
        wd.find_element_by_class_name(WorkspacesConstants.SHARE_PRIVAT_BUTTON_KEBAB_MENU_CLASS_NAME).click()
        time.sleep(2)

    def add_new_workspace(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.ADD_WORKSPACE_BUTTON_MENU_ID).click()
        time.sleep(2)

    def add_new_chart(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.ADD_CHART_BUTTON_MENU_ID).click()
        time.sleep(2)
        if wd.find_elements_by_xpath(WorkspacesConstants.NOTIFICATION_BLOCK_XPATH):
            message = wd.find_element_by_xpath(WorkspacesConstants.MAX_ALLOWED_CHARTS_MESSAGE_XPATH)
            return print(message.text)
        else:
            pass

    def enter_workspace_name(self, workspace_name):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.NEW_WSP_NAME_FIELD_ID).click()
        wd.find_element_by_id(WorkspacesConstants.NEW_WSP_NAME_FIELD_ID).clear()
        wd.find_element_by_id(WorkspacesConstants.NEW_WSP_NAME_FIELD_ID).send_keys(workspace_name)

    def choose_random_forex_symbol(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.SEARCH_SYMBOL_CHART_MODAL_FIELD_ID).click()
        # wd.find_element_by_css_selector('.scxInstrumentSearchContainer.containerWorkspace ul li:nth-child(2)').click()
        links = wd.find_elements_by_css_selector(WorkspacesConstants.FOREX_INSTRUMENT_LISTS_CSS_SELECTOR)
        link = links[randint(0, len(links) - 1)]
        time.sleep(2)
        wd.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(2)
        wd.execute_script("arguments[0].click();", link)

    def choose_random_timing(self):
        pass

    def add_new_ideas_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(WorkspacesConstants.ADD_BUTTON_NEW_CHART_MODAL_CSS_SELECTOR).click()

    def open_workspace_list(self):
        wd = self.app.wd
        self.discard_changes_when_leaveWS()
        wd.find_element_by_xpath(WorkspacesConstants.WORKSPACE_LIST_OPEN_BUTTON_XPATH).click()
        self.discard_changes_when_leaveWS()

    def get_workspace_list(self):
        wd = self.app.wd
        time.sleep(3)
        self.open_workspace_list()
        count = []
        time.sleep(3)
        if wd.find_elements_by_css_selector(WorkspacesConstants.WSP_LIST_LEFT_SLIDE_CSS_SELECTOR):
            count = len(wd.find_elements_by_css_selector(WorkspacesConstants.WSP_LIST_LEFT_SLIDE_CSS_SELECTOR))
        return count

    def close_workspace_list(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(WorkspacesConstants.CLOSE_WSP_LIST_BUTTON_CSS_SELECTOR).click()

    def choose_random_bars(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.NEW_CHART_MODAL_BAR_STYLE_ID).click()
        links = wd.find_elements_by_xpath(WorkspacesConstants.NEW_CHART_MODAL_BAR_STYLE_LINK_XPATH)
        link = links[randint(0, len(links) - 1)]
        link.click()

    def get_charts_list(self):
        wd = self.app.wd
        count = []
        time.sleep(3)
        if wd.find_element_by_css_selector(ChartsConstants.SINGLE_CHARTS_CSS_SELECTOR):
            count = len(wd.find_elements_by_css_selector(ChartsConstants.SINGLE_CHARTS_CSS_SELECTOR))
        return count

    def open_random_private_workspaces(self):
        wd = self.app.wd
        time.sleep(3)
        if wd.find_elements_by_xpath(WorkspacesConstants.PRIVAT_WSP_THUMBNAIL_XPATH):
            links = wd.find_elements_by_xpath(WorkspacesConstants.PRIVAT_WSP_THUMBNAIL_XPATH)
            link = links[randint(0, len(links) - 1)]
            name = link.text
            link.click()
            return name
        else:
            if wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME):
                error = wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME)
                return error.text

    def return_imported_name(self):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element_by_xpath(WorkspacesConstants.WORKSPACE_OPEN_BUTTON_XPATH)
        return name.text

    def click_random_checkbox_in_manage_workspaces(self):
        wd = self.app.wd
        time.sleep(2)
        if wd.find_elements_by_xpath(WorkspacesConstants.CHECKBOX_PRIVAT_MANAGE_WSP_XPATH):
            links = wd.find_elements_by_xpath(WorkspacesConstants.CHECKBOX_PRIVAT_MANAGE_WSP_XPATH)
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            if wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME):
                error = wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME)
                return error.text

    def click_random_checkbox_in_premium_manage_workspaces(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath(WorkspacesConstants.CHECKBOX_PREMIUM_MANAGE_WSP_XPATH):
            links = wd.find_elements_by_xpath(WorkspacesConstants.CHECKBOX_PREMIUM_MANAGE_WSP_XPATH)
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            if wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME):
                error = wd.find_element_by_class_name(WorkspacesConstants.NO_WSP_MESSAGE_CLASS_NAME)
                return error.text

    def manage_workspaces_click_import_button(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.IMPORT_BUTTON_MANAGE_WSP_ID).click()
        time.sleep(3)

    def manage_workspaces_click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.DELETE_BUTTON_MANAGE_WSP_ID).click()

    def open_tab_premium_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_id(WorkspacesConstants.PREMIUM_WSP_TAB_ID).click()
        time.sleep(5)

    def open_random_premium_workspaces(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath(WorkspacesConstants.PREMIUM_TITLE_MANAGE_WSP_XPATH)
        link = links[randint(0, len(links) - 1)]
        name = link.text
        link.click()
        return name

    def save_changes_when_leaveWS(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath(WorkspacesConstants.SAVE_CHANGES_BUTTON_LEAVE_WSP_MODAL_XPATH):
            wd.find_element_by_xpath(WorkspacesConstants.SAVE_CHANGES_BUTTON_LEAVE_WSP_MODAL_XPATH).click()
        else:
            pass

    def discard_changes_when_leaveWS(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath(WorkspacesConstants.DISCARD_CHANGES_BUTTON_LEAVE_WSP_MODAL_XPATH):
            wd.find_element_by_xpath(WorkspacesConstants.DISCARD_CHANGES_BUTTON_LEAVE_WSP_MODAL_XPATH).click()
        else:
            pass
