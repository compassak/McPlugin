import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from postingPage import posting
from loginPage import login
from models import baseUnit, function
import unittest


class postingTest(baseUnit.BaseTest):
    """用户发帖测试"""

    def user_posting_verify(self, row):
        posting(self.driver, row).user_posting()

    def test_posting1(self):
        """发布空贴"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = posting(self.driver, 4)
        self.user_posting_verify(4)
        self.assertEqual('', '')
        function.print_screen(self.driver, 'posting_empty_post.png')
        lo.logout()

    def test_posting2(self):
        """发布资源贴"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = posting(self.driver, 3)
        self.user_posting_verify(3)
        self.assertEqual('', '')
        function.print_screen(self.driver, 'posting_source_post.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
