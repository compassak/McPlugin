from selenium import webdriver
import os


def print_screen(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base = base_dir.split('test_case')[0]
    file_path = base + 'report/images/' + file_name
    file_path.replace("\\", "/")
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com/')
    print_screen(driver, 'baidu.png')
    driver.quit()
