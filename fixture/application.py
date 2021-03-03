from selenium import webdriver
from fixture.session import SessionHelper
from fixture.market.registration import RegistrationHelper
from fixture.market.profile import ProfileHelper
from fixture.market.FAQ import FAQHelper
from fixture.market.tutorial import TutorialHelper
from fixture.market.smart_tools import SmartToolsHelper
from fixture.market.smart_hub import SmartHubHelper
from fixture.market.features import FeaturesHelper
from fixture.market.marketing_pages import MarketingPagesHelper
from fixture.market.plans import PlansHelper
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
        if wd.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div[1]/button[1]'):
            wd.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/button[1]').click()
            time.sleep(3)
        else:
            pass

    def destroy(self):
        self.wd.quit()
