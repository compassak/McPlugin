import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from permissionPage import permission
from loginPage import login
from models import baseUnit, function
import unittest


class viewPermissionTest(baseUnit.BaseTest):
    """用户查看个人权限测试"""

    def view_permission_verify(self):
        permission(self.driver).view_permission()

    def test_view_permission(self):
        """用户查看权限"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.view_permission_verify()
        pn = permission(self.driver)
        self.assertEqual(pn.section_name(), "版块名称")
        function.print_screen(self.driver, 'view_permission.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()