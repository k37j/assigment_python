import time
from .BasePage import BasePage
from selenium.webdriver.support.select import Select

class ExpenseListPage(BasePage):

    
    some_locator = ''

    locators = {
        'filter select':    '//select[@class="filter-select"]',
        'filter option':    '//select[@class="filter-select"]//option',

        'list table':       '//ul[@class="ul-costs"]',
        'list row':         '//li[@class="list-costs"]',
        'title cell':       './/span[@class="cost-title"]',
        'payer cell':       './/span[@class="cost-paidfor"]',
        'amount cell':      './/span[@class="cost-amount"]'
    }

    def _is_loaded(self):
        self.driver.find_element_by_xpath(self.locators['filter select'])
        self.driver.find_element_by_xpath(self.locators['list table'])

    def _get_list_of_visible_rows_elements(self):
        list_rows = self.driver.find_elements_by_xpath(self.locators["list row"])
        visible_rows = []
        for row in list_rows:
            if row.is_displayed():
                visible_rows.append(row)
        
        return visible_rows

    def _get_list_row_data(self, list_rows=None):
        if list_rows is None:
            list_rows = self._get_list_of_visible_rows_elements()
        list_row_content = []
        for row in list_rows:
            list_row_content.append([
                row.find_element_by_xpath(self.locators['title cell']).text,
                row.find_element_by_xpath(self.locators['payer cell']).text,
                row.find_element_by_xpath(self.locators['amount cell']).text
            ])
        
        return list_row_content

    def list_row_is_present(self, expected_list_row_data_set):
        ui_data_array = self._get_list_row_data()
        if len(ui_data_array) == 0:
            return False
        
        result = []
        for ui_data_set in ui_data_array:
            result.append(all(d in ui_data_set for d in expected_list_row_data_set))
        
        if True in result:
            # case if some rows are duplicated:
            if result.count(True) > 1:
                # dont know what to do here, can be a feature, can be a bug (duplication of data on ui/db)
                print(str(expected_list_row_data_set) + ' present multiple ' + result.count(True) + ' times!')
            return True
        return False

    def get_number_of_visible_rows(self):
        return len(self._get_list_of_visible_rows_elements())

    def open_filter_dropdown(self):
        self.driver.find_element_by_xpath(self.locators['filter select']).click()

    def _get_filter_option_element_with_value(self, val):
        # will return first matching option, can be issue if filtering is not unique (but that would be an error in design i'd say)
        filter_options = self.driver.find_elements_by_xpath(self.locators['filter option'])
        for f_opt in filter_options:
            if f_opt.text == val:
                return f_opt
        return None

    def filter_dropdown_has_value(self, value):
        return self._get_filter_option_element_with_value(value) is not None

    def select_filter_dropdown_value(self, value):
        if self.filter_dropdown_has_value(value):
            self._get_filter_option_element_with_value(value).click()
            # to close filter
            self.open_filter_dropdown()
        else:
            Exception('Filter does not contain desired value: ' + str(value))

    def get_filter_value(self):
        select = Select(self.driver.find_element_by_xpath(self.locators['filter select']))
        selected_option = select.first_selected_option   
        return selected_option.text