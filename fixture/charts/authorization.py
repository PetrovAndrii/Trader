import time


class AuthorizationHelper:

    def __init__(self, app):
        self.app = app

    def open_google(self):
        wd = self.app.wd
        wd.get('https://google.com')

    def check_log_in_profile(self):
        wd = self.app.wd
        wd.find_elements_by_css_selector('.landing-header__account-img')
