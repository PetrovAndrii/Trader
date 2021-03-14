import time


class RegistrationHelper:

    def __init__(self, app):
        self.app = app

    def cookies_agree(self):
        wd = self.app.wd
        if wd.find_elements_by_css_selector('.banner_cookie_agreeBtn'):
            wd.find_element_by_css_selector('.banner_cookie_agreeBtn').click()
        else:
            pass

    def registration_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name('landing-header__button').click()

    def registration_fields(self, group_registration):
        wd = self.app.wd
        wd.find_element_by_css_selector('.regFullNameField').click()
        wd.find_element_by_css_selector('.regFullNameField').clear()
        wd.find_element_by_css_selector('.regFullNameField').send_keys(group_registration.full_name)
        wd.find_element_by_css_selector('.regEmailField').click()
        wd.find_element_by_css_selector('.regEmailField').clear()
        wd.find_element_by_css_selector('.regEmailField').send_keys(group_registration.email)
        wd.find_element_by_css_selector('.regPassField').click()
        wd.find_element_by_css_selector('.regPassField').clear()
        wd.find_element_by_css_selector('.regPassField').send_keys(group_registration.password)
        wd.find_element_by_css_selector('.regPassConfField').click()
        wd.find_element_by_css_selector('.regPassConfField').clear()
        wd.find_element_by_css_selector('.regPassConfField').send_keys(group_registration.confirm_pass)
        wd.find_element_by_css_selector('.regPhoneNumberField').click()
        wd.find_element_by_css_selector('.regPhoneNumberField').clear()
        wd.find_element_by_css_selector('.regPhoneNumberField').send_keys(group_registration.phone)

    def agree_terms_conditions(self):
        wd = self.app.wd
        element = wd.find_element_by_css_selector('.EULACheckbox')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_css_selector('.EULACheckbox').click()

    def button_join(self):
        wd = self.app.wd
        wd.find_element_by_name('submit').click()
        time.sleep(10)

    def error_name(self):
        wd = self.app.wd
        error = wd.find_elements_by_css_selector('.form-control regFullNameField errorInput')
        if error:
            print('Fullname empty')
        else:
            pass

    def error_email(self):
        wd = self.app.wd
        error = wd.find_element_by_id('emailError')
        if error.is_displayed():
            print(' ')
            print('EMAIL ADDRESS:', error.text)
        else:
            pass

    def error_agree(self):
        wd = self.app.wd
        error = wd.find_element_by_id('EULALoginError')
        if error.is_displayed():
            print(' ')
            print('You must agree with terms and conditions')
        else:
            pass

    def error_pass(self):
        wd = self.app.wd
        error = wd.find_element_by_id('passwordError')
        if error.is_displayed():
            print(' ')
            print('PASSWORD:', error.text)
        else:
            pass

    def error_confirm_pass(self):
        wd = self.app.wd
        error = wd.find_element_by_id('passwordMatchError')
        if error.is_displayed():
            print(' ')
            print('CONFIRM PASSWORD:', error.text)
        else:
            pass

    def check_success_registration(self):
        wd = self.app.wd
        if wd.find_elements_by_css_selector('.offer-heading'):
            self.app.open_home_page()
            time.sleep(1)
            self.app.session.log_out()
        else:
            pass

    def exist_account(self):
        wd = self.app.wd
        error = wd.find_element_by_id('userExistError')
        if error.is_displayed():
            text = error.text
            return text
        else:
            pass

    def login_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.landing-header__login').click()

    def join_for_free_at_login_form(self):
        wd = self.app.wd
        wd.find_element_by_class_name('joinForFreeLogin').click()