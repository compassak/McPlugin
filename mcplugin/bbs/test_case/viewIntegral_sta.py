import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from integralPage import integral
from loginPage import login
from models import baseUnit, function
import unittest


class viewIntegralTest(baseUnit.BaseTest):
    """用户查看积分测试"""

    def view_integral_verify(self):
        integral(self.driver).view_integral()

    def test_view_integral(self):
        """用户查看积分"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_integral_verify()
        inte = integral(self.driver)
        self.assertEqual(inte.integral_log(), "查看更多»\n积分记录")
        function.print_screen(self.driver, 'view_integral.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
