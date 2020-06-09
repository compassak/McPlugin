import os
import sys
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/bbs/test_case')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/bbs/test_case/models')
sys.path.append(os.path.abspath('./').replace('\\', '/') + '/bbs/test_case/page_obj')
from HTMLTestRunner import HTMLTestRunner
from sendMail import new_report
from sendMail import send_mail
import unittest
import time


if __name__ == "__main__":
    currentTime = time.strftime("%Y-%m-%d %H-%M-%S")
    fp = open('./bbs/report/' + currentTime + 'result.html', 'wb')
    # 设置生成报告文本信息
    runner = HTMLTestRunner(stream=fp, title="我的世界论坛-MCPlugin自动化测试报告",
                            description="环境：windows10\n浏览器：FireFox\n\n用例执行情况: ")
    discover = unittest.defaultTestLoader.discover('./bbs/test_case', pattern='*_sta.py')
    # 运行测试用例生成报告
    runner.run(discover)
    # 关闭文件流
    fp.close()
    # 获取最新生成报告的文件名
    file_name = new_report('./bbs/report/')
    # 发送邮件个相关人员，人员有多个可以循环发送
    send_mail(file_name, receiver='1442904439@qq.com')