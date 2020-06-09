import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
import time
from base import Page
from loginPage import login
from selenium import webdriver


class privacyFilter(Page):
    """用户隐私过滤界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=privacy'
        self.filter_selector_loc = (By.NAME, 'privacy[view][friend]')
        self.filter_selector_public_loc = (By.CSS_SELECTOR, 'option:nth-child(1)')
        self.filter_selector_friends_loc = (By.CSS_SELECTOR, 'option:nth-child(2)')
        self.filter_selector_private_loc = (By.CSS_SELECTOR, 'option:nth-child(3)')
        self.filter_selector_register_loc = (By.CSS_SELECTOR, 'option:nth-child(4)')
        self.submit_button_loc = (By.CSS_SELECTOR, '.pn')

    def setFilter(self, option):
        self.find_element(*self.filter_selector_loc).click()
        if option == '公开':
            self.find_element(*self.filter_selector_public_loc).click()
        elif option == '好友可见':
            self.find_element(*self.filter_selector_friends_loc).click()
        elif option == '保密':
            self.find_element(*self.filter_selector_private_loc).click()
        elif option == '仅注册用户可见':
            self.find_element(*self.filter_selector_register_loc).click()

    def getFilter(self):
        filter_selector = self.find_element(*self.filter_selector_loc)
        options = filter_selector.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.is_selected():
                return option.text

    def submit_button(self):
        self.find_element(*self.submit_button_loc).click()

    def select_filter(self, option):
        self.open()
        self.setFilter(option)
        self.submit_button()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    pf = privacyFilter(driver)
    lo.user_login(username, password)
    pf.select_filter("好友可见")
    time.sleep(1)
    print(pf.getFilter())
    lo.logout()
