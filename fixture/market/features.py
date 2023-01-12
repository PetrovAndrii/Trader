import time

from selenium.webdriver.common.by import By


class FeaturesHelper:

    def __init__(self, app):
        self.app = app

    def open_features_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "div.landing-header__nav-link-wrap").click()
        time.sleep(1)
        element = wd.find_element(By.CSS_SELECTOR, '.landing-header__more-dropdown')
        element.find_element(By.LINK_TEXT, 'Features').click()

    def button_explore_smart_tools(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="tw-hidden w-64 mt-12 lg:block"]/button').click()

    def button_get_started(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="relative bg-white"]/div[2]/div/div/a/button').click()
        url = wd.current_url
        return url

# Dashboard Customization

    def custom_workspaces(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def variable_chart_monitoring(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def access_to_realtime_data(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

# Indicators
    def popular_indicators(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def active_alerts(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def custom_indicators(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

    def premium_indicators(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/ul/li[4]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[4]/div/div[2]')
        except Exception as ex:
            print(ex)

    def premium_indicators_button(self):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element(By.XPATH, '//*[@class="container mt-12 lg:mt-8"]'
                                  '/section/div/div/div/div[4]/div/div[1]/div/a').click()
        time.sleep(2)

# Connect & Trade
    def easily_connect(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def choose_from_forex_brokers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def connect_trading_accounts(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element(By.XPATH, '//*[@class="container mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

# Additional Features
    def trading_rooms(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="cards-container__inner"]/div[1]/div/a').click()

    def trading_ideas(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="cards-container__inner"]/div[2]/div/a').click()

    def marketplace(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="cards-container__inner"]/div[3]/div/a').click()
        time.sleep(1)

    def support(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="cards-container__inner"]/div[4]/div/a').click()
