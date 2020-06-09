import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class permission(Page):
    """
    用户权限界面类
    """

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=usergroup&do=forum'
        self.section_name_loc = (By.CSS_SELECTOR, '.xw1:nth-child(1)')

    def section_name(self):
        return self.find_element(*self.section_name_loc).text

    def view_permission(self):
        self.open()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    pn = permission(driver)
    lo.user_login(username, password)
    pn.view_permission()
    sleep(1)
    print(pn.section_name())
    lo.logout()
