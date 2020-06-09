import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from models import baseUnit, function
from base import Page
import unittest
import time


class viewPosTest(baseUnit.BaseTest):
    """用户浏览帖子测试"""

    bbs_new_post_model_loc = (By.CSS_SELECTOR, '#tablink1')
    bbs_new_post_loc = (By.CSS_SELECTOR, '#tabcontent1 .topRank:nth-child(1) > a')
    post_open_hint_loc = (By.CSS_SELECTOR, 'label.z')

    def post_open(self):
        return self.driver.find_element(*self.post_open_hint_loc).text

    def view_new_post_verify(self):
        index = Page(self.driver)
        index.open()
        actions = ActionChains(self.driver)
        actions.click_and_hold(index.find_element(*self.bbs_new_post_model_loc)).perform()
        index.find_element(*self.bbs_new_post_loc).click()

    def test_view_new_post(self):
        """浏览最新帖子"""
        self.view_new_post_verify()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到新打开的标签页
        self.assertEqual(self.post_open(), '电梯直达')
        function.print_screen(self.driver, 'view_new_post.png')


if __name__ == '__main__':
    unittest.main()
