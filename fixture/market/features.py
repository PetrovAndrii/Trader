import time


class FeaturesHelper:

    def __init__(self, app):
        self.app = app

    def open_features_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/a[3]').click()

    def button_explore_smart_tools(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="LandingPageContainer"]/section/section[2]/div/div[1]/a/button').click()

    def button_get_started(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="relative bg-white"]/div[2]/div/div/a/button').click()
        url = wd.current_url
        return url

# Dashboard Customization

    def custom_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def variable_chart_monitoring(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def access_to_realtime_data(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-10 lg:mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

# Indicators
    def popular_indicators(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def active_alerts(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def custom_indicators(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

    def premium_indicators(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/ul/li[4]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]/section/div/div/div/div[4]/div/div[2]')
        except Exception as ex:
            print(ex)

    def premium_indicators_button(self):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_xpath('//*[@class="container mt-12 lg:mt-8"]'
                                 '/section/div/div/div/div[4]/div/div[1]/div/a').click()
        time.sleep(2)

# Connect & Trade
    def easily_connect(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-8"]/section/ul/li[1]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-8"]/section/div/div/div/div[1]/div/div[2]')
        except Exception as ex:
            print(ex)

    def choose_from_forex_brokers(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-8"]/section/ul/li[2]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-8"]/section/div/div/div/div[2]/div/div[2]')
        except Exception as ex:
            print(ex)

    def connect_trading_accounts(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="container mt-8"]/section/ul/li[3]').click()
        try:
            wd.find_element_by_xpath('//*[@class="container mt-8"]/section/div/div/div/div[3]/div/div[2]')
        except Exception as ex:
            print(ex)

# Additional Features
    def trading_rooms(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="cards-container__inner"]/div[1]/div/a').click()

    def trading_ideas(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="cards-container__inner"]/div[2]/div/a').click()

    def marketplace(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="cards-container__inner"]/div[3]/div/a').click()

    def support(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="cards-container__inner"]/div[4]/div/a').click()
