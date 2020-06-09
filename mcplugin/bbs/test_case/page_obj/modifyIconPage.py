import sys
import os
sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class modifyIcon(Page):
    """
    用户头像修改界面类
    """

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=avatar'
        self.select_img_button_loc = (By.ID, "avatarfile")
        self.size_selector_loc = (By.CSS_SELECTOR, ".ui-slider-handle")
        self.submit_button_loc = (By.NAME, "confirm")
        self.modify_success_hint_loc = (By.CSS_SELECTOR, '.finishbutton')

    def select_img(self, icon_path):
        self.find_element(*self.select_img_button_loc).send_keys(icon_path)

    def select_size(self):
        size_selector = self.find_element(*self.size_selector_loc)
        actions = ActionChains(self.driver)
        actions.click_and_hold(size_selector).perform()
        actions.drag_and_drop_by_offset(size_selector, -30, 0).perform()

    def submit_icon(self):
        self.find_element(*self.submit_button_loc).click()

    def modify_icon_no_select_size(self, icon_path):
        """修改头像不改变选择大小入口"""
        self.open()
        self.script("arguments[0].scrollIntoView(false);", self.find_element(*self.select_img_button_loc))
        self.select_img(icon_path)
        sleep(1)
        self.submit_icon()

    def modify_icon(self, icon_path):
        """修改头像不改变选择大小入口"""
        self.open()
        self.script("arguments[0].scrollIntoView(false);", self.find_element(*self.select_img_button_loc))
        self.select_img(icon_path)
        sleep(1)
        self.select_size()
        self.submit_icon()

    def modify_success_hint(self):
        return self.find_element(*self.modify_success_hint_loc).get_attribute('value')


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    micon = modifyIcon(driver)
    iconPath = str(os.path.abspath('./').replace('/', '\\').split('test_case')[0]) + "report\\images\\icon.jpg"
    lo.user_login(username, password)
    micon.modify_icon(iconPath)
    lo.logout()
