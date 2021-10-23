import time


class SmartToolsHelper:

    def __init__(self, app):
        self.app = app

    def open_smart_tools(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.landing-header__nav-link-wrap").click()
        time.sleep(1)
        element = wd.find_element_by_css_selector('.landing-header__more-dropdown')
        element.find_element_by_link_text('Smart Tools').click()

    def button_get_started(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="relative bg-white"]/div[2]/div/div/a/button').click()
        url = wd.current_url
        return url

    def name_tools(self):
        wd = self.app.wd
        tools = wd.find_element_by_xpath('//h1[@class="product-head"]')
        return tools.text

    def st_in_marketplace(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="__layout"]'
                                                  '/div/section/section[1]/div/a').get_attribute("href")
        wd.get(new_window_url)
        page = self.tools_copy()
        wd.get(current_url)
        return page

    def tools_copy(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath('//*[@class="nuxt-link-exact-active nuxt-link-active"]/span')
        if name:
            name1 = wd.find_element_by_xpath('//*[@class="nuxt-link-exact-active nuxt-link-active"]/span')
            return name1.text
        else:
            return print('error')

# Trend/Swing tools
    def s_fib(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[1]').click()

    def s_waves(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[2]').click()
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]'
                                 '/section/div/div/div/div[2]/div/div[1]/div/a/button').click()

    def s_patterns(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[3]').click()
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]'
                                 '/div[2]/section/div/div/div/div[3]/div/div[1]/div/a/button').click()

    def s_trend_lines(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[4]').click()

    def s_analytics(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[5]').click()
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]'
                                 '/div[2]/section/div/div/div/div[5]/div/div[1]/div/a/button').click()

    def s_gauge(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]/div[2]/section/ul/li[6]').click()
        wd.find_element_by_xpath('//*[@id="trendSwingTools"]'
                                 '/div[2]/section/div/div/div/div[6]/div/div[1]/div/a/button').click()

# Market Levels
    def s_support(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="marketLevels"]/div[2]/section/ul/li[1]').click()

    def s_resistance(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="marketLevels"]/div[2]/section/ul/li[2]').click()

    def s_pivots(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="marketLevels"]/div[2]/section/ul/li[3]').click()

# Range tools
    def daily_encapsulation(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="rangeTools"]/div/div[2]/section/ul/li[1]').click()

    def weekly_encapsulation(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="rangeTools"]/div/div[2]/section/ul/li[2]').click()

    def candlestick_overlay(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="rangeTools"]/div/div[2]/section/ul/li[3]').click()
