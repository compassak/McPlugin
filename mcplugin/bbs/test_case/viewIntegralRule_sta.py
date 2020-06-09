import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from integralRulePage import integralRule
from loginPage import login
from models import baseUnit, function
import unittest


class viewIntegralRuleTest(baseUnit.BaseTest):
    """用户查看积分规则测试"""

    def view_integral_rule_verify(self, ruleCategories=None):
        if ruleCategories is None:
            integralRule(self.driver).view_integral_rule_all()
        else:
            integralRule(self.driver).view_integral_rule_on_filter(ruleCategories)

    def test_view_integral_rule1(self):
        """用户查看所有积分规则"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_integral_rule_verify()
        ir = integralRule(self.driver)
        self.assertEqual(ir.integral_action_name(), "动作名称")
        function.print_screen(self.driver, 'view_all_integral_rule.png')
        lo.logout()

    def test_view_integral_rule2(self):
        """用户查看筛选后积分规则"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_integral_rule_verify("喝茶闲聊")
        ir = integralRule(self.driver)
        self.assertEqual(ir.integral_action_name(), "动作名称")
        function.print_screen(self.driver, 'view_integral_rule_on_filter.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
