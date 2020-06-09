import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from loginPage import login
from base import Page
from time import sleep
from selenium import webdriver


class modifyBase(Page):
    """
    用户基本信息修改界面类
    """

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp'
        self.modify_gender_loc = (By.ID, "gender")  # 性别
        self.modify_gender_man_loc = (By.XPATH, "//option[. = '男']")
        self.modify_gender_woman_loc = (By.XPATH, "//option[. = '女']")
        self.modify_gender_secret_loc = (By.XPATH, "//option[. = '保密']")
        self.modify_qq_loc = (By.ID, "qq")  # qq号码
        self.modify_intro_loc = (By.ID, "bio")  # 个人简介
        self.modify_sight_message_loc = (By.ID, "sightmlmessage")  # 个性签名
        self.modify_submit_button_loc = (By.CSS_SELECTOR, "#profilesubmitbtn > strong")

    def modify_gender(self, gender):
        gender_selector = self.find_element(*self.modify_gender_loc)
        gender_selector.click()
        if gender == '男':
            gender_selector.find_element(*self.modify_gender_man_loc).click()
        elif gender == '女':
            gender_selector.find_element(*self.modify_gender_woman_loc).click()
        elif gender == '保密':
            gender_selector.find_element(*self.modify_gender_secret_loc).click()

    def modify_qqNumber(self, qq):
        self.find_element(*self.modify_qq_loc).clear()
        self.find_element(*self.modify_qq_loc).send_keys(qq)

    def modify_intro(self, intro):
        self.find_element(*self.modify_intro_loc).clear()
        self.find_element(*self.modify_intro_loc).send_keys(intro)

    def modify_sight_message(self, message):
        self.find_element(*self.modify_sight_message_loc).clear()
        self.find_element(*self.modify_sight_message_loc).send_keys(message)

    def modify_submit(self):
        self.find_element(*self.modify_submit_button_loc).click()

    def get_gender(self):
        gender_selector = self.find_element(*self.modify_gender_loc)
        options = gender_selector.find_elements(By.TAG_NAME, 'option')
        for option in options:
            if option.is_selected():
                return option.text

    def get_qqNumber(self):
        return self.find_element(*self.modify_qq_loc).get_attribute('value')

    def get_intro(self):
        return self.find_element(*self.modify_intro_loc).text

    def get_message(self):
        return self.find_element(*self.modify_sight_message_loc).text

    def modify(self, gender, qq, intro, message):
        """统一修改个基本资料入口"""
        self.open()
        self.modify_gender(gender)
        self.modify_qqNumber(qq)
        self.modify_intro(intro)
        self.modify_sight_message(message)
        self.modify_submit()
        sleep(1)


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    modify = modifyBase(driver)
    lo.user_login(username,password)
    modify.modify('保密', '123456789', '6年mc老玩家', 'minecraft=a world')
    lo.logout()