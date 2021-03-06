import time
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

    def manage_workspaces_option(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.pvtwspdropdown').click()

    def share_private_workspace(self):
        wd = self.app.wd
        wd.find_element_by_class_name('btn-sharePrivate').click()
        time.sleep(2)

    def add_new_workspace(self):
        wd = self.app.wd
        wd.find_element_by_id('addNewWSP').click()
        time.sleep(2)

    def add_new_chart(self):
        wd = self.app.wd
        wd.find_element_by_id('addNewChartToWSP').click()
        time.sleep(2)

    def enter_workspace_name(self, workspace_name):
        wd = self.app.wd
        wd.find_element_by_id('newWspName').click()
        wd.find_element_by_id('newWspName').clear()
        wd.find_element_by_id('newWspName').send_keys(workspace_name)

    def choose_random_forex_symbol_workspace(self):
        wd = self.app.wd
        wd.find_element_by_id('newChartModalSymbolSearch').click()
        wd.find_element_by_css_selector('.scxInstrumentSearchContainer.containerWorkspace ul li:nth-child(2)').click()
        links = wd.find_elements_by_css_selector('div[data-scxexchange="FOREX"]')
        link = links[randint(0, len(links) - 1)]
        time.sleep(2)
        wd.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(2)
        wd.execute_script("arguments[0].click();", link)

    def choose_random_forex_symbol_chart(self):
        wd = self.app.wd
        wd.find_element_by_id('newChartModalSymbolSearch').click()
        links = wd.find_elements_by_css_selector('div[data-scxexchange="FOREX"]')
        link = links[randint(0, len(links) - 1)]
        time.sleep(2)
        wd.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(2)
        wd.execute_script("arguments[0].click();", link)

    def choose_random_timing(self):
        pass

    def add_new_ideas_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[data-bb-handler="success"]').click()

    def open_workspace_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="workspace__open-btn"]').click()

    def get_workspace_list(self):
        wd = self.app.wd
        self.open_workspace_list()
        count = []
        time.sleep(3)
        if wd.find_elements_by_css_selector('li[role="option"]'):
            count = len(wd.find_elements_by_css_selector('li[role="option"]'))
        return count

    def close_workspace_list(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.ucpicon-close.close-dropdown').click()

    def choose_random_bars(self):
        wd = self.app.wd
        wd.find_element_by_id('newChartModalBarStyle').click()
        links = wd.find_elements_by_xpath('//*[@id="newChartModalBarStyle"]/div[2]//div')
        link = links[randint(0, len(links) - 1)]
        link.click()

    def get_charts_list(self):
        wd = self.app.wd
        count = []
        time.sleep(3)
        if wd.find_element_by_css_selector('.single-chart'):
            count = len(wd.find_elements_by_css_selector('.single-chart'))
        return count

    def open_random_private_workspaces(self):
        wd = self.app.wd
        time.sleep(3)
        if wd.find_elements_by_xpath('//span[@class="openPrivate"]'):
            links = wd.find_elements_by_xpath('//span[@class="openPrivate"]')
            link = links[randint(0, len(links) - 1)]
            name = link.text
            link.click()
            return name
        else:
            if wd.find_element_by_class_name('noWspFoundMsg'):
                error = wd.find_element_by_class_name('noWspFoundMsg')
                return error.text

    def return_imported_name(self):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element_by_xpath('//*[@class="workspace__open-btn"]/span[2]')
        return name.text

    def click_random_checkbox_in_manage_workspaces(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath('//*[@class="fake-checkbox cbxSelectPvtWsp"]'):
            links = wd.find_elements_by_xpath('//*[@class="fake-checkbox cbxSelectPvtWsp"]')
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            if wd.find_element_by_class_name('noWspFoundMsg'):
                error = wd.find_element_by_class_name('noWspFoundMsg')
                return error.text

    def click_random_checkbox_in_premium_manage_workspaces(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath('//*[@class="fake-checkbox cbxSelectPrmWsp"]'):
            links = wd.find_elements_by_xpath('//*[@class="fake-checkbox cbxSelectPrmWsp"]')
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            if wd.find_element_by_class_name('noWspFoundMsg'):
                error = wd.find_element_by_class_name('noWspFoundMsg')
                return error.text

    def manage_workspaces_click_import_button(self):
        wd = self.app.wd
        wd.find_element_by_id('btn-wsp-import-all').click()

    def manage_workspaces_click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_id('btn-wsp-delete-all').click()

    def open_tab_premium_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_id('premiumWSP').click()
        time.sleep(5)

    def open_random_premium_workspaces(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath('//span[@class="openPremium"]')
        link = links[randint(0, len(links) - 1)]
        name = link.text
        link.click()
        return name
