import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class enshrine(Page):
    """用户收藏界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=space&do=favorite&type=all'
        self.open_enshrine_hint_loc = (By.LINK_TEXT, '删除')

    def open_enshrine(self):
        return self.find_element(*self.open_enshrine_hint_loc).text

    def view_enshrine(self):
        """查看收藏统一入口"""
        self.open()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)

    eh = enshrine(driver)
    lo.user_login(username, password)

    eh.view_enshrine()
    sleep(1)
    print(eh.open_enshrine())
    lo.logout()

