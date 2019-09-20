import time
from .BasePage import BasePage

class ExpenseListPage(BasePage):
    
    some_locator = ''

    locators = {
        'list table':   '//ul[@class="ul-costs"]',
        'list row':     '//li[@class="list-costs"]',
        'title cell':   './/span[@class="cost-title"]',
        'payer cell':   './/span[@class="cost-paidfor"]',
        'amount cell':  './/span[@class="cost-amount"]'
    }

    def _get_list_row_data(self):
        list_rows = self.driver.find_elements_by_xpath(self.locators["list row"])
        list_row_content = []
        for i in range(0,len(list_rows)):
            list_row_content.append([
                list_rows[i].find_element_by_xpath(self.locators['title cell']).text,
                list_rows[i].find_element_by_xpath(self.locators['payer cell']).text,
                list_rows[i].find_element_by_xpath(self.locators['amount cell']).text
            ])
        
        return list_row_content


    def list_row_is_present(self, expected_list_row_data_set):
        ui_data_array = self._get_list_row_data()
        if len(ui_data_array) == 0:
            raise Exception('No data rows present')
        
        result = []
        for ui_data_set in ui_data_array:
            result.append(all(d in ui_data_set for d in expected_list_row_data_set))
        
        if True in result:
            if result.count(True) > 1:
                # dont know what to do here
                print(str(expected_list_row_data_set) + ' present multiple ' + result.count(True) + ' times!')
            return True
        return False
