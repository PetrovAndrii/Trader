from datetime import datetime
import string
import random

from selenium.webdriver.common.by import By

from constants.charts import ChartsConstants


class CommonHelper:

    def __init__(self, app):
        self.app = app

    def get_current_date_time(self):
        date_time = datetime.now()
        return date_time.strftime('%Y-%m-%d %H.%M.%S')

    def random_symbol(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def open_trading_panel(self):
        wd = self.app.wd
        if not wd.find_elements(By.CLASS_NAME, ChartsConstants.TRADING_PANEL_OPEN_CLASS_NAME):
            wd.find_element(By.ID, ChartsConstants.TRADING_PANEL_ARROW_BUTTON_ID).click()
        else:
            pass

    def close_trading_panel(self):
        wd = self.app.wd
        if wd.find_elements(By.CLASS_NAME, ChartsConstants.TRADING_PANEL_OPEN_CLASS_NAME):
            wd.find_element(By.ID, ChartsConstants.TRADING_PANEL_ARROW_BUTTON_ID).click()
        else:
            pass
