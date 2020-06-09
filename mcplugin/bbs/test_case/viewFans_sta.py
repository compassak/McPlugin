import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from fansPage import fans
from loginPage import login
from models import baseUnit, function
import unittest


class viewFansTest(baseUnit.BaseTest):
    """用户查看收藏测试"""

    def view_enshrine_verify(self):
        fans(self.driver).view_fans()

    def test_view_integral(self):
        """用户查看积分"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_enshrine_verify()
        fa= fans(self.driver)
        self.assertEqual(fa.open_fans_page(), "发动态")
        function.print_screen(self.driver, 'view_fans.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()