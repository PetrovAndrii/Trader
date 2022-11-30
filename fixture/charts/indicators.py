from random import randint
import time
from constants.indicators import IndicatorsConstants


class IndicatorsHelper:

    def __init__(self, app):
        self.app = app

    def click_add_indicators_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.ADD_INDICATORS_BUTTON_TOOLBAR_CSS_SELECTOR).click()

    def add_random_general_indicator(self):
        wd = self.app.wd
        self.app.wait_element_not_located_id(IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements_by_css_selector(IndicatorsConstants.ADD_SELECTED_BUTTON_CSS_SELECTOR):
            links = wd.find_elements_by_css_selector(IndicatorsConstants.ADD_SELECTED_BUTTON_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link)
            link.click()
        else:
            print('HAVE NOT INDICATORS ON "MY INDICATORS" TAB')

    def get_indicators_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements_by_css_selector(IndicatorsConstants.INDICATOR_CAPTURE_PANEL_CSS_SELECTOR):
            count.append(element)
        return len(count)

    def close_indicators_modal_dialog(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.CLOSE_INDICATORS_MODAL_DIALOG_CSS_SELECTOR).click()
        # wd.find_element_by_css_selector('#scxIndicators div div div.modal-header a').click()

    def click_general_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.GENERAL_TAB_CSS_SELECTOR).click()

    def click_premium_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.PREMIUM_TAB_CSS_SELECTOR).click()

    def click_my_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.MY_INDICATORS_TAB_CSS_SELECTOR).click()
        time.sleep(3)

    def click_button_add_indicator_on_my_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.ADD_INDICATORS_BUTTON_MY_INDICATOR_TAB_CSS_SELECTOR).click()
        time.sleep(3)

    def choose_indicator_to_select_on_my_indicators(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector(IndicatorsConstants.LIST_INDICATORS_DROPDOWN_MY_INDICATORS_CSS_SELECTOR)
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        return link.text

    def confirm_selected_indicator(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.ADD_BUTTON_MY_INDICATORS_CSS_SELECTOR).click()

    def fill_custom_indicator_name(self, indicator_name):
        wd = self.app.wd
        self.app.wait_element_located_id(IndicatorsConstants.DIALOG_CONTAINER_MY_INDICATORS_ID)
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(indicator_name)

    def fill_custom_indicator_description(self, description):
        wd = self.app.wd
        wd.find_element_by_css_selector(IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element_by_css_selector(IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element_by_css_selector(IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(description)

    def button_save_as_custom_indicator(self):
        wd = self.app.wd
        wd.find_element_by_id(IndicatorsConstants.SAVE_AS_CUSTOM_BUTTON_MY_INDICATORS_ID).click()
        self.app.wait_element_not_located_id(IndicatorsConstants.SAVE_AS_CUSTOM_BUTTON_MY_INDICATORS_ID)

    def check_added_name(self, added_name):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element_by_xpath('//*[contains(text(), "' + added_name + '")]')
        # name = wd.find_element_by_xpath('//*[@id="indicators_container"]/div[last()]/div/div[2]')
        return name.text

    def get_my_indicators_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements_by_css_selector(IndicatorsConstants.LIST_MY_INDICATORS_CONTAINER_CSS_SELECTOR):
            count.append(element)
        return len(count)

    def delete_random_indicator_from_my_indicator_tab(self):
        wd = self.app.wd
        self.app.wait_element_not_located_id(IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements_by_css_selector(IndicatorsConstants.DELETE_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR):
            links = wd.find_elements_by_css_selector(IndicatorsConstants.DELETE_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link)
            link.click()
        else:
            print('HAVE NOT INDICATORS ON "MY INDICATORS" TAB')

    def click_edit_random_indicator_from_my_indicator_tab(self):
        wd = self.app.wd
        self.app.wait_element_not_located_id(IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements_by_css_selector(IndicatorsConstants.EDIT_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR):
            links = wd.find_elements_by_css_selector(IndicatorsConstants.EDIT_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link)
            link.click()
        else:
            print('HAVE NOT INDICATORS ON "MY INDICATORS" TAB')

    def change_indicator_name(self, indicator_name):
        wd = self.app.wd
        self.app.wait_element_located_id(IndicatorsConstants.DIALOG_CONTAINER_MY_INDICATORS_ID)
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element_by_css_selector(IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(indicator_name)

    def search_name(self, text):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[.='" + text + "']")

    def delete_random_indicator_from_workspace(self):
        wd = self.app.wd
        if wd.find_elements_by_css_selector(IndicatorsConstants.REMOVE_BUTTON_PANEL_WSP_CSS_SELECTOR):
            links = wd.find_elements_by_css_selector(IndicatorsConstants.REMOVE_BUTTON_PANEL_WSP_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            return print('NO INDICATOR AT WORKPLACE')

    def open_indicator_context_menu(self):
        wd = self.app.wd
        if wd.find_elements_by_css_selector(IndicatorsConstants.KABOB_MENU_PANEL_WSP_CSS_SELECTOR):
            links = wd.find_elements_by_css_selector(IndicatorsConstants.KABOB_MENU_PANEL_WSP_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            return print('NO INDICATOR AT WORKPLACE')

    def click_delete_indicator_from_context_menu(self):
        wd = self.app.wd
        self.app.wait_element_located_xpath(IndicatorsConstants.DELETE_INDICATORS_LINK_KABOB_MENU_XPATH)
        wd.find_element_by_xpath(IndicatorsConstants.DELETE_INDICATORS_LINK_KABOB_MENU_XPATH).click()
