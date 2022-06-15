from datetime import datetime
import string
import random


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
        if not wd.find_elements_by_class_name('tradingPanelOpened'):
            wd.find_element_by_id('tradingPopUp_arrowId').click()
        else:
            pass

    def close_trading_panel(self):
        wd = self.app.wd
        if wd.find_elements_by_class_name('tradingPanelOpened'):
            wd.find_element_by_id('tradingPopUp_arrowId').click()
        else:
            pass
