import time
from model.registration_model import Group
import string
import random


def random_symbol(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


class PlansHelper:

    def __init__(self, app):
        self.app = app

    def open_plans_all(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/div[1]/span').click()
        time.sleep(5)
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/div[1]/ul/li[1]').click()
        time.sleep(5)

    def open_plans_360pro(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/div[1]/span').click()
        time.sleep(1)
        wd.find_element_by_xpath('//*[@class="landing-header__navigation"]/div[1]/ul/li[2]').click()

    def click_access_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.market-page_top_button').click()

    def check_cost(self):
        wd = self.app.wd
        cost = wd.find_element_by_xpath('//*[@id="registration"]/div[1]/div/h3/strong')
        return cost.text

    def price_top_rigth(self):
        wd = self.app.wd
        dollar = wd.find_element_by_xpath('//*[@id="elite-info"]/div[1]/h4/span')
        cent = wd.find_element_by_xpath('//*[@id="elite-info"]/div[1]/h4/sup[2]/span')
        together = dollar.text + '.' + cent.text
        return together

    def fill_fields(self):
        self.app.registration.cookies_agree()
        email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
        print('')
        print('Email: ', email)
        self.app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                                        confirm_pass='P@ssw0rd', phone='+380930000000'))
        self.app.registration.agree_terms_conditions()
        self.app.registration.button_join()

    def checkout_plan_cost(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@class="your-plan__row"]/div[1]/div/label/div[2]/div/span[1]')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        cost = wd.find_element_by_xpath('//*[@class="your-plan__row"]/div[1]/div/label/div[2]/div/span[1]')
        return cost.text

    def checkout_total_price(self):
        wd = self.app.wd
        element = wd.find_element_by_id('totalPrice')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        cost = wd.find_element_by_id('totalPrice')
        return cost.text

    def get_row_list(self):
        wd = self.app.wd
        count = []
        if wd.find_elements_by_xpath('//*[contains(@style, "none")]'):
            count = len(wd.find_elements_by_xpath('//*[@class="table__row-wrap"][contains(@style, "none")]'))
        return count

    def put_only_differences(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@class="plans-gap w-5/12"]/div/span[2]/label/span')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_xpath('//*[@class="plans-gap w-5/12"]/div/span[2]/label/span').click()