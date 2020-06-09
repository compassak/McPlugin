import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from enshrinePage import enshrine
from loginPage import login
from models import baseUnit, function
import unittest


class viewEnshrineTest(baseUnit.BaseTest):
    """用户查看收藏测试"""

    def view_enshrine_verify(self):
        enshrine(self.driver).view_enshrine()

    def test_view_integral(self):
        """用户查看积分"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_enshrine_verify()
        eh= enshrine(self.driver)
        self.assertEqual(eh.open_enshrine(), "删除")
        function.print_screen(self.driver, 'view_enshrine.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
