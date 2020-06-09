import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from privacyFilterPage import privacyFilter
from loginPage import login
from models import baseUnit, function
import unittest
import time


class privacyFilterTest(baseUnit.BaseTest):
    """用户选择主页隐私权限测试"""

    def select_filter_verify(self,option):
        privacyFilter(self.driver).select_filter(option)

    def test_view_integral1(self):
        """不选择"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.select_filter_verify('')
        time.sleep(1)
        pf = privacyFilter(self.driver)
        self.assertEqual(pf.getFilter(), pf.getFilter())
        function.print_screen(self.driver, 'no_select_privacy_strategy.png')
        lo.logout()

    def test_view_integral2(self):
        """选择主页为公开"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.select_filter_verify('公开')
        time.sleep(1)
        pf = privacyFilter(self.driver)
        self.assertEqual(pf.getFilter(), '公开')
        function.print_screen(self.driver, 'select_privacy_strategy_public.png')
        lo.logout()

    def test_view_integral3(self):
        """选择主页为好友可见"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.select_filter_verify('好友可见')
        time.sleep(1)
        pf = privacyFilter(self.driver)
        self.assertEqual(pf.getFilter(), '好友可见')
        function.print_screen(self.driver, 'select_privacy_strategy_friends.png')
        lo.logout()

    def test_view_integral4(self):
        """选择主页为保密"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.select_filter_verify('保密')
        time.sleep(1)
        pf = privacyFilter(self.driver)
        self.assertEqual(pf.getFilter(), '保密')
        function.print_screen(self.driver, 'select_privacy_strategy_private.png')
        lo.logout()

    def test_view_integral5(self):
        """选择主页为注册用户可见"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.select_filter_verify('仅注册用户可见')
        time.sleep(1)
        pf = privacyFilter(self.driver)
        self.assertEqual(pf.getFilter(), '仅注册用户可见')
        function.print_screen(self.driver, 'select_privacy_strategy_register.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
