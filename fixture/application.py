from selenium import webdriver

from constants.workspace import WorkspacesConstants
from fixture.session import SessionHelper
from fixture.charts.registration import RegistrationHelper
from fixture.market.profile import ProfileHelper
from fixture.old_fixture.FAQ import FAQHelper
from fixture.market.tutorial import TutorialHelper
from fixture.market.smart_tools import SmartToolsHelper
from fixture.market.smart_hub import SmartHubHelper
from fixture.market.features import FeaturesHelper
from fixture.market.marketing_pages import MarketingPagesHelper
from fixture.old_fixture.plans import PlansHelper
from fixture.charts.sharing import SharingHelper
from fixture.common import CommonHelper
from fixture.charts.login_form import LoginFormHelper
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from constants.header import HeaderConstants
from constants.charts import ChartsConstants
from constants.register import RegisterConstants
from fixture.charts.indicators import IndicatorsHelper
from fixture.charts.workspace_chart import WorkspaceChartHelper


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
        self.common = CommonHelper(self)
        self.login_form = LoginFormHelper(self)
        self.indicators = IndicatorsHelper(self)
        self.workspace_chart = WorkspaceChartHelper(self)
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
        self.wait_alert_is_present()
        # time.sleep(2)
        try:
            Alert(wd).accept()
        except:
            pass
        if wd.find_elements(By.CSS_SELECTOR, ChartsConstants.CLOSE_CHROME_MODAL_WINDOW_BUTTON_CSS_SELECTOR):
            wd.find_element(By.CSS_SELECTOR, ChartsConstants.CLOSE_CHROME_MODAL_WINDOW_BUTTON_CSS_SELECTOR).click()
        else:
            pass

    def open_charts_page(self):
        wd = self.wd
        self.open_home_page()
        self.session.log_in_from_homepage(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
        self.wait_element_located(By.XPATH, HeaderConstants.CHARTS_LINK_XPATH)
        wd.find_element(By.XPATH, HeaderConstants.CHARTS_LINK_XPATH).click()
        self.wait_element_located(By.CSS_SELECTOR, RegisterConstants.COOKIES_AGREE_BUTTON_CSS_SELECTOR)
        self.registration.cookies_agree()
        self.wait_element_located(By.CSS_SELECTOR, WorkspacesConstants.TRADING_ACCOUNT_TABLE_CSS_SELECTOR)

# wait methods
    def wait_element_located(self, by, locator, timeout=5):
        try:
            ui.WebDriverWait(self.wd, timeout).until(ec.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def wait_element_not_located(self, by, locator, timeout=5):
        try:
            ui.WebDriverWait(self.wd, timeout).until_not(ec.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def wait_alert_is_present(self, timeout=2):
        try:
            ui.WebDriverWait(self.wd, timeout).until(ec.alert_is_present())
            return True
        except TimeoutException as ex:
            return print(ex)

    def destroy(self):
        self.wd.quit()
