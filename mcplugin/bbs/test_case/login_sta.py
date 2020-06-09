import sys
import os
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from loginPage import login
from models import baseUnit, function
import unittest
import time


class loginTest(baseUnit.BaseTest):
    """论坛登陆测试"""

    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名，密码为空登陆"""
        self.user_login_verify()
        lo = login(self.driver)
        self.assertEqual(lo.login_error(), "抱歉，密码空或包含非法字符")
        function.print_screen(self.driver, 'uname_pword_empty.png')

    def test_login2(self):
        """用户名为空登陆"""
        self.user_login_verify(password="123456")
        lo = login(self.driver)
        self.assertEqual(lo.login_error(), "抱歉，用户名为空")
        function.print_screen(self.driver, 'uname_empty.png')

    def test_login3(self):
        """密码为空登陆"""
        self.user_login_verify(username='minecraft')
        lo = login(self.driver)
        self.assertEqual(lo.login_error(), "抱歉，密码为空")
        function.print_screen(self.driver, 'pword_empty.png')

    def test_login4(self):
        """用户名密码不匹配登陆"""
        self.user_login_verify(username="minecraft", password="123456")
        lo = login(self.driver)
        self.assertEqual(lo.login_error(), "用户名或密码错误")
        function.print_screen(self.driver, 'uname_pword_error.png')

    def test_login5(self):
        """用户名密码正确"""
        self.user_login_verify(username=self.username, password=self.password)
        time.sleep(3)
        lo = login(self.driver)
        self.assertEqual(lo.login_success(), "minecraft_ak")
        function.print_screen(self.driver, 'uname_pword_true.png')
        lo.logout()


if __name__ == "__main__":
    unittest.main()
