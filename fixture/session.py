import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_in_from_homepage(self, mail_login, pass_login):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__login'):
            wd.find_element_by_css_selector('.landing-header__login').click()
            self.do_log_in(mail_login, pass_login)
        else:
            pass

    def do_log_in(self, mail_login, pass_login):
        wd = self.app.wd
        self.fill_login_form(mail_login, pass_login)
        self.click_log_in_button()
        time.sleep(2)
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            pass
        else:
            self.check_logout_button_on_footer()

    def click_log_in_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.form-button').click()

    def log_in_from_footer_on_marketplace(self, mail_login, pass_login):
        self.open_marketplace_page()
        self.login_button_on_footer()
        self.do_log_in(mail_login, pass_login)

    def log_in_from_wish_list_on_marketplace(self,  mail_login, pass_login):
        wd = self.app.wd
        self.open_marketplace_page()
        wd.find_element_by_css_selector('.wish-list-link.flex').click()
        self.fill_login_form(mail_login, pass_login)
        self.click_log_in_button()
        self.check_logout_button_on_footer()

    def log_in_from_shopping_cart_on_marketplace(self,  mail_login, pass_login):
        wd = self.app.wd
        self.open_marketplace_page()
        wd.find_element_by_css_selector('.relative.flex').click()
        wd.find_element_by_xpath('//*[@class="auth-switch"]/p/a').click()
        time.sleep(2)
        self.do_log_in(mail_login, pass_login)

    def log_in_from_charts_page(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element_by_id('profile-btn_').click()
        if wd.find_elements_by_xpath("//*[contains(text(), 'Sign In')]"):
            wd.find_element_by_xpath("//*[contains(text(), 'Sign In')]").click()
            self.fill_login_form(mail_login, pass_login)
            self.click_log_in_button()
        else:
            pass

    def log_in_from_modal_window_on_charts(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element_by_css_selector('.ucpicon-alert-b').click()
        if wd.find_elements_by_css_selector('.upgrade-button'):
            wd.find_element_by_css_selector('.upgrade-button').click()
            self.fill_login_form(mail_login, pass_login)
            self.click_log_in_button()
            time.sleep(2)
        else:
            pass

    def open_charts(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/a[1]').click()
        time.sleep(2)
        if wd.find_elements_by_css_selector('.banner_cookie_agreeBtn'):
            wd.find_element_by_css_selector('.banner_cookie_agreeBtn').click()
        else:
            pass

    def fill_login_form(self, mail_login, pass_login):
        self.fill_email(mail_login)
        self.fill_password(pass_login)

    def fill_email(self, mail_login):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Email"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(mail_login)

    def fill_password(self, pass_login):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Password"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(pass_login)

    def log_out_from_homepage(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[3]/a').click()
        else:
            self.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
            self.app.wait_element_not_class_name('form-inputs')
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            element = wd.find_element_by_xpath('//*[@class="landing-header__account-details"]/ul/li[3]/a')
            wd.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()

    def open_google(self):
        wd = self.app.wd
        wd.get('https://google.com')

    def check_log_in_profile(self):
        wd = self.app.wd
        wd.find_elements_by_css_selector('.landing-header__account-img')

    def check_authorization_on_chart(self):
        wd = self.app.wd
        wd.find_element_by_id('profile-btn_').click()
        wd.find_element_by_xpath("//*[contains(text(), 'Sign Out')]")

    def open_marketplace_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_element_by_css_selector('.landing-header__navigation')
        element.find_element_by_link_text('Marketplace').click()

    def login_button_on_footer(self):
        wd = self.app.wd
        element = wd.find_element_by_css_selector('.footer-account__item.footer-account__login')
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()

    def check_logout_button_on_footer(self):
        wd = self.app.wd
        time.sleep(3)
        element = wd.find_element_by_css_selector('.footer-account__item.footer-account__login')
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        button_name = element.text
        assert button_name == "Logout"
