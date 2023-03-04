import time

from selenium.webdriver.common.by import By

from constants.hidden import HiddenConstants
from constants.header import HeaderConstants
from constants.register import RegisterConstants
from constants.charts import ChartsConstants
from constants.login import LoginConstants
from constants.footer import FooterConstants


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_in_from_homepage(self, mail_login, pass_login):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements(By.CSS_SELECTOR, HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.LOGIN_BUTTON_CSS_SELECTOR).click()
            self.do_log_in(mail_login, pass_login)
        else:
            pass

    def do_log_in(self, mail_login, pass_login):
        wd = self.app.wd
        self.key()
        self.fill_login_form(mail_login, pass_login)
        self.click_log_in_button()
        time.sleep(2)
        if wd.find_elements(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR):
            pass
        else:
            self.check_logout_button_on_footer()

    def click_log_in_button(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, LoginConstants.LOG_IN_BUTTON_CSS_SELECTOR).click()

    def log_in_from_footer_on_marketplace(self, mail_login, pass_login):
        self.open_marketplace_page()
        self.login_button_on_footer()
        self.do_log_in(mail_login, pass_login)

    def log_in_from_wish_list_on_marketplace(self,  mail_login, pass_login):
        wd = self.app.wd
        self.open_marketplace_page()
        wd.find_element(By.CSS_SELECTOR, HeaderConstants.WISH_LIST_ICON_CSS_SELECTOR).click()
        wd.get(self.app.base_url + "login" + HiddenConstants.CAPTCHA_KEY_TEXT)
        time.sleep(2)
        self.fill_login_form(mail_login, pass_login)
        self.click_log_in_button()
        self.check_logout_button_on_footer()

    def log_in_from_shopping_cart_on_marketplace(self,  mail_login, pass_login):
        wd = self.app.wd
        self.open_marketplace_page()
        wd.find_element(By.CSS_SELECTOR, HeaderConstants.BASKET_ICON_CSS_SELECTOR).click()
        wd.find_element(By.XPATH, RegisterConstants.LOGIN_LINK_XPATH).click()
        time.sleep(2)
        self.do_log_in(mail_login, pass_login)

    def log_in_from_charts_page(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element(By.ID, ChartsConstants.PROFILE_BUTTON_ID).click()
        if wd.find_elements(By.XPATH, ChartsConstants.SIGN_IN_ACC_CONTENT_LINK_XPATH):
            wd.find_element(By.XPATH, ChartsConstants.SIGN_IN_ACC_CONTENT_LINK_XPATH).click()
            self.key()
            self.fill_login_form(mail_login, pass_login)
            self.click_log_in_button()
        else:
            pass

    def log_in_from_modal_window_on_charts(self, mail_login, pass_login):
        wd = self.app.wd
        self.open_charts()
        wd.find_element(By.CSS_SELECTOR, ChartsConstants.ALERT_BUTTON_CSS_SELECTOR).click()
        if wd.find_elements(By.CSS_SELECTOR, ChartsConstants.UPGRADE_BUTTON_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, ChartsConstants.UPGRADE_BUTTON_CSS_SELECTOR).click()
            self.fill_login_form(mail_login, pass_login)
            self.click_log_in_button()
            time.sleep(2)
        else:
            pass

    def open_charts(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, HeaderConstants.CHARTS_LINK_XPATH).click()
        time.sleep(2)
        if wd.find_elements(By.CSS_SELECTOR, ChartsConstants.COOKIE_AGREE_BUTTON_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, ChartsConstants.COOKIE_AGREE_BUTTON_CSS_SELECTOR).click()
        else:
            pass

    def fill_login_form(self, mail_login, pass_login):
        self.app.wait_element_located(By.CSS_SELECTOR, LoginConstants.LOG_IN_BUTTON_CSS_SELECTOR)
        self.fill_email(mail_login)
        self.fill_password(pass_login)

    def fill_email(self, mail_login):
        wd = self.app.wd
        wd.find_element(By.XPATH, LoginConstants.EMAIL_FIELD_XPATH).click()
        wd.find_element(By.XPATH, LoginConstants.EMAIL_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, LoginConstants.EMAIL_FIELD_XPATH).send_keys(mail_login)

    def fill_password(self, pass_login):
        wd = self.app.wd
        wd.find_element(By.XPATH, LoginConstants.PASSWORD_FIELD_XPATH).click()
        wd.find_element(By.XPATH, LoginConstants.PASSWORD_FIELD_XPATH).clear()
        wd.find_element(By.XPATH, LoginConstants.PASSWORD_FIELD_XPATH).send_keys(pass_login)

    def log_out_from_homepage(self):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_elements(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR).click()
            time.sleep(2)
            wd.find_element(By.XPATH, HeaderConstants.LOGOUT_TOOLBAR_BUTTON_XPATH).click()
        else:
            self.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
            self.app.wait_element_not_located(By.CSS_SELECTOR, LoginConstants.FORM_INPUTS_CSS_SELECTOR)
            wd.find_element(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR).click()
            time.sleep(2)
            element = wd.find_element(By.XPATH, HeaderConstants.LOGOUT_TOOLBAR_BUTTON_XPATH)
            wd.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()

    def open_google(self):
        wd = self.app.wd
        wd.get('https://google.com')

    def check_log_in_profile(self):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, HeaderConstants.ACCOUNT_IMAGE_CSS_SELECTOR)

    def check_authorization_on_chart(self):
        wd = self.app.wd
        self.app.wait_element_located(By.ID, ChartsConstants.PROFILE_BUTTON_ID)
        wd.find_element(By.ID, ChartsConstants.PROFILE_BUTTON_ID).click()
        wd.find_element(By.XPATH, ChartsConstants.SIGN_OUT_ACC_CONTENT_LINK_XPATH)

    def open_marketplace_page(self):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_element(By.CSS_SELECTOR, HeaderConstants.LANDING_NAVIGATION_PANEL_CSS_SELECTOR)
        element.find_element(By.LINK_TEXT, HeaderConstants.MARKETPLACE_LINK_TXT).click()

    def login_button_on_footer(self):
        wd = self.app.wd
#        element = wd.find_element(By.CSS_SELECTOR, FooterConstants.LOG_IN_LINK_CSS_SELECTOR)
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
#        element.click()
        time.sleep(2)
        wd.find_element(By.CSS_SELECTOR, FooterConstants.LOG_IN_LINK_CSS_SELECTOR).click()

    def check_logout_button_on_footer(self):
        wd = self.app.wd
        time.sleep(3)
        element = wd.find_element(By.CSS_SELECTOR, FooterConstants.LOG_IN_LINK_CSS_SELECTOR)
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        self.app.wait_element_located(By.CSS_SELECTOR, FooterConstants.LOG_IN_LINK_CSS_SELECTOR)
        button_name = element.text
        assert button_name == "Logout"

    def key(self):
        wd = self.app.wd
        self.app.wait_element_located(By.CSS_SELECTOR, LoginConstants.LOG_IN_BUTTON_CSS_SELECTOR)
        wd.get(wd.current_url + HiddenConstants.CAPTCHA_KEY_TEXT)
        time.sleep(2)
