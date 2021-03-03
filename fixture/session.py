from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_in(self, mail_login, pass_login):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__login'):
            wd.find_element_by_css_selector('.landing-header__login').click()
            wd.find_element_by_name('username').click()
            wd.find_element_by_name('username').clear()
            wd.find_element_by_name('username').send_keys(mail_login)
            wd.find_element_by_name('password').click()
            wd.find_element_by_name('password').clear()
            wd.find_element_by_name('password').send_keys(pass_login)
            wd.find_element_by_name('authenticate').click()
        else:
            pass


    def log_out(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements_by_css_selector('.landing-header__account-img'):
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                     '/div[1]/div/div/div/div[3]/div[3]/div/ul/li[4]/a').click()
        else:
            self.log_in(mail_login="smart0trader2@gmail.com", pass_login="P@ssw0rd")
            wd.find_element_by_css_selector('.landing-header__account-img').click()
            wd.find_element_by_xpath('//*[@id="LandingPageContainer"]'
                                     '/div[1]/div/div/div/div[3]/div[3]/div/ul/li[4]/a').click()