import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class friends(Page):
    """用户好友界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=space&do=friend'
        self.friend_interaction_button_loc = (By.XPATH, '//div[2]/a[2]')
        self.send_msg_button_loc = (By.XPATH, '//p[4]/a')
        self.msg_input_loc = (By.CSS_SELECTOR, '#pmmessage')
        self.submit_button_loc = (By.CSS_SELECTOR, '#pmsubmit_btn > strong')
        self.show_hint_Box = (By.CSS_SELECTOR, '#return_showMsgBox')

    def mouse_over_interaction(self):
        interaction = self.find_element(*self.friend_interaction_button_loc)
        ActionChains(self.driver).move_to_element(interaction).perform()

    def open_send_msg_window(self):
        self.find_element(*self.send_msg_button_loc).click()

    def set_msg(self, msg):
        self.find_element(*self.msg_input_loc).send_keys(msg)

    def get_send_msg_hint(self):
        return self.find_element(*self.show_hint_Box).text

    def submit_msg(self):
        self.find_element(*self.submit_button_loc)

    def friends_send_msg(self, msg):
        """查看粉丝统一入口"""
        self.open()
        self.mouse_over_interaction()
        self.open_send_msg_window()
        self.set_msg(msg)
        self.submit_msg()


if __name__ == '__main__':
    username = 'm4044'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)

    fd = friends(driver)
    lo.user_login(username, password)

    fd.friends_send_msg("1")
    sleep(1)
    print(fd.get_send_msg_hint(), type(fd.get_send_msg_hint()))
    lo.logout()
