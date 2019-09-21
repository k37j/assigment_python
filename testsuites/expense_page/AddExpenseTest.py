import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class AddExpenseScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        expenseList.add_new_expense(testData)

    def validate_correct_expense(self, testData):
        expenseList = ExpenseListPage(self.driver)
        assert expenseList.list_row_is_present(testData),  'Correct expense was not added to list: ' + str(testData)

    def validate_incorrect_expense(self, testData):
        expenseList = ExpenseListPage(self.driver)
        assert expenseList.get_number_of_visible_rows() == testData, 'New expense was added' 
        

class AddExpenseTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())
        self.scenario = AddExpenseScenario(self.testSession.get_driver())

    def test_add_valid_expense(self):
        data_set = [
                ['Diving', 'Amine', '12.00 $'],
                ['House', 'Julie', '355555.00 $'],
                ['Boat', 'Kévin', '85.00 $']
            ]
        for d in data_set:
            self.scenario.run(d)
            self.scenario.validate_correct_expense(d)

    def test_add_expense_no_title(self):
        data_set = ['', 'Kévin', '3.00 $']
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)

    def test_add_expense_no_payer(self):
        data_set = ['Wine', '', '7.00 $']
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)

    def test_add_expense_empty_amount(self):
        # if amount is empty it'll crash page badly after refresh
        data_set = ['Nuts', 'Kévin', ''] 
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)

    def test_add_expense_string_amount(self):
        # if amount is empty it'll crash page badly after refresh
        data_set = ['Boots', 'Kévin', 'Twenty Five'] 
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)
    
    def test_add_expense_deciaml_amount(self):
        # i'd say it's a bug, to define with developer and PO
        data_set = ['Birds', 'Kévin', '0,75 $'] 
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)

    def test_add_expense_euro_amount(self):
        # i'd say it's a bug, to define with developer and PO
        data_set = ['Tower', 'Kévin', '75 Eur'] 
        expected_row_count = 5
        self.scenario.run(data_set)
        self.scenario.validate_incorrect_expense(expected_row_count)

    def tearDown(self):
        self.testSession.close_test_session()
