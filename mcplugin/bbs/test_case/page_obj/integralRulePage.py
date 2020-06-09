import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from loginPage import login
from selenium import webdriver


class integralRule(Page):
    """用户积分规则界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=credit&op=rule'
        self.integral_action_name_loc = (By.CSS_SELECTOR, 'th.xw1:nth-child(1)')
        self.integral_rule_filter_loc = (By.CSS_SELECTOR, 'li.y > select:nth-child(1)')
        self.integral_rule_wfrk_loc = (
            By.CSS_SELECTOR, 'li.y > select:nth-child(1) > optgroup:nth-child(2) > option:nth-child(1)')
        self.integral_rule_hcxl_loc = (
            By.CSS_SELECTOR, 'li.y > select:nth-child(1) > optgroup:nth-child(3) > option:nth-child(2)')

    def integral_action_name(self):
        return self.find_element(*self.integral_action_name_loc).text

    def select_rule_filter(self, ruleCategories):
        self.find_element(*self.integral_rule_filter_loc).click()
        if ruleCategories == '万服入口':
            self.find_element(*self.integral_rule_wfrk_loc).click()
        elif ruleCategories == '喝茶闲聊':
            self.find_element(*self.integral_rule_hcxl_loc).click()
        else:
            self.find_element(*self.integral_rule_wfrk_loc).click()

    def view_integral_rule_all(self):
        self.open()

    def view_integral_rule_on_filter(self, ruleCategories):
        self.open()
        self.select_rule_filter(ruleCategories)


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    ir = integralRule(driver)
    lo.user_login(username, password)
    ir.view_integral_rule_on_filter('喝茶闲聊')
    print(ir.integral_action_name())
    lo.logout()
