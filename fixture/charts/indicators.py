from random import randint
import time

from selenium.webdriver.common.by import By

from constants.indicators import IndicatorsConstants


class IndicatorsHelper:

    def __init__(self, app):
        self.app = app

    def click_add_indicators_button(self):
        wd = self.app.wd
        # we have two identical css selectors and in order not to write a very large selector,
        # we click on the second such selector in the list
        elements = wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.ADD_INDICATORS_BUTTON_TOOLBAR_CSS_SELECTOR)
        elements[1].click()

    def add_random_indicator(self):
        wd = self.app.wd
        self.app.wait_element_not_located(By.ID, IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.INDICATOR_ITEM_CSS_SELECTOR):
            links = wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.INDICATOR_ITEM_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link),
            indicator_name = link.find_element(By.CSS_SELECTOR,
                                               IndicatorsConstants.SELECTED_INDICATOR_NAME_CSS_SELECTOR)
            add_button = link.find_element(By.CSS_SELECTOR, IndicatorsConstants.ADD_SELECTED_BUTTON_CSS_SELECTOR)
            add_button.click()
            time.sleep(1)
            return print('Indicator was added - ' + indicator_name.text)
        else:
            print('HAVE NOT INDICATORS ON TAB')

    def get_indicators_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.INDICATOR_CAPTURE_PANEL_CSS_SELECTOR):
            count.append(element)
        return len(count)

    def close_indicators_modal_dialog(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.CLOSE_INDICATORS_MODAL_DIALOG_CSS_SELECTOR).click()
        # wd.find_element(By.CSS_SELECTOR, '#scxIndicators div div div.modal-header a').click()

    def click_general_indicators(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.GENERAL_TAB_CSS_SELECTOR).click()

    def click_premium_indicators(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.PREMIUM_TAB_CSS_SELECTOR).click()

    def click_my_indicators(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.MY_INDICATORS_TAB_CSS_SELECTOR).click()
        time.sleep(3)

    def click_button_add_indicator_on_my_indicators(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR,
                        IndicatorsConstants.ADD_INDICATORS_BUTTON_MY_INDICATOR_TAB_CSS_SELECTOR).click()
        time.sleep(3)

    def choose_indicator_to_select_on_my_indicators(self):
        wd = self.app.wd
        links = wd.find_elements(By.CSS_SELECTOR,
                                 IndicatorsConstants.LIST_INDICATORS_DROPDOWN_MY_INDICATORS_CSS_SELECTOR)
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        return link.text

    def confirm_selected_indicator(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.ADD_BUTTON_MY_INDICATORS_CSS_SELECTOR).click()

    def fill_custom_indicator_name(self, indicator_name):
        wd = self.app.wd
        self.app.wait_element_located(By.ID, IndicatorsConstants.DIALOG_CONTAINER_MY_INDICATORS_ID)
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element(By.CSS_SELECTOR,
                        IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(indicator_name)

    def fill_custom_indicator_description(self, description):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element(By.CSS_SELECTOR,
                        IndicatorsConstants.DESCRIPTION_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(description)

    def button_save_as_custom_indicator(self):
        wd = self.app.wd
        wd.find_element(By.ID, IndicatorsConstants.SAVE_AS_CUSTOM_BUTTON_MY_INDICATORS_ID).click()
        self.app.wait_element_not_located(By.ID, IndicatorsConstants.SAVE_AS_CUSTOM_BUTTON_MY_INDICATORS_ID)

    def check_added_name(self, added_name):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element(By.XPATH, '//*[contains(text(), "' + added_name + '")]')
        # name = wd.find_element(By.XPATH, '//*[@id="indicators_container"]/div[last()]/div/div[2]')
        return name.text

    def get_my_indicators_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.LIST_MY_INDICATORS_CONTAINER_CSS_SELECTOR):
            count.append(element)
        return len(count)

    def delete_random_indicator_from_my_indicator_tab(self):
        wd = self.app.wd
        self.app.wait_element_not_located(By.ID, IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.DELETE_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR):
            links = wd.find_elements(By.CSS_SELECTOR,
                                     IndicatorsConstants.DELETE_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link)
            link.click()
        else:
            print('HAVE NOT INDICATORS ON TAB')

    def click_edit_random_indicator_from_my_indicator_tab(self):
        wd = self.app.wd
        self.app.wait_element_not_located(By.ID, IndicatorsConstants.LIST_INDICATORS_CONTAINER_ID)
        if wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.EDIT_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR):
            links = wd.find_elements(By.CSS_SELECTOR,
                                     IndicatorsConstants.EDIT_INDICATORS_BUTTON_MY_INDICATOR_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("return arguments[0].scrollIntoView(true);", link)
            link.click()
        else:
            print('HAVE NOT INDICATORS ON TAB')

    def change_indicator_name(self, indicator_name):
        wd = self.app.wd
        self.app.wait_element_located(By.ID, IndicatorsConstants.DIALOG_CONTAINER_MY_INDICATORS_ID)
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).click()
        wd.find_element(By.CSS_SELECTOR, IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).clear()
        wd.find_element(By.CSS_SELECTOR,
                        IndicatorsConstants.CUSTOM_NAME_FIELD_MY_INDICATORS_CSS_SELECTOR).send_keys(indicator_name)

    def search_name(self, text):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[.='" + text + "']")

    def delete_random_indicator_from_workspace(self):
        wd = self.app.wd
        if wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.REMOVE_BUTTON_PANEL_WSP_CSS_SELECTOR):
            links = wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.REMOVE_BUTTON_PANEL_WSP_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            link.click()
            time.sleep(1)
        else:
            return print('NO INDICATOR AT WORKPLACE')

    def open_indicator_context_menu(self):
        wd = self.app.wd
        if wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.KABOB_MENU_PANEL_WSP_CSS_SELECTOR):
            links = wd.find_elements(By.CSS_SELECTOR, IndicatorsConstants.KABOB_MENU_PANEL_WSP_CSS_SELECTOR)
            link = links[randint(0, len(links) - 1)]
            time.sleep(1)
            link.click()
            time.sleep(1)
        else:
            return print('NO INDICATOR AT WORKPLACE')

    def click_delete_indicator_from_context_menu(self):
        wd = self.app.wd
        self.app.wait_element_located(By.XPATH, IndicatorsConstants.DELETE_INDICATORS_LINK_KABOB_MENU_XPATH)
        wd.find_element(By.XPATH, IndicatorsConstants.DELETE_INDICATORS_LINK_KABOB_MENU_XPATH).click()
