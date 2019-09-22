from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSetup(object):
    
    def open_test_session(self, sessionType='chrome', capabilities=None, options=None):
        "sessionType for Chrome/Mozilla/IE/etc"
        if sessionType.lower() == 'chrome':
            self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
        else:
            raise ValueError('Not supported session type')

    def _clear_local_storage(self):
        # no need for now
        try:
            self.driver.execute('window.localStorage.clear()')
        except Exception as wde:
            print('! Problem with setting up test environment !')
            raise Exception(wde)

    def get_driver(self):
        if not self.driver:
            raise Exception('Open test session first')
        return self.driver

    def close_test_session(self):        
        self.driver.close()

    def get_capabilities_tablet(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=768,1024")
        return chrome_options