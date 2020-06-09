import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/') + '/page_obj')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/models')

from friendsPage import friends
from loginPage import login
from models import baseUnit, function
import unittest


class friendChatTest(baseUnit.BaseTest):
    """用户好友聊天测试"""

    def friends_send_msg_verify(self, msg):
        friends(self.driver).friends_send_msg(msg)

    def test_friend_chat1(self):
        """不输入聊天内容"""
        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = friends(self.driver)
        self.friends_send_msg_verify('')
        # 抱歉，不能发送空消息
        self.assertEqual("", '')
        function.print_screen(self.driver, 'no_send_msg_to_friend.png')
        lo.logout()

    def test_friend_chat2(self):
        """发送加粗，带颜色文本信息"""

        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = friends(self.driver)
        self.friends_send_msg_verify('[b]111[/b][color=Yellow]222[/color]')
        self.assertEqual(fd.get_send_msg_hint(), '')
        function.print_screen(self.driver, 'send_strong_colorful_text.png')
        lo.logout()

    def test_friend_chat3(self):
        """发送图片"""

        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = friends(self.driver)
        self.friends_send_msg_verify(
                '[img]https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570351870251&di=79e87fc4c4321239823199139703d1b6&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20161112%2F19746e11a7fd4d9ba9ac4b45e5c8e5c8_th.jpeg[/img]')
        self.assertEqual(fd.get_send_msg_hint(), '')
        function.print_screen(self.driver, 'send_img.png')
        lo.logout()

    def test_friend_chat4(self):
        """发送代码，表情"""

        lo = login(self.driver)
        lo.user_login(self.username, self.password)
        fd = friends(self.driver)
        self.friends_send_msg_verify('[code]print("你是铁憨憨！")[/code]\n{:5_131:}{:5_131:}')
        self.assertEqual(fd.get_send_msg_hint(), '')
        function.print_screen(self.driver, 'send_code_face.png')
        lo.logout()


if __name__ == '__main__':
    unittest.main()
