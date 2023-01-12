import time

from selenium.webdriver.common.by import By


class SmartHubHelper:

    def __init__(self, app):
        self.app = app

    def open_smart_hub(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "div.landing-header__nav-link-wrap").click()
        time.sleep(1)
        element = wd.find_element(By.CSS_SELECTOR, '.landing-header__more-dropdown')
        element.find_element(By.LINK_TEXT, 'Smart Hub').click()

    def click_tutorials(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[1]/div[4]/a/button').click()

    def click_blog(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[2]/div[4]/a/button').click()

    def click_knowledge_base(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[3]/div[4]/a/button').click()

    def click_ideas_community(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[4]/div[4]/a/button').click()

    def click_trading_rooms(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[5]/div[4]/a/button').click()

    def click_marketplace(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="__layout"]'
                                  '/div/section/section[2]/div/div/div/div[6]/div[4]/a/button').click()
        time.sleep(1)
