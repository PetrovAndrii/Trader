import time
from datetime import datetime
from random import randint


class WorkspaceChartHelper:

    def __init__(self, app):
        self.app = app

    def button_add_workspace_chart(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="app-header__top"]/div[3]').click()

    def manage_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="Manage Workspaces"]').click()

    def workspaces_option(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.pvtwspdropdown').click()

    def share_private_workspace(self):
        wd = self.app.wd
        wd.find_element_by_class_name('btn-sharePrivate').click()
        time.sleep(10)
