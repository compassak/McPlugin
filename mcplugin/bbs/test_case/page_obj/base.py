class Page(object):
    """页面基础类"""

    base_url = 'https://www.mcplugin.cn'
    url = '/'

    def __init__(self, s_driver, parent=None):
        self.driver = s_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did ont land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, scr, search_button=None):
        return self.driver.execute_script(scr, search_button)

    def refresh_page(self):
        self.driver.refresh()
