from selenium import webdriver
from fixture.session import SessionHelper
from fixture.charts.registration import RegistrationHelper
from fixture.market.profile import ProfileHelper
from fixture.market.FAQ import FAQHelper
from fixture.market.tutorial import TutorialHelper
from fixture.market.smart_tools import SmartToolsHelper
from fixture.market.smart_hub import SmartHubHelper
from fixture.market.features import FeaturesHelper
from fixture.market.marketing_pages import MarketingPagesHelper
from fixture.market.plans import PlansHelper
from fixture.charts.sharing import SharingHelper
from fixture.charts.workspace_chart import WorkspaceChartHelper
from fixture.common import CommonHelper
from fixture.charts.authorization import AuthorizationHelper
from fixture.charts.indicators import IndicatorsHelper
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
import time


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == "ie":
            self.wd = webdriver.Ie()
            self.wd.maximize_window()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.registration = RegistrationHelper(self)
        self.profile = ProfileHelper(self)
        self.FAQ = FAQHelper(self)
        self.tutorial = TutorialHelper(self)
        self.smart_tools = SmartToolsHelper(self)
        self.smart_hub = SmartHubHelper(self)
        self.features = FeaturesHelper(self)
        self.marketing_pages = MarketingPagesHelper(self)
        self.plans = PlansHelper(self)
        self.sharing = SharingHelper(self)
        self.workspace_chart = WorkspaceChartHelper(self)
        self.common = CommonHelper(self)
        self.authorization = AuthorizationHelper(self)
        self.indicators = IndicatorsHelper(self)
        self.base_url = base_url

    # check valid session in browser or not
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        time.sleep(2)
        try:
            Alert(wd).accept()
        except:
            pass
        if wd.find_elements_by_css_selector('button.pushcrew-chrome-style-notification-btn.pushcrew-btn-close'):
            wd.find_element_by_css_selector('button.pushcrew-chrome-style-notification-btn.pushcrew-btn-close').click()
        else:
            pass

    def open_charts_page(self):
        wd = self.wd
        self.open_home_page()
        self.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
        time.sleep(3)
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/a[1]').click()
        time.sleep(5)
        self.registration.cookies_agree()

# wait methods
    def wait_element_located_id(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException:
            return False

    def wait_element_not_located_id(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until_not(EC.visibility_of_element_located((By.ID, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_xpath(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_link_text(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_partial_link_text(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_name(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.NAME, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_tag_name(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.TAG_NAME, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_class_name(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def wait_element_located_css_selector(self, locator, timeout=20):
        try:
            ui.WebDriverWait(self.wd, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException as ex:
            return print(ex)

    def destroy(self):
        self.wd.quit()
