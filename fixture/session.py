import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_in_from_homepage(self, mail_login, pass_login):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__login'):
            wd.find_element_by_css_selector('.landing-header__login').click()
            self.fill_login_form(mail_login, pass_login)
            wd.find_element_by_name('authenticate').click()
            time.sleep(3)
            wd.find_element_by_css_selector('.landing-header__account-img')
        else:
            pass

    def log_in_from_marketplace(self, mail_login, pass_login):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("span.trading-icon-more").click()
        time.sleep(1)
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/div[2]/ul/li[3]').click()
        if wd.find_elements_by_css_selector('.landing-header__login'):
            wd.find_element_by_css_selector('.landing-header__login').click()
            wd.find_element_by_xpath('//input[@placeholder="Email Address"]').click()
            wd.find_element_by_xpath('//input[@placeholder="Email Address"]').clear()
            wd.find_element_by_xpath('//input[@placeholder="Email Address"]').send_keys(mail_login)
            wd.find_element_by_xpath('//input[@placeholder="Password"]').click()
            wd.find_element_by_xpath('//input[@placeholder="Password"]').clear()
            wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(pass_login)
            wd.find_element_by_class_name('form-button').click()
            wd.find_element_by_css_selector('.landing-header__account-img')
        else:
            pass

    def log_in_from_charts_page(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element_by_id('profile-btn_').click()
        if wd.find_elements_by_xpath("//*[contains(text(), 'Sign In')]"):
            wd.find_element_by_xpath("//*[contains(text(), 'Sign In')]").click()
            self.fill_login_form(mail_login, pass_login)
            wd.find_element_by_name('authenticate').click()
        else:
            pass

    def log_in_from_modal_window_on_charts(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element_by_css_selector('.ucpicon-share-b').click()
        if wd.find_elements_by_css_selector('.simple-modal__btn.button.'
                                            'button--text-right.button--link.button--primary'):
            wd.find_element_by_css_selector('.simple-modal__btn.button.'
                                            'button--text-right.button--link.button--primary').click()
            self.fill_login_form(mail_login, pass_login)
            wd.find_element_by_name('authenticate').click()
        else:
            pass

    def open_charts(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/a[1]').click()
        if wd.find_elements_by_css_selector('.banner_cookie_agreeBtn'):
            wd.find_element_by_css_selector('.banner_cookie_agreeBtn').click()
        else:
            pass

    def fill_login_form(self, mail_login, pass_login):
        wd = self.app.wd
        wd.find_element_by_name('username').click()
        wd.find_element_by_name('username').clear()
        wd.find_element_by_name('username').send_keys(mail_login)
        wd.find_element_by_name('password').click()
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys(pass_login)

    def log_out_from_homepage(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[4]/a').click()
        else:
            self.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            time.sleep(2)
            wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                     '/ul/li[4]/a').click()
