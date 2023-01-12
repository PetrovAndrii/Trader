import time

from selenium.webdriver.common.by import By

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
        element = wd.find_element(By.CSS_SELECTOR, '.landing-header__navigation')
        element.find_element(By.LINK_TEXT, 'Pricing').click()

    def open_plans_360pro(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@class="landing-header__navigation"]/div[1]/span').click()
        time.sleep(1)
        wd.find_element(By.XPATH, '//*[@class="landing-header__navigation"]/div[1]/ul/li[2]').click()

    def click_access_button(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, '.market-page_top_button').click()

    def check_cost(self):
        wd = self.app.wd
        cost = wd.find_element(By.XPATH, '//*[@id="registration"]/div[1]/div/h3/strong')

        return cost.text

    def price_top_rigth(self):
        wd = self.app.wd
        dollar = wd.find_element(By.XPATH, '//*[@id="elite-info"]/div[1]/h4/span')
        cent = wd.find_element(By.XPATH, '//*[@id="elite-info"]/div[1]/h4/sup[2]/span')
        together = dollar.text + '.' + cent.text
        return together

    def fill_fields(self):
        self.app.registration.cookies_agree()
        email = random_symbol("smart", 7) + random_symbol("trader", 7) + "@yopmail.com"
        print('')
        print('Email: ', email)
        self.app.registration.registration_fields(Group(full_name='Test Test', email=email, password='P@ssw0rd',
                                                        confirm_pass='P@ssw0rd', phone='+380930000000'))
        self.app.registration.agree_terms_conditions_license()
        self.app.registration.click_button_create_my_account()

    def checkout_plan_cost(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, '//*[@class="your-plan__row"]/div[1]/div/label/div[2]/div/span[1]')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        cost = wd.find_element(By.XPATH, '//*[@class="your-plan__row"]/div[1]/div/label/div[2]/div/span[1]')
        return cost.text

    def checkout_total_price(self):
        wd = self.app.wd
        element = wd.find_element(By.ID, 'totalPrice')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        cost = wd.find_element(By.ID, 'totalPrice')
        return cost.text

    def get_row_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements(By.XPATH, '//*[@class="table__row-wrap"][contains(@style, "none")]'):
            count.append(element)
        return len(count)

    def put_only_differences(self):
        wd = self.app.wd
        element = wd.find_element(By.XPATH, '//*[@class="plans-gap w-5/12"]/div/span[2]/label/span')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element(By.XPATH, '//*[@class="plans-gap w-5/12"]/div/span[2]/label/span').click()
