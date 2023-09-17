import ast
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants.register import RegisterConstants
from constants.login import LoginConstants
from constants.header import HeaderConstants


class RegistrationHelper:

    def __init__(self, app):
        self.app = app

    def cookies_agree(self):
        wd = self.app.wd
        if wd.find_elements(By.CSS_SELECTOR, RegisterConstants.COOKIES_AGREE_BUTTON_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, RegisterConstants.COOKIES_AGREE_BUTTON_CSS_SELECTOR).click()
        else:
            pass

    def open_registration_form(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR).click()
            self.app.wait_element_located(By.XPATH, HeaderConstants.LOGOUT_TOOLBAR_BUTTON_XPATH, timeout=2)
#           time.sleep(2)
            wd.find_element(By.XPATH, HeaderConstants.LOGOUT_TOOLBAR_BUTTON_XPATH).click()
            wd.find_element(By.CLASS_NAME, HeaderConstants.GET_STARTED_BUTTON_CLASS_NAME).click()
            # try it free button on plans page
            element = wd.find_element(By.CSS_SELECTOR, '.button.button-blue.button-border.button-sm')
            wd.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()
        else:
            wd.find_element(By.CLASS_NAME, HeaderConstants.GET_STARTED_BUTTON_CLASS_NAME).click()
            element = wd.find_element(By.CSS_SELECTOR, '.button.button-blue.button-border.button-sm')
            wd.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()

    def registration_fields(self, full_name, email, password, phone_code, phone_number):
        time.sleep(2)
        self.fill_full_name(full_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_phone_code(phone_code)
        self.fill_phone_number(phone_number)

    def registration_fields_without_phone(self, full_name, email, password):
        time.sleep(2)
        self.fill_full_name(full_name)
        self.fill_email(email)
        self.fill_password(password)

    def fill_full_name(self, full_name):
        wd = self.app.wd
        wd.find_element(By.XPATH, RegisterConstants.FULL_NAME_FIELD_XPATH).click()
        wd.find_element(By.XPATH, RegisterConstants.FULL_NAME_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, RegisterConstants.FULL_NAME_FIELD_XPATH).send_keys(full_name)

    def fill_email(self, email):
        wd = self.app.wd
        wd.find_element(By.XPATH, RegisterConstants.EMAIL_FIELD_XPATH).click()
        element = wd.find_element(By.XPATH, RegisterConstants.EMAIL_FIELD_XPATH)
        wd.execute_script("arguments[0].value=''", element)
        # wd.find_element(By.XPATH, RegisterConstants.EMAIL_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, RegisterConstants.EMAIL_FIELD_XPATH).send_keys(email)

    def fill_password(self, password):
        wd = self.app.wd
        wd.find_element(By.XPATH, RegisterConstants.PASSWORD_FIELD_XPATH).click()
        element = wd.find_element(By.XPATH, RegisterConstants.PASSWORD_FIELD_XPATH)
        wd.execute_script("arguments[0].value=''", element)
        # wd.find_element(By.XPATH, RegisterConstants.PASSWORD_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, RegisterConstants.PASSWORD_FIELD_XPATH).send_keys(password)

    def fill_phone_code(self, phone_code):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.PHONE_CODE_BUTTON_CSS_SELECTOR).click()
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.PHONE_CODE_SEARCH_FIELD_CSS_SELECTOR).click()
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.PHONE_CODE_SEARCH_FIELD_CSS_SELECTOR).clear()
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.PHONE_CODE_SEARCH_FIELD_CSS_SELECTOR).send_keys(phone_code)
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.PHONE_CODE_LIST_ITEM_CSS_SELECTOR).click()

    def fill_phone_number(self, phone_number):
        wd = self.app.wd
        wd.find_element(By.XPATH, RegisterConstants.PHONE_NUMBER_FIELD_XPATH).click()
        wd.find_element(By.XPATH, RegisterConstants.PHONE_NUMBER_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, RegisterConstants.PHONE_NUMBER_FIELD_XPATH).send_keys(phone_number)

    def agree_terms_conditions_license(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, RegisterConstants.AGREE_TERMS_CHECKBOX_XPATH)
        # wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_button_create_my_account(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, RegisterConstants.CREATE_MY_ACCOUNT_BUTTON_XPATH)
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
#       time.sleep(5)

    def check_confirmation_registration(self):
        wd = self.app.wd
        time.sleep(2)
        self.app.wait_element_located(By.CSS_SELECTOR, RegisterConstants.CONFIRMATION_REGISTRATION_CSS_SELECTOR)
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.CONFIRMATION_REGISTRATION_CSS_SELECTOR)

    def login_button(self):
        wd = self.app.wd
        if wd.find_elements(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR).click()
            time.sleep(2)
            wd.find_element(By.XPATH, HeaderConstants.LOGOUT_TOOLBAR_BUTTON_XPATH).click()
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR).click()
        else:
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR).click()

    def link_create_an_account_at_login_form(self):
        wd = self.app.wd
        wd.refresh()
        wd.find_element(By.XPATH, LoginConstants.CREATE_AN_ACCOUNT_LINK_XPATH).click()
        self.app.wait_element_located(By.XPATH, RegisterConstants.CREATE_MY_ACCOUNT_BUTTON_XPATH)

    def check_error_in_page(self):
        wd = self.app.wd
        if not wd.find_elements(By.XPATH, RegisterConstants.ERROR_CONTAINS_XPATH):
            pass
        else:
            assert print('HAVE SOME ERROR ON PAGE')

    def show_password_is_inactive(self):
        wd = self.app.wd
        if wd.find_element(By.CSS_SELECTOR, LoginConstants.UCPICON_EYE_ELEMENT_CSS_SELECTOR):
            pass
        else:
            assert print('SHOW PASSWORD ACTIVE')

    def checkbox_not_selected(self):
        wd = self.app.wd
        if wd.find_element(By.XPATH, RegisterConstants.AGREE_TERMS_CHECKBOX_XPATH).is_selected():
            assert print('CHECKBOX SELECTED')
        else:
            pass

    def click_do_active_show_password(self):
        self.app.login_form.click_do_active_show_password()

    def click_do_inactive_show_password(self):
        self.app.login_form.click_do_inactive_show_password()

    def name_field_error(self):
        wd = self.app.wd
        error = wd.find_element(By.XPATH, RegisterConstants.FIELD_IS_REQUIRED_ERROR_XPATH)
        return error.text

    def email_field_error(self):
        wd = self.app.wd
        error = wd.find_element(By.XPATH, RegisterConstants.VALID_EMAIL_ERROR_XPATH)
        # wd.execute_script("return arguments[0].scrollIntoView(true);", error)
        return error.text

    def password_field_empty(self):
        wd = self.app.wd
        color = wd.find_element(By.XPATH, RegisterConstants.PASSWORD_FIELD_XPATH).value_of_css_property("border-color")
        r, g, b = ast.literal_eval(color.strip("rgb"))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value

    def text_if_agree_checkbox_not_selected(self):
        wd = self.app.wd
        time.sleep(1)
        if wd.find_elements(By.XPATH, RegisterConstants.YOU_MUST_AGREE_ERROR_TEXT_XPATH):
            error = wd.find_element(By.XPATH, RegisterConstants.YOU_MUST_AGREE_ERROR_TEXT_XPATH)
            return error.text
        else:
            error = 'Page have not error'
            return error

    def terms_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.XPATH, RegisterConstants.TERMS_LINK_XPATH).get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def license_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.XPATH, RegisterConstants.LICENSE_LINK_XPATH).get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def link_login_at_registration_form(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, RegisterConstants.CREATE_AN_ACCOUNT_LINK_XPATH).click()
        self.app.wait_element_located(By.XPATH, RegisterConstants.CREATE_MY_ACCOUNT_BUTTON_XPATH)

    def active_character_count_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.ACTIVE_CHARACTER_COUNT_ERROR_CSS_SELECTOR)

    def active_number_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.ACTIVE_NUMBER_ERROR_CSS_SELECTOR)

    def active_special_character_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.ACTIVE_SPECIAL_CHARACTER_ERROR_CSS_SELECTOR)

    def active_capital_letter_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.ACTIVE_CAPITAL_LETTER_ERROR_CSS_SELECTOR)

    def character_count_no_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.CHARACTER_COUNT_NO_ERROR_CSS_SELECTOR)

    def number_no_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.NUMBER_NO_ERROR_CSS_SELECTOR)

    def special_character_no_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.SPECIAL_CHARACTER_NO_ERROR_CSS_SELECTOR)

    def capital_letter_no_error(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, RegisterConstants.CAPITAL_LETTER_NO_ERROR_CSS_SELECTOR)

    def scroll_up(self):
        wd = self.app.wd
        wd.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        time.sleep(2)
