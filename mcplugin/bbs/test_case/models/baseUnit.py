import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from driver import getDriver
import unittest


class BaseTest(unittest.TestCase):
    """基础测试类"""

    username = 'minecraft_ak'
    password = '2438675akkl'

    def runTest(self):
        assert (True == True)

    def setUp(self):
        self.driver = getDriver("FireFox")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    test = BaseTest()
