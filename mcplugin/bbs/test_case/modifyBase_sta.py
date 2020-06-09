import sys
import os
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from modifyBasePage import modifyBase
from loginPage import login
from models import baseUnit, function
import unittest
import time


class modifyBaseTest(baseUnit.BaseTest):
    """用户基本信息修改测试"""

    def modify_base_verify(self, gender, qq, intro, message):
        modifyBase(self.driver).modify(gender, qq, intro, message)

    def test_modify1(self):
        """只填写性别"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        
        self.modify_base_verify('男', '', '', '')
        time.sleep(3)
        mof = modifyBase(self.driver)
        self.assertEqual(mof.get_gender(), "男")
        function.print_screen(self.driver, 'only_send_gender.png')
        lo.logout()

    def test_modify2(self):
        """只填写qq号码"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.modify_base_verify('', '123123123', '', '')
        time.sleep(3)
        mof = modifyBase(self.driver)
        self.assertEqual(mof.get_qqNumber(), "123123123")
        function.print_screen(self.driver, 'only_send_qqNumber.png')
        lo.logout()

    def test_modify3(self):
        """只填写用户简介"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.modify_base_verify('', '', '6年我的世界老玩家啊', '')
        time.sleep(3)
        mof = modifyBase(self.driver)
        self.assertEqual(mof.get_intro(), "6年我的世界老玩家啊")
        function.print_screen(self.driver, 'only_send_intro.png')
        lo.logout()

    def test_modify4(self):
        """只填写用户个性签名"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.modify_base_verify('', '', '', 'minecraft=a world')
        time.sleep(3)
        mof = modifyBase(self.driver)
        self.assertEqual(mof.get_message(), "minecraft=a world")
        function.print_screen(self.driver, 'only_send_message.png')
        lo.logout()

    def test_modify5(self):
        """填写所有基本信息"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)

        self.modify_base_verify('男', '123123123', '6年我的世界老玩家啊', 'minecraft=a world')
        time.sleep(3)
        mof = modifyBase(self.driver)
        self.assertEqual(mof.get_gender(), "男")
        self.assertEqual(mof.get_qqNumber(), "123123123")
        self.assertEqual(mof.get_intro(), "6年我的世界老玩家啊")
        self.assertEqual(mof.get_message(), "minecraft=a world")
        function.print_screen(self.driver, 'all_send.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
