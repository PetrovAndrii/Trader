import time
from datetime import datetime
from random import randint


class SharingHelper:

    def __init__(self, app):
        self.app = app

    def share_ideas_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//div[@title="Share Ideas"]').click()

    def share_charts_button(self):
        wd = self.app.wd
        wd.find_element_by_id('shareChartBtn').click()

    def share_workspace_button(self):
        wd = self.app.wd
        wd.find_element_by_id('shareWspBtn').click()

    def browse_ideas(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="Browse Ideas"]').click()
        time.sleep(3)

    def browse_scripts(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="Browse Scripts"]').click()
        time.sleep(3)

    def snapshot(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//button[@class="btnSnapshot btn btn-primary"]').click()
        time.sleep(5)
        element = wd.find_element_by_xpath('//*[@class="image-loader"]/div/div[5]/span[3]')
        if element.is_displayed():
            pass
        else:
            result_load_snapshot = wd.find_element_by_xpath('//*[@class="image-loader"]/div/div[5]')
            return result_load_snapshot.text

    def make_snapshot_chart(self):
        self.snapshot()

    def make_snapshot_workspace(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//button[@class="btnWSPSnapshot btn btn-primary"]').click()
        time.sleep(5)
        element = wd.find_element_by_xpath('//*[@class="image-loader"]/div/div[5]/span[3]')
        if element.is_displayed():
            pass
        else:
            result_load_snapshot = wd.find_element_by_xpath('//*[@class="image-loader"]/div/div[5]')
            return result_load_snapshot.text

    def make_snapshot_scripts(self):
        self.snapshot()

    def write_idea_name(self, idea_name):
        wd = self.app.wd
        wd.find_element_by_css_selector('.shareIdea_Title').click()
        wd.find_element_by_css_selector('.shareIdea_Title').clear()
        wd.find_element_by_css_selector('.shareIdea_Title').send_keys(idea_name)

    def write_description(self, description_text):
        wd = self.app.wd
        wd.find_element_by_id('descArea').click()
        wd.find_element_by_id('descArea').clear()
        wd.find_element_by_id('descArea').send_keys(description_text)

    def publish_idea(self):
        wd = self.app.wd
        wd.find_element_by_id('shareBtn').click()

    def get_current_date_time(self):
        date_time = datetime.now()
        return date_time.strftime('%Y-%m-%d %H.%M.%S')

    def open_manage_shared_ideas_scripts(self):
        wd = self.app.wd
        self.share_ideas_button()
        wd.find_element_by_xpath('//*[@title="Manage Shared Ideas & Scripts"]').click()

    def check_shared_ideas(self):
        wd = self.app.wd
        self.open_manage_shared_ideas_scripts()
        name = wd.find_element_by_xpath('//*[@id="bodyContentHolder"]/div[1]/div/div[1]')
        return name.text

    def import_random_workspace_button(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath('//div[@class="wspsViewST thumbnail"]')
        l = links[randint(0, len(links) - 1)]
        l.click()
        name = l.find_element_by_xpath('//*[@class="ideas_title"]')
        name1 = str(name.text)
        wd.find_element_by_xpath('//*[@class="ideas_footer_import"]').click()
        return name1.upper()

    def import_random_chart_button(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath('//div[@class="chartsViewST thumbnail"]')
        l = links[randint(0, len(links) - 1)]
        l.click()
        name = l.find_element_by_xpath('//*[@class="ideas_title"]')
        name1 = str(name.text)
        wd.find_element_by_xpath('//*[@class="ideas_footer_import"]').click()
        return name1.upper()

    def return_imported_name(self):
        wd = self.app.wd
        time.sleep(5)
        name = wd.find_element_by_xpath('//*[@class="workspace__open-btn"]/span[2]')
        return name.text

    def open_scripting_tab(self):
        wd = self.app.wd
        wd.find_element_by_class_name('scriptingTab').click()

    def open_user_smart_script(self):
        wd = self.app.wd
        wd.find_element_by_class_name('openBtn').click()

    def smart_script_share_button(self):
        wd = self.app.wd
        links = wd.find_elements_by_css_selector('.shareScriptBtn')
        l = links[randint(0, len(links) - 1)]
        l.click()

    def import_random_scripts_button(self):
        wd = self.app.wd
        links = wd.find_elements_by_xpath('//div[@class="scriptViewST thumbnail"]')
        l = links[randint(0, len(links) - 1)]
        l.click()
        name = l.find_element_by_xpath('//*[@class="ideas_title"]')
        name1 = name.text
        wd.find_element_by_xpath('//*[@class="ideas_footer_import"]').click()
        return name1

    def return_imported_script_name(self):
        wd = self.app.wd
        time.sleep(3)
        name = wd.find_element_by_xpath('//*[@id="runEADataTable"]/tbody/tr[last()]/td[1]/div/span[1]')
        return name.text

    def remove_random_sharing_ideas(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath('//*[@title="Delete workspace"]'):
            links = wd.find_elements_by_xpath('//*[@title="Delete workspace"]')
            l = links[randint(0, len(links) - 1)]
            l.click()
        else:
            return print('HAVE NOT IDEAS FOR DELETE')

    def get_shared_ideas_scripts_list(self):
        wd = self.app.wd
        count = []
        for element in wd.find_elements_by_xpath('//*[@title="Delete workspace"]'):
            count.append(element)
        return count
