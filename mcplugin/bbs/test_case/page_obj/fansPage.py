import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class fans(Page):
    """用户粉丝界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=follow&do=follower'
        self.no_fans_hint_loc = (By.CSS_SELECTOR, '.xi2')

    def open_fans_page(self):
        return self.find_element(*self.no_fans_hint_loc).text

    def view_fans(self):
        """查看粉丝统一入口"""
        self.open()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)

    fa = fans(driver)
    lo.user_login(username, password)

    fa.view_fans()
    sleep(1)
    print(fa.open_fans_page())
    lo.logout()
