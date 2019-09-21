import time
from .BasePage import BasePage
from ..utils.utils import converse_to_float
from selenium.webdriver.support.select import Select

class ExpenseListPage(BasePage):

    
    some_locator = ''

    locators = {
        'filter select':        '//select[@class="filter-select"]',
        'select option':        './option',

        'add new payer input':  '//input[@placeholder="Add new user"]',
        'confirm new payer':    '//input[@placeholder="Add new user"]/following-sibling::button',

        'list table':           '//ul[@class="ul-costs"]',
        'list row':             '//li[@class="list-costs"]',
        'title cell':           './/span[@class="cost-title"]',
        'payer cell':           './/span[@class="cost-paidfor"]',
        'amount cell':          './/span[@class="cost-amount"]',

        'add exp title':        '//form[@class="form-expense"]//input[@id="title"]',
        'add exp payer':        '//form[@class="form-expense"]//select[@id="paidBy"]',
        'add exp amount':       '//form[@class="form-expense"]//input[@id="amount"]',
        'confirm expense':      '//form[@class="form-expense"]//button'
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
                row.find_element_by_xpath(self.locators['payer cell']).text.lower().split('paid by')[1].title().strip(),
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

    def get_sum_of_expenses(self):
        expense_rows = self._get_list_row_data(self._get_list_of_visible_rows_elements())
        sum = 0
        for exp_row in expense_rows:
            sum += converse_to_float(exp_row[2])
        return sum

    def _get_select_element_of_type(self, select_type):
        if select_type.lower() == 'add exp payer':
            return self.driver.find_element_by_xpath(self.locators['add exp payer'])
        elif select_type.lower() == 'filter':
            return self.driver.find_element_by_xpath(self.locators['filter select'])
        else:
            Exception('Incorrect select type: ' + select_type)


    # Filtering
    def open_select_dropdown(self, select_type):
        self._get_select_element_of_type(select_type).click()

    def _get_select_option_element_with_value(self, select_type, val):
        select = self._get_select_element_of_type(select_type)
        # will return first matching option, can be issue if filtering is not unique (but that would be an error in design i'd say)
        filter_options = select.find_elements_by_xpath(self.locators['select option'])
        for f_opt in filter_options:
            if f_opt.text == val:
                return f_opt
        return None

    def select_dropdown_has_value(self, select_type, value):
        return self._get_select_option_element_with_value(select_type, value) is not None

    def select_value_in_select_dropdown(self, select_type, value):
        if self.select_dropdown_has_value(select_type, value):
            self._get_select_option_element_with_value(select_type, value).click()
            # to close filter
            self.open_select_dropdown(select_type)
        else:
            Exception('Filter does not contain desired value: ' + str(value))

    def get_select_dropdown_value(self, select_type):
        select = Select(self._get_select_element_of_type(select_type))
        selected_option = select.first_selected_option   
        return selected_option.text

    # Adding Expense
    def _fill_expense_title(self, title):
        self.driver.find_element_by_xpath(self.locators['add exp title']).send_keys(title)

    def _select_expense_payer(self, payer):
        if 'paid by' in payer.lower():
            payer = payer.lower().split('paid by')[1].title().strip()
        self.open_select_dropdown('add exp payer')
        self.select_value_in_select_dropdown('add exp payer', payer)

    def _fill_expense_amount(self, amount):
        self.driver.find_element_by_xpath(self.locators['add exp amount']).send_keys(amount)

    def fill_new_expense(self, title, payer, amount):
        self._fill_expense_title(title)
        self._select_expense_payer(payer)
        self._fill_expense_amount(amount)

    def confirm_new_expense(self):
        self.driver.find_element_by_xpath(self.locators['confirm expense']).click()

    def add_new_expense(self, expense_data):
        self.fill_new_expense(expense_data[0], expense_data[1], expense_data[2])
        self.confirm_new_expense()

    # new payer
    def _fill_new_payer_field(self, text):
        self.driver.find_element_by_xpath(self.locators['add new payer input']).send_keys(text)

    def _confirm_adding_new_payer(self):
        self.driver.find_element_by_xpath(self.locators['confirm new payer']).click()

    def add_new_payer(self, payer_name):
        self._fill_new_payer_field(payer_name)
        self._confirm_adding_new_payer()