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