import sys
import os

sys.path.append(os.path.abspath('./').replace('\\', '/'))

from selenium.webdriver.common.by import By
from base import Page
from time import sleep
from loginPage import login
from selenium import webdriver


class exchangeIntegral(Page):
    """用户兑换积分界面类"""

    def __init__(self, s_driver):
        super().__init__(s_driver)
        self.url = '/home.php?mod=spacecp&ac=credit&op=exchange'
        self.exchange_amount_loc = (By.CSS_SELECTOR, '#exchangeamount')
        self.password_loc = (By.NAME, 'password')
        self.exchange_submit_button_loc = (By.CSS_SELECTOR, '#exchangesubmit_btn')
        self.exchange_hint_loc = (By.CSS_SELECTOR, 'i')

    def set_amount(self, amount):
        self.find_element(*self.exchange_amount_loc).send_keys(amount)

    def exchange_submit(self):
        self.find_element(*self.exchange_submit_button_loc).click()

    def exchange_hint(self):
        return self.find_element(*self.exchange_hint_loc).text

    def exchange_integral(self, amount, password1):
        """统一兑换积分入口"""

        lop = login(self.driver)
        self.open()
        self.set_amount(amount)
        lop.login_password(password1)
        self.exchange_submit()


if __name__ == '__main__':
    username = 'minecraft_ak'
    password = '2438675akkl'
    driver = webdriver.Firefox()
    lo = login(driver)
    ei = exchangeIntegral(driver)

    lo.user_login(username, password)
    ei.exchange_integral('', password)
    sleep(0.7)
    print(ei.exchange_hint())
    sleep(1)
    lo.logout()
