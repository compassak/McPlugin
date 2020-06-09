import sys
import os
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from modifyIconPage import modifyIcon
from loginPage import login
from models import baseUnit, function
import unittest
import time


class modifyIconTest(baseUnit.BaseTest):
    """用户头像修改测试"""

    iconPath = ''
    # 判断是模块内调用还是模块外调用
    if 'test_case' in os.path.abspath('./'):
        iconPath = str(os.path.abspath('./').replace('/', '\\').split('test_case')[0]) + "report\\images\\icon.jpg"
    else:
        iconPath = str(os.path.abspath('./').replace('/', '\\')) + "\\bbs\\report\\images\\icon.jpg"

    def modify_icon_select_size_verify(self, icon_path=iconPath):
        modifyIcon(self.driver).modify_icon(icon_path)

    def modify_icon_no_select_size_verify(self, icon_path=iconPath):
        modifyIcon(self.driver).modify_icon_no_select_size(icon_path)

    def test_modify1(self):
        """修改头像不选择图像大小"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        self.modify_icon_no_select_size_verify(self.iconPath)
        time.sleep(1)
        mo = modifyIcon(self.driver)
        self.assertEqual(mo.modify_success_hint(), '完成')
        function.print_screen(self.driver, "modify_icon_no_select_size.png")
        lo.logout()

    def test_modify2(self):
        """修改头像选择合适大小"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        self.modify_icon_select_size_verify(self.iconPath)
        time.sleep(1)
        mo = modifyIcon(self.driver)
        self.assertEqual(mo.modify_success_hint(), '完成')
        function.print_screen(self.driver, "modify_icon_select_size.png")
        lo.logout()


if __name__ == '__main__':
    unittest.main()
