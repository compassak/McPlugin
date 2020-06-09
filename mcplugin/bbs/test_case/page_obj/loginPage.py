import sys
import os
sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from selenium import webdriver


class login(Page):
    """用户登陆界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/'
        self.login_username_loc = (By.NAME, 'username')
        self.login_password_loc = (By.NAME, 'password')
        self.login_button_loc = (By.CSS_SELECTOR, '.pn')
        self.login_submit_button_loc = (By.XPATH, '//strong')
        self.login_error_hint_loc = (By.XPATH, '//i')
        self.login_success_username_loc = (By.CSS_SELECTOR, '.vwmy > a:nth-child(1)')
        self.logout_button_loc = (By.XPATH, '//a[6]')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).click()
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).click()
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login_submit_button(self):
        self.find_element(*self.login_submit_button_loc).click()

    def user_login(self, username='', password=''):
        """统一登陆入口"""
        self.open()
        self.login_button()
        sleep(1)
        self.login_username(username)
        self.login_password(password)
        self.login_submit_button()
        sleep(1)

    def login_error(self):
        return self.find_element(*self.login_error_hint_loc).text

    def login_success(self):
        return self.find_element(*self.login_success_username_loc).text

    def logout(self):
        self.find_element(*self.logout_button_loc).click()


if __name__ == '__main__':
    user_login = login(webdriver.Firefox())
    user_login.user_login("minecraft_ak", "2438675akkl")
    sleep(5)
    print(user_login.login_success())
    user_login.logout()
    sleep(3)
    # print(user_login.login_error())
