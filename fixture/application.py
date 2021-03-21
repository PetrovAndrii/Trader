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
from fixture.charts.add_workspace_chart import WorkspaceChartHelper
import time


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
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
        self.add_workspace_chart = WorkspaceChartHelper(self)
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
        wd.maximize_window()
        time.sleep(2)
        if wd.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div[1]/button[1]'):
            wd.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/button[1]').click()
        else:
            pass
        wd.application_cache

    def open_charts_page(self):
        wd = self.wd
        wd.get(self.base_url)
        self.open_home_page()
        self.session.log_in(mail_login="test@yopmail.com", pass_login="P@ssw0rd")
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/a[1]').click()
        time.sleep(3)
        self.registration.cookies_agree()

    def destroy(self):
        self.wd.quit()
