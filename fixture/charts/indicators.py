from random import randint, random
import time
from selenium.webdriver.support.ui import Select


class IndicatorsHelper:

    def __init__(self, app):
        self.app = app

    def click_add_indicators_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.scxToolbar-btn.scxToolbar-btn-indicators.indicatorMove.text-center').click()

    def add_random_general_indicator(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector('.scxIndicators_button_simple.scxIndicators_button_add')
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()

    def get_indicators_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements_by_css_selector('.indicatorCapturePanel'):
            count.append(element)
        return len(count)

    def close_indicators_modal_dialog(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#scxIndicators div div div.modal-header a').click()

    def click_general_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.scxIndicators_allIndicators').click()

    def click_premium_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.scxIndicators_mtiIndicators').click()

    def click_my_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.scxIndicators_myIndicators').click()
        time.sleep(3)

    def click_button_add_indicator_on_my_indicators(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.btn.btn-primary.addNewIndicator').click()
        time.sleep(3)

    def choose_indicator_to_select_on_my_indicators(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector('.bootbox-input.bootbox-input-select.form-control option')
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        return link.text

    def confirm_selected_indicator(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[data-bb-handler="confirm"]').click()

    def fill_custom_indicator_name(self, indicator_name):
        wd = self.app.wd
        self.app.wait_element_located_id('scxIndicatorDialog_container_social')
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_name').click()
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_name').clear()
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_name').send_keys(indicator_name)

    def fill_custom_indicator_description(self, description):
        wd = self.app.wd
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_description').click()
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_description').clear()
        wd.find_element_by_css_selector('.form-control.scxIndicators_input_description').send_keys(description)

    def button_save_as_custom_indicator(self):
        wd = self.app.wd
        wd.find_element_by_id('scxIndicatorDialog_btn_save').click()
        self.app.wait_element_not_located_id('scxIndicatorDialog_btn_save')

    def check_added_name(self):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element_by_xpath('//*[@id="indicators_container"]/div[last()]/div/div[2]')
        return name.text

