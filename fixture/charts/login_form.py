import time
from constants.login import LoginConstants
from constants.reset import ResetConstants
from constants.register import RegisterConstants
from constants.header import HeaderConstants


class LoginFormHelper:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector(HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR):
            wd.find_element_by_css_selector(HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR).click()
            time.sleep(2)
        else:
            self.app.session.log_out_from_homepage()
            wd.find_element_by_css_selector(HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR).click()

    def check_error_in_page(self):
        self.app.registration.check_error_in_page()

    def show_password_is_inactive(self):
        self.app.registration.show_password_is_inactive()

    def click_do_active_show_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(LoginConstants.UCPICON_EYE_ELEMENT_CSS_SELECTOR).click()
        if wd.find_element_by_css_selector(LoginConstants.UCPICON_ON_ELEMENT_CSS_SELECTOR) and\
                wd.find_elements_by_xpath(LoginConstants.PASSWORD_FIELD_SHOW_TEXT_XPATH):
            pass
        else:
            assert print('something wrong')

    def click_do_inactive_show_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(LoginConstants.UCPICON_ON_ELEMENT_CSS_SELECTOR).click()
        if wd.find_element_by_css_selector(LoginConstants.UCPICON_EYE_ELEMENT_CSS_SELECTOR) and\
                wd.find_elements_by_xpath(LoginConstants.PASSWORD_FIELD_HIDE_TEXT_XPATH):
            pass
        else:
            assert print('something wrong')

    def link_create_an_account_at_login_form(self):
        self.app.registration.link_create_an_account_at_login_form()

    def click_link_forgot_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(LoginConstants.FORGOT_LINK_CSS_SELECTOR).click()
        self.app.wait_element_located_css_selector(ResetConstants.RESET_BODY_ELEMENT_CSS_SELECTOR)

    def click_link_back_to_login_at_reset_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath(ResetConstants.BACK_LINK_XPATH).click()
        self.app.wait_element_located_css_selector(LoginConstants.FORM_INPUTS_CSS_SELECTOR)

    def fill_email(self, mail_login):
        self.app.session.fill_email(mail_login)

    def fill_password(self, pass_login):
        self.app.session.fill_password(pass_login)

    def click_log_in_button(self):
        self.app.session.click_log_in_button()

    def check_error_if_email_empty(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath(LoginConstants.ERROR_EMAIL_TEXT_XPATH)
        return error_text.text

    def check_no_error_in_email_field(self):
        wd = self.app.wd
        field_name = wd.find_element_by_xpath(LoginConstants.ERROR_EMAIL_TEXT_XPATH)
        text_field = field_name.text
        assert text_field == 'Email'

    def check_error_if_password_empty(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath(LoginConstants.ERROR_PASSWORD_TEXT_XPATH)
        return error_text.text

    def check_no_error_in_password_field(self):
        wd = self.app.wd
        field_name = wd.find_element_by_xpath(LoginConstants.ERROR_PASSWORD_TEXT_XPATH)
        text_field = field_name.text
        assert text_field == 'Password'

    def check_error_wrong_email_or_password(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath(LoginConstants.ERROR_INVALID_TEXT_XPATH)
        return error_text.text

    def click_reset_password_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ResetConstants.RESET_PASSWORD_BUTTON_CSS_SELECTOR).click()
        time.sleep(2)

    def check_error_in_email_field_on_reset_page(self):
        wd = self.app.wd
        if wd.find_element_by_css_selector(ResetConstants.ERROR_REQUIRED_TEXT_CSS_SELECTOR):
            error_text = wd.find_element_by_css_selector(ResetConstants.ERROR_REQUIRED_TEXT_CSS_SELECTOR)
            return error_text.text
        else:
            return print('no error on reset password page')

    def check_massage_on_reset_page_if_account_not_exist(self):
        wd = self.app.wd
        error = wd.find_element_by_css_selector(ResetConstants.ERROR_TEXT_ACCOUNT_NOT_EXIST_CSS_SELECTOR)
        return error.text

    def click_link_create_an_account_on_reset_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(ResetConstants.CREATE_ACCOUNT_LINK_CSS_SELECTOR).click()
        self.app.wait_element_located_css_selector(RegisterConstants.CHECKOUT_TEXT_CSS_SELECTOR)
