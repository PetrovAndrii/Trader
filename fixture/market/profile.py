from selenium.common.exceptions import NoSuchElementException
import time
from random import randint
import os


class ProfileHelper:

    def __init__(self, app):
        self.app = app

    def my_profile(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.landing-header__account-img').click()
        time.sleep(2)
        wd.find_element_by_xpath('//*[@class="landing-header__account-details"]'
                                 '/ul/li[1]/a').click()
        try:
            wd.find_element_by_xpath('//*[@class="form"]/label[4]/p')
            return True
        except NoSuchElementException:
            print('')
            print('NOT FOUND ELEMENT!')
            return False

    def button_change_passw0rd(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="form"]/div/button').click()

    def current_password(self, curr_pass):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="password-form"]/label[1]/input').click()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[1]/input').clear()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[1]/input').send_keys(curr_pass)

    def change_pass(self, new_pass):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="password-form"]/label[2]/input').click()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[2]/input').clear()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[2]/input').send_keys(new_pass)
        wd.find_element_by_xpath('//*[@class="password-form"]/label[3]/input').click()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[3]/input').clear()
        wd.find_element_by_xpath('//*[@class="password-form"]/label[3]/input').send_keys(new_pass)

    def save_new_pass(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.modal-button-primary').click()
        time.sleep(5)

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
        number = 10
        phone = ''.join(["%s" % randint(0, 9) for num in range(0, number)])
        wd.find_element_by_xpath('//*[@class="form"]/label[3]/input').click()
        wd.find_element_by_xpath('//*[@class="form"]/label[3]/input').clear()
        wd.find_element_by_xpath('//*[@class="form"]/label[3]/input').send_keys(phone)

    def save_new_phone(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.upgrade-button.small.save-button').click()
