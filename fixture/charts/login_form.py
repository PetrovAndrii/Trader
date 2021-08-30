from random import randint
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
