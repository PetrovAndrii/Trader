import time

log_in_button = ".landing-header__login"


class LoginFormHelper:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector(log_in_button):
            wd.find_element_by_css_selector(log_in_button).click()
            time.sleep(2)
        else:
            self.app.session.log_out_from_homepage()
            wd.find_element_by_css_selector(log_in_button).click()

    def check_error_in_page(self):
        self.app.registration.check_error_in_page()

    def show_password_is_inactive(self):
        self.app.registration.show_password_is_inactive()

    def click_do_active_show_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.show-password.ucpicon-eye').click()
        if wd.find_element_by_css_selector('.show-password.ucpicon-on') and\
                wd.find_elements_by_xpath('//input[(@placeholder="Password") and (@type="text")]'):
            pass
        else:
            assert print('something wrong')

    def click_do_inactive_show_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.show-password.ucpicon-on').click()
        if wd.find_element_by_css_selector('.show-password.ucpicon-eye') and\
                wd.find_elements_by_xpath('//input[(@placeholder="Password") and (@type="password")]'):
            pass
        else:
            assert print('something wrong')

    def link_create_an_account_at_login_form(self):
        self.app.registration.link_create_an_account_at_login_form()

    def click_link_forgot_password(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.simple-link.forgot-link').click()
        self.app.wait_element_located_css_selector('.reset-body')

    def click_link_back_to_login_at_reset_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="reset-head"]/a').click()
        self.app.wait_element_located_css_selector('.form-inputs')

    def fill_email(self, mail_login):
        self.app.session.fill_email(mail_login)

    def fill_password(self, pass_login):
        self.app.session.fill_password(pass_login)

    def click_log_in_button(self):
        self.app.session.click_log_in_button()

    def check_error_if_email_empty(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[1]/span/div/p')
        return error_text.text

    def check_no_error_in_email_field(self):
        wd = self.app.wd
        field_name = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[1]/span/div/p')
        text_field = field_name.text
        assert text_field == 'Email'

    def check_error_if_password_empty(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[2]/span/div/p')
        return error_text.text

    def check_no_error_in_password_field(self):
        wd = self.app.wd
        field_name = wd.find_element_by_xpath('//*[@class="form-inputs"]/div[2]/span/div/p')
        text_field = field_name.text
        assert text_field == 'Password'

    def check_error_wrong_email_or_password(self):
        wd = self.app.wd
        error_text = wd.find_element_by_xpath('//*[@class="form-block"]/form/p')
        return error_text.text

    def click_reset_password_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.form-button').click()
        time.sleep(2)

    def check_error_in_email_field_on_reset_page(self):
        wd = self.app.wd
        if wd.find_element_by_css_selector('.input-label.input-error'):
            error_text = wd.find_element_by_css_selector('.input-label.input-error')
            return error_text.text
        else:
            return print('no error on reset password page')

    def check_massage_on_reset_page_if_account_not_exist(self):
        wd = self.app.wd
        error = wd.find_element_by_css_selector('p.error')
        return error.text

    def click_link_create_an_account_on_reset_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('p.error > a').click()
        self.app.wait_element_located_css_selector('.checkout-step')
