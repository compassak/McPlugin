import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from exchangeIntegralPage import exchangeIntegral
from loginPage import login
from models import baseUnit, function
import unittest


class exchangeIntegralTest(baseUnit.BaseTest):
    """用户积分兑换测试"""

    def exchange_integral_verify(self, amount, password):
        exchangeIntegral(self.driver).exchange_integral(amount, password)

    def test_exchange_integral1(self):
        """不输入兑换数量和密码"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        ei = exchangeIntegral(self.driver)
        self.exchange_integral_verify('', '')
        self.assertEqual(ei.exchange_hint(), '抱歉，您尚未输入需要兑换的数量')
        function.print_screen(self.driver, 'no_send_amount_password.png')
        lo.logout()

    def test_exchange_integral2(self):
        """不输入密码"""

        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        ei = exchangeIntegral(self.driver)
        self.exchange_integral_verify(2, '')
        self.assertEqual(ei.exchange_hint(), '抱歉，密码为空')
        function.print_screen(self.driver, 'no_send_password.png')
        lo.logout()

    def test_exchange_integral3(self):
        """输入兑换数量，密码"""

        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        ei = exchangeIntegral(self.driver)
        self.exchange_integral_verify(2, self.password)
        self.assertEqual(ei.exchange_hint(), '抱歉，兑换后金块不足 0')
        function.print_screen(self.driver, 'send_amount_password.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
