import time


class FAQHelper:

    def __init__(self, app):
        self.app = app

    def open_faq(self):
        wd = self.app.wd
        url = wd.current_url + '/FAQ'
        wd.get(url)
        # wd.find_element_by_css_selector("span.trading-icon-more").click()
        # time.sleep(1)
        # element = wd.find_element_by_css_selector('.landing-header__more.landing-header__more--open')
        # element.find_element_by_link_text('FAQ').click()

    def get_faq_list(self):
        wd = self.app.wd
        count = []
        if wd.find_elements_by_css_selector('div.faq'):
            count = len(wd.find_elements_by_css_selector('div.faq.active'))
        return count

    def show_all(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.showAllFAQs').click()

    def hide_all(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.hideAllFAQs').click()

    def id_rate(self):
        wd = self.app.wd
        if wd.find_element_by_xpath('//*[@id="rate"][@class="faq active"]'):
            pass
        else:
            wd.find_element_by_id('rate').click()
            wd.find_element_by_xpath('//*[@id="rate"][@class="faq active"]')

    def rate_link_plans(self):
        wd = self.app.wd
        if wd.find_element_by_xpath('//*[@id="rate"][@class="faq active"]'):
            wd.find_element_by_xpath('//*[@id="rate"]/div[2]/p/a').click()
            wd.find_elements_by_css_selector('.bg-white')
        else:
            print('TEST FAILED')

    def id_create(self):
        wd = self.app.wd
        wd.find_element_by_id('create').click()
        wd.find_element_by_xpath('//*[@id="create"][@class="faq active"]')

    def check_link_at_create(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="create"]/div[2]/p/a').click()
        time.sleep(3)
        if wd.find_element_by_css_selector('.checkout-container.jc_c'):
            pass
        else:
            wd.find_element_by_css_selector('.landing-header__account-img')

    def id_support(self):
        wd = self.app.wd
        wd.find_element_by_id('support').click()
        wd.find_element_by_xpath('//*[@id="support"][@class="faq active"]')

    def fb_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_link_text("Facebook Group").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def feedback_portal_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_link_text("Feedback Portal").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def release_notes_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_link_text("Release Notes").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_brokers(self):
        wd = self.app.wd
        wd.find_element_by_id('brokers').click()
        wd.find_element_by_xpath('//*[@id="brokers"][@class="faq active"]')

    def learn_more_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_xpath('//*[@id="brokers"]/div[2]/p[1]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def help_finding_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_link_text("Need help finding a broker? Learn More").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_multiple(self):
        wd = self.app.wd
        wd.find_element_by_id('multiple').click()
        wd.find_element_by_xpath('//*[@id="multiple"][@class="faq active"]')

    def id_connect(self):
        wd = self.app.wd
        wd.find_element_by_id('connect').click()
        wd.find_element_by_xpath('//*[@id="connect"][@class="faq active"]')

    def follow_help_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element_by_partial_link_text("the help within this blog post").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_change_plans(self):
        wd = self.app.wd
        wd.find_element_by_id('change-plans').click()
        wd.find_element_by_xpath('//*[@id="change-plans"][@class="faq active"]')
