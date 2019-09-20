class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self._is_loaded()

    def _is_loaded(self):
        pass
