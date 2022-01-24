import ast
import time

from selenium.webdriver.common.keys import Keys


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
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[3]/a').click()
            wd.find_element_by_class_name('landing-header__button').click()
        else:
            wd.find_element_by_class_name('landing-header__button').click()

    def registration_fields(self, full_name, email, password, phone):
        time.sleep(2)
        self.fill_full_name(full_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_phone(phone)

    def fill_full_name(self, full_name):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Full Name"]').send_keys(full_name)

    def fill_email(self, email):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Email"]').click()
        element = wd.find_element_by_xpath('//input[@placeholder="Email"]')
        wd.execute_script("arguments[0].value=''", element)
        # wd.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email)

    def fill_password(self, password):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Password"]').click()
        element = wd.find_element_by_xpath('//input[@placeholder="Password"]')
        wd.execute_script("arguments[0].value=''", element)
        # wd.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(password)

    def fill_phone(self, phone):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys(phone)

    def agree_terms_conditions_license(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//input[@type="checkbox"]')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_button_create_my_account(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//button[@type="submit"]')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(5)

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

    def link_create_an_account_at_login_form(self):
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

    def show_password_is_inactive(self):
        wd = self.app.wd
        if wd.find_element_by_css_selector('.show-password.ucpicon-eye'):
            pass
        else:
            assert print('SHOW PASSWORD ACTIVE')

    def checkbox_not_selected(self):
        wd = self.app.wd
        if wd.find_element_by_xpath('//*[@class="form-block"]/form/label/input').is_selected():
            assert print('CHECKBOX SELECTED')
        else:
            pass

    def click_do_active_show_password(self):
        self.app.login_form.click_do_active_show_password()

    def click_do_inactive_show_password(self):
        self.app.login_form.click_do_inactive_show_password()

    def name_field_error(self):
        wd = self.app.wd
        error = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[1]/span/div/p')
        return error.text

    def email_field_error(self):
        wd = self.app.wd
        error = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[2]/span/div/p')
        # wd.execute_script("return arguments[0].scrollIntoView(true);", error)
        return error.text

    def password_field_empty(self):
        wd = self.app.wd
        color = wd.find_element_by_xpath('//input[@placeholder="Password"]').value_of_css_property("border-color")
        r, g, b = ast.literal_eval(color.strip("rgb"))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value

    def text_if_agree_checkbox_not_selected(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath('//*[@class="form-block"]/form/p'):
            error = wd.find_element_by_xpath('//*[@class="form-block"]/form/p')
            return error.text
        else:
            error = 'Page have not error'
            return error

    def terms_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@name="terms"]/span/a[1]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def license_link(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@name="terms"]/span/a[2]').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def link_login_at_registration_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="auth-switch"]/p/a').click()
        self.app.wait_element_located_xpath('//button[@type="submit"]')

    def active_character_count_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(1) > i.ucpicon-close')

    def active_number_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(2) > i.ucpicon-close')

    def active_special_character_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(3) > i.ucpicon-close')

    def active_capital_letter_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(4) > i.ucpicon-close')

    def character_count_no_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(1) > i.ucpicon-content-menu-checkbox')

    def number_no_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(2) > i.ucpicon-content-menu-checkbox')

    def special_character_no_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(3) > i.ucpicon-content-menu-checkbox')

    def capital_letter_no_error(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.validation-rules > p:nth-child(4) > i.ucpicon-content-menu-checkbox')

    def scroll_up(self):
        wd = self.app.wd
        wd.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(2)
