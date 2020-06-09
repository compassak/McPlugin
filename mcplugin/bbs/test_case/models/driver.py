from selenium import webdriver
from time import sleep


def getDriver(browser='FireFox'):
    driver = None
    if browser == 'FireFox':
        driver = webdriver.Firefox()
    elif browser == 'Edge':
        driver = webdriver.Edge()
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = getDriver()
    dr.get("https://www.mcplugin.cn/")
    sleep(3)
    dr.quit()
