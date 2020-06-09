import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class integral(Page):
    """
    用户积分界面类
    """

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=credit&op=base'
        self.integral_log_loc = (By.CSS_SELECTOR, '.mbm')

    def integral_log(self):
        return self.find_element(*self.integral_log_loc).text

    def view_integral(self):
        self.open()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    inte = integral(driver)
    lo.user_login(username, password)
    inte.view_integral()
    sleep(1)
    print(inte.integral_log())
    lo.logout()
