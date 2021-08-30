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
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[3]/a').click()
            wd.find_element_by_class_name('landing-header__button').click()
        else:
            wd.find_element_by_class_name('landing-header__button').click()

    def registration_fields(self, group_registration):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').send_keys(group_registration.full_name)
        wd.find_element_by_xpath('//input[@placeholder="Email"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(group_registration.email)
        wd.find_element_by_xpath('//input[@placeholder="Password"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(group_registration.password)
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys(group_registration.phone)

    def agree_terms_conditions_license(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//input[@type="checkbox"]')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()

    def button_create_my_account(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//button[@type="submit"]')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(5)
        if not wd.find_elements_by_css_selector('.error'):
            pass
        else:
            print('HAVE SOME ERROR ON PAGE')

    def check_confirmation_registration(self):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_css_selector('.offer-content')

    def login_button(self):
        wd = self.app.wd
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[3]/a').click()
            wd.find_element_by_css_selector('.landing-header__login').click()
        else:
            wd.find_element_by_css_selector('.landing-header__login').click()

    def join_for_free_at_login_form(self):
        wd = self.app.wd
        wd.refresh()
        wd.find_element_by_xpath('//*[@class="auth-switch"]/p/a').click()
        self.app.wait_element_located_xpath('//button[@type="submit"]')

    def check_error_in_page(self):
        wd = self.app.wd
        if not wd.find_elements_by_xpath('//*[contains(@class,"error")]'):
            pass
        else:
            assert print('HAVE SOME ERROR ON PAGE')
#            return print('HAVE SOME ERROR ON PAGE')

    # def error_name(self):
    #     wd = self.app.wd
    #     error = wd.find_elements_by_css_selector('.form-control regFullNameField errorInput')
    #     if error:
    #         print('Fullname empty')
    #     else:
    #         pass
    #
    # def error_email(self):
    #     wd = self.app.wd
    #     error = wd.find_element_by_id('emailError')
    #     if error.is_displayed():
    #         print(' ')
    #         print('EMAIL ADDRESS:', error.text)
    #     else:
    #         pass
    #
    # def error_agree(self):
    #     wd = self.app.wd
    #     error = wd.find_element_by_id('EULALoginError')
    #     if error.is_displayed():
    #         print(' ')
    #         print('You must agree with terms and conditions')
    #     else:
    #         pass
    #
    # def error_pass(self):
    #     wd = self.app.wd
    #     error = wd.find_element_by_id('passwordError')
    #     if error.is_displayed():
    #         print(' ')
    #         print('PASSWORD:', error.text)
    #     else:
    #         pass
    #
    # def exist_account(self):
    #     wd = self.app.wd
    #     error = wd.find_element_by_id('userExistError')
    #     if error.is_displayed():
    #         text = error.text
    #         return text
    #     else:
    #         pass
