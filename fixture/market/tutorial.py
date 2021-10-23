import time
import re
from selenium.common.exceptions import InvalidSelectorException


class TutorialHelper:

    def __init__(self, app):
        self.app = app

    def open_tutorial(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page down
        element = wd.find_element_by_css_selector('.firstNavColumn.secondPart')
        element.find_element_by_link_text('Tutorials').click()

    def check_fideo_form(self):
        wd = self.app.wd
        try:
            time.sleep(2)
            wd.find_element_by_xpath('//*[@id="__layout"]/div/section/div/div[1]/div[2]')
        except InvalidSelectorException as ex:
            print(ex)

    def copy_name_tutorial(self):
        wd = self.app.wd
        name = wd.find_element_by_xpath('//*[@id="__layout"]/div/section/div/div[1]/div[3]/h1')
        return name.text

# Ignite, Chapter 1 - How to Get Started With SmartTrader
    def chapter1_video1(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath('//*[@id="__layout"]'
                                         '/div/section/section[2]/div/section[1]/div/div[1]/div/div[1]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath('//*[@id="__layout"]'
                                             '/div/section/section[2]/div/section[1]/div/div[1]/div/div[1]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter1_video1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[1]/h5/a').click()

    def chapter1_video2(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[2]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[2]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter1_video2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[2]/h5/a').click()

    def chapter1_video3(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[3]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[3]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter1_video3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[3]/h5/a').click()

    def chapter1_video4(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[4]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[4]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter1_video4_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[1]/div/div[1]/div/div[4]/h5/a').click()

# Ignite, Chapter 2 - Understanding Toolbars and How to Customize Them
    def chapter2_video1(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[1]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[1]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[1]/h5/a').click()

    def chapter2_video2(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[2]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[2]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[2]/h5/a').click()

    def chapter2_video3(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[3]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[3]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[3]/h5/a').click()

    def chapter2_video4(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[4]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[4]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video4_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[4]/h5/a').click()

    def click_swiper_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[3]').click()
        time.sleep(2)

    def chapter2_video5(self):
        wd = self.app.wd
        self.click_swiper_2()
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[5]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[5]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video5_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[5]/h5/a').click()

    def chapter2_video6(self):
        wd = self.app.wd
        self.click_swiper_2()
        self.click_swiper_2()
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[6]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[6]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video6_6(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[6]/h5/a').click()

    def chapter2_video7(self):
        wd = self.app.wd
        self.click_swiper_2()
        self.click_swiper_2()
        self.click_swiper_2()
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[7]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[7]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter2_video7_7(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[2]/div/div[1]/div/div[7]/h5/a').click()

# Ignite, Chapter 3 - Understanding Indicators, Templates, and Tracking
    def chapter3_video1(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[1]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[1]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter3_video1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[1]/h5/a').click()

    def chapter3_video2(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[2]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[2]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter3_video2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[2]/h5/a').click()

    def chapter3_video3(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[3]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[3]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter3_video3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[3]/h5/a').click()

    def chapter3_video4(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[4]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[4]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter3_video4_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[3]/div/div[1]/div/div[4]/h5/a').click()

# Ignite, Chapter 4 - How to Use SmartTrader Alerts With Trading
    def chapter4_video1(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[1]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[1]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter4_video1_1(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[1]/h5/a').click()

    def chapter4_video2(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[2]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[2]/h5/a')
            return re.sub('[?]', '', name1.text)
        else:
            return print('error')

    def chapter4_video2_2(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[2]/h5/a').click()

    def chapter4_video3(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[3]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath(
                '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[3]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter4_video3_3(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            '//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[1]/div/div[3]/h5/a').click()

    def chapter4_video4(self):
        wd = self.app.wd
        name = wd.find_elements_by_xpath('//*[@id="__layout"]'
                                         '/div/section/section[2]/div/section[4]/div/div[1]/div/div[4]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath('//*[@id="__layout"]'
                                             '/div/section/section[2]/div/section[4]/div/div[1]/div/div[4]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter4_video4_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="__layout"]'
                                 '/div/section/section[2]/div/section[4]/div/div[1]/div/div[4]/h5/a').click()

    def click_swiper_4(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="__layout"]/div/section/section[2]/div/section[4]/div/div[3]').click()
        time.sleep(2)

    def chapter4_video5(self):
        wd = self.app.wd
        self.click_swiper_4()
        name = wd.find_elements_by_xpath('//*[@id="__layout"]'
                                         '/div/section/section[2]/div/section[4]/div/div[1]/div/div[5]/h5/a')
        if name:
            name1 = wd.find_element_by_xpath('//*[@id="__layout"]'
                                             '/div/section/section[2]/div/section[4]/div/div[1]/div/div[5]/h5/a')
            return name1.text
        else:
            return print('error')

    def chapter4_video5_5(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="__layout"]'
                                 '/div/section/section[2]/div/section[4]/div/div[1]/div/div[5]/h5/a').click()
