from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSetup(object):
    
    def open_test_session(self, sessionType='chrome', capabilities=None, options=None):
        "sessionType for Chrome/Mozilla/IE/etc"
        if sessionType.lower() == 'chrome':
            # should be in PATH, but does not recognize for me after moving solution
            self.driver = webdriver.Chrome(executable_path='G://GIT//Drivers//chromedriver_2.33', options=options, desired_capabilities=capabilities)
        else:
            raise ValueError('Not supported session type')

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