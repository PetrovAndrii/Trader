import time
from random import randint
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException


class SharingHelper:

    def __init__(self, app):
        self.app = app

    def share_ideas_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.scxToolbarButton-dropdownElement__icon.ucpicon-share').click()
        time.sleep(1)

    def share_charts_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div[data-scxvalue="share-chart"]').click()
        time.sleep(2)
        if wd.find_elements_by_css_selector('.bootbox-body'):
            element = wd.find_element_by_css_selector('.bootbox-body')
            return print(element.text)
        else:
            pass

    def share_workspace_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div[data-scxvalue="share-wsp"]').click()
        if wd.find_elements_by_css_selector('.bootbox-body'):
            element = wd.find_element_by_css_selector('.bootbox-body')
            return print(element.text)
        else:
            pass

    def browse_ideas(self):
        wd = self.app.wd
        new_window_url = wd.find_element_by_xpath('//*[@title="Browse Ideas"]').get_attribute("href")
        wd.get(new_window_url)
        # wd.find_element_by_xpath('//*[@title="Browse Ideas"]').click()
        try:
            Alert(wd).accept()
        except (UnexpectedAlertPresentException, NoAlertPresentException):
            pass
        time.sleep(3)

    def browse_scripts(self):
        wd = self.app.wd
        new_window_url = wd.find_element_by_xpath('//*[@title="Browse Scripts"]').get_attribute("href")
        wd.get(new_window_url)
        # wd.find_element_by_xpath('//*[@title="Browse Scripts"]').click()
        try:
            Alert(wd).accept()
        except (UnexpectedAlertPresentException, NoAlertPresentException):
            pass
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

    def open_manage_shared_ideas_scripts(self):
        wd = self.app.wd
        self.share_ideas_button()
        wd.find_element_by_css_selector('div[data-scxvalue="manage-shared"]').click()

    def check_shared_ideas(self, name_shared_ideas):
        wd = self.app.wd
        time.sleep(3)
        self.open_manage_shared_ideas_scripts()
        time.sleep(3)
        name = wd.find_element_by_xpath('//*[contains(text(), "' + name_shared_ideas + '")]')
        return name.text

    def import_random_workspace_button(self):
        wd = self.app.wd
        self.app.wait_element_located_xpath('//div[@class="wspsViewST thumbnail"]')
#        time.sleep(3)
        links = wd.find_elements_by_xpath('//div[@class="wspsViewST thumbnail"]')
        link = links[randint(0, len(links) - 1)]
        wd.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()
        name = link.find_element_by_xpath('//*[@class="ideas_title"]')
        name1 = str(name.text)
        self.import_button_from_opened_ideas()
        return name1.upper()

    def import_button_from_opened_ideas(self):
        wd = self.app.wd
        # scroll to element
        element = wd.find_element_by_xpath('//*[@class="ideas_footer_import"]')
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_xpath('//*[@class="ideas_footer_import"]').click()

    def import_random_chart_button(self):
        wd = self.app.wd
        time.sleep(3)
        links = wd.find_elements_by_xpath('//div[@class="chartsViewST thumbnail"]')
        link = links[randint(0, len(links) - 1)]
        link.click()
        name = link.find_element_by_xpath('//*[@class="ideas_title"]')
        name1 = str(name.text)
        self.import_button_from_opened_ideas()
        return name1.upper()

    def return_imported_name(self):
        wd = self.app.wd
        time.sleep(15)
        name = wd.find_element_by_xpath('//*[@class="workspace__open-btn"]/span[2]')
        return name.text

    def open_scripting_tab(self):
        wd = self.app.wd
        if not wd.find_elements_by_class_name('tradingPanelOpened'):
            self.app.common.open_trading_panel()
            wd.find_element_by_class_name('scriptingTab').click()
        else:
            wd.find_element_by_class_name('scriptingTab').click()

    def open_user_smart_script(self):
        wd = self.app.wd
        wd.find_element_by_class_name('openBtn').click()

    def open_my_smart_scripts_tab(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('ul.ModalTabs > li:nth-child(3)').click()

    def smart_script_share_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.DropdownActions').click()
        wd.find_element_by_xpath('//*[@class="DropdownActions__options"]/li[2]').click()

    def import_random_scripts_button(self):
        wd = self.app.wd
        element = wd.find_element_by_class_name('noSearchResults')
        if element.is_displayed():
            print('No Search Results')
        else:
            time.sleep(3)
            links = wd.find_elements_by_xpath('//div[@class="scriptViewST thumbnail"]')
            link = links[randint(0, len(links) - 1)]
            wd.execute_script("arguments[0].scrollIntoView(true);", link)
            link.click()
            name = link.find_element_by_xpath('//*[@class="ideas_title"]')
            name1 = name.text
            wd.find_element_by_xpath('//*[@class="ideas_footer_import"]').click()
            return name1

    def return_imported_script_name(self):
        wd = self.app.wd
        time.sleep(3)
        if wd.find_elements_by_class_name('noSearchResults'):
            print('No Search Results')
        else:
            self.app.wait_element_located_class_name('SSListItem')
            self.open_my_smart_scripts_tab()
            # to get a new script, sort by new ones and take the second script from the list
            #  (the first one as a favorite for sharing)
            self.click_sort_button()
            self.sort_by_newest()
            time.sleep(3)
            name = wd.find_element_by_xpath('//*[@class="SmartScriptModal__list-inner-container"]/div[1]/div/div[1]')
            return name.text

    def click_sort_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('div.SortButton').click()

    def sort_by_newest(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('ul.SortButton__list > li:nth-child(2)').click()

    def sort_by_oldest(self):
        wd = self.app.wd
        self.click_sort_button()
        wd.find_element_by_css_selector('ul.SortButton__list > li:nth-child(1)').click()

    def remove_random_sharing_ideas(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath('//*[@title="Delete workspace"]'):
            links = wd.find_elements_by_xpath('//*[@title="Delete workspace"]')
            link = links[randint(0, len(links) - 1)]
            link.click()
        else:
            return print('HAVE NOT IDEAS FOR DELETE')

    def get_shared_ideas_scripts_list(self):
        wd = self.app.wd
        count = []
        time.sleep(5)
        for element in wd.find_elements_by_xpath('//*[@title="Delete workspace"]'):
            count.append(element)
        return count

    def random_view_on_social_hub(self):
        wd = self.app.wd
        time.sleep(5)
        if wd.find_elements_by_xpath('//*[@class="viewOnHub pull-right"]'):
            links = wd.find_elements_by_xpath('//*[@class="viewOnHub pull-right"]')
            link = links[randint(0, len(links) - 1)]
            link.click()
            try:
                Alert(wd).accept()
            except (UnexpectedAlertPresentException, NoAlertPresentException):
                pass
            time.sleep(5)
        else:
            return print('HAVE NOT IDEAS FOR VIEW')

    def button_share_into_social_on_footer(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@class="detail-idea-footer"]')
        # scroll to element
        wd.execute_script("return arguments[0].scrollIntoView(true);", element)
        wd.find_element_by_xpath('//*[@class="detail-idea-footer"]/div[2]').click()

    def button_share_into_social_on_ideas(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="ideas_share"]').click()

    def open_workspace_list(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="workspace__open-btn"]').click()

    def open_setting_active_workspaces(self):
        wd = self.app.wd
        wd.find_element_by_id('activeWsp').click()
        wd.find_element_by_xpath('//*[@id="activeWsp"]/a/div[2]/span[1]').click()

    def click_share_button_on_ws_settings(self):
        wd = self.app.wd
        self.app.wait_element_located_xpath('//*[@id="activeWsp"]/ul/li[3]')
        wd.find_element_by_xpath('//*[@id="activeWsp"]/ul/li[3]').click()

    def share_workspace_from_settings(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('.item--share').click()
