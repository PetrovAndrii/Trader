from selenium.common.exceptions import NoSuchElementException
import time
from random import randint
import os


class ProfileHelper:

    def __init__(self, app):
        self.app = app

    def my_profile(self):
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_css_selector('.landing-header__account-img').click()
        time.sleep(2)
        wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                 '/ul/li[1]/a').click()
        try:
            wd.find_element_by_css_selector('button.upgrade-button')
            return True
        except NoSuchElementException:
            print('')
            print('NOT FOUND ELEMENT!')
            return False

    def button_change_passw0rd(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button.upgrade-button').click()

    def current_password(self, curr_pass):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="Current Password"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Current Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Current Password"]').send_keys(curr_pass)

    def change_pass(self, new_pass):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@placeholder="New Password"]').click()
        wd.find_element_by_xpath('//input[@placeholder="New Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="New Password"]').send_keys(new_pass)
        wd.find_element_by_xpath('//input[@placeholder="Confirm Password"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Confirm Password"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys(new_pass)

    def save_new_pass(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.modal-button-primary').click()
        self.app.wait_element_located_css_selector('.form-button')

    def user_image(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.button-blue-simple').click()

    def upload_new_photo(self, path_foto):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@type='file']").send_keys(os.getcwd() + path_foto)

    def save_photo(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.modal-button-primary').click()

    def new_phone_number(self):
        wd = self.app.wd
        number = 9
        phone = ''.join(["%s" % randint(0, 8) for num in range(0, number)])
        # click edit button on the phone field
        wd.find_element_by_css_selector('.simple-button.simple-button--link.simple-button--slim').click()
        # write phone code
        wd.find_element_by_css_selector('.PhoneInput__button').click()
        time.sleep(1)
        wd.find_element_by_css_selector('.PhoneInput__search').click()
        wd.find_element_by_css_selector('.PhoneInput__search').clear()
        wd.find_element_by_css_selector('.PhoneInput__search').send_keys('380')
        time.sleep(2)
        wd.find_element_by_css_selector('.PhoneInput__list-item').click()
        # write phone number
        wd.find_element_by_xpath('//input[@placeholder="Phone Number"]').click()
        wd.find_element_by_xpath('//input[@placeholder="Phone Number"]').clear()
        wd.find_element_by_xpath('//input[@placeholder="Phone Number"]').send_keys(phone)
        print('phone number ', phone)
        return phone

    def save_new_phone(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.simple-button.simple-button--link.simple-button--slim > span').click()
        time.sleep(1)

    def check_new_phone(self):
        wd = self.app.wd
        # get a phone number
        get_phone_number = wd.find_element_by_css_selector('.ContentCard.mb-8 > span')
        # convert to text
        text = get_phone_number.text
        # remove all spaces
        phone_number = text.split()
        phone_number = ''.join(phone_number)
        return phone_number
