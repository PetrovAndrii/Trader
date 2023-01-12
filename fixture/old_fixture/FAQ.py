import time

from selenium.webdriver.common.by import By


class FAQHelper:

    def __init__(self, app):
        self.app = app

    def open_faq(self):
        wd = self.app.wd
        url = wd.current_url + '/FAQ'
        wd.get(url)
        # wd.find_element(By.CSS_SELECTOR, "span.trading-icon-more").click()
        # time.sleep(1)
        # element = wd.find_element(By.CSS_SELECTOR, '.landing-header__more.landing-header__more--open')
        # element.find_element(By.LINK_TEXT, 'FAQ').click()

    def get_faq_list(self):
        wd = self.app.wd
        count = []
        if wd.find_elements(By.CSS_SELECTOR, 'div.faq'):
            count = len(wd.find_elements(By.CSS_SELECTOR, 'div.faq.active'))
        return count

    def show_all(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, '.showAllFAQs').click()

    def hide_all(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, '.hideAllFAQs').click()

    def id_rate(self):
        wd = self.app.wd
        if wd.find_element(By.XPATH, '//*[@id="rate"][@class="faq active"]'):
            pass
        else:
            wd.find_element(By.ID, 'rate').click()
            wd.find_element(By.XPATH, '//*[@id="rate"][@class="faq active"]')

    def rate_link_plans(self):
        wd = self.app.wd
        if wd.find_element(By.XPATH, '//*[@id="rate"][@class="faq active"]'):
            wd.find_element(By.XPATH, '//*[@id="rate"]/div[2]/p/a').click()
            wd.find_elements(By.CSS_SELECTOR, '.bg-white')
        else:
            print('TEST FAILED')

    def id_create(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'create').click()
        wd.find_element(By.XPATH, '//*[@id="create"][@class="faq active"]')

    def check_link_at_create(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="create"]/div[2]/p/a').click()
        time.sleep(3)
        if wd.find_element(By.CSS_SELECTOR, '.checkout-container.jc_c'):
            pass
        else:
            wd.find_element(By.CSS_SELECTOR, '.landing-header__account-img')

    def id_support(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'support').click()
        wd.find_element(By.XPATH, '//*[@id="support"][@class="faq active"]')

    def fb_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.LINK_TEXT, "Facebook Group").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def feedback_portal_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.LINK_TEXT, "Feedback Portal").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def release_notes_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.LINK_TEXT, "Release Notes").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_brokers(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'brokers').click()
        wd.find_element(By.XPATH, '//*[@id="brokers"][@class="faq active"]')

    def learn_more_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.XPATH, '//*[@id="brokers"]/div[2]/p[1]/a').get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def help_finding_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.LINK_TEXT, "Need help finding a broker? Learn More").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_multiple(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'multiple').click()
        wd.find_element(By.XPATH, '//*[@id="multiple"][@class="faq active"]')

    def id_connect(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'connect').click()
        wd.find_element(By.XPATH, '//*[@id="connect"][@class="faq active"]')

    def follow_help_url(self):
        wd = self.app.wd
        current_url = wd.current_url
        new_window_url = wd.find_element(By.PARTIAL_LINK_TEXT, "the help within this blog post").get_attribute("href")
        wd.get(new_window_url)
        url = wd.current_url
        wd.get(current_url)
        return url

    def id_change_plans(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'change-plans').click()
        wd.find_element(By.XPATH, '//*[@id="change-plans"][@class="faq active"]')
