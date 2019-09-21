import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class AddNewPayerTestScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        expenseList.add_new_payer(testData)

    
    def validate_correct_scenario(self, testData):
        expenseList = ExpenseListPage(self.driver)
        expenseList.open_select_dropdown('add exp payer')
        assert expenseList.select_dropdown_has_value('add exp payer', testData), 'Correct Expense payer not added: ' + testData
        expenseList.open_select_dropdown('filter')
        assert expenseList.select_dropdown_has_value('filter', testData), 'Correct Expense Expense Filter payer not added: ' + testData
        
    def validate_incorrect_scenarion(self, testData):
        expenseList = ExpenseListPage(self.driver)
        expenseList.open_select_dropdown('add exp payer')
        assert not expenseList.select_dropdown_has_value('add exp payer', testData), 'Incorrect payer added to Add Expense payer dropdown:  "' + testData + '"'
        expenseList.open_select_dropdown('filter')
        assert not expenseList.select_dropdown_has_value('filter', testData), 'Incorrect payer added to Expense Filter dropdown: "' + testData + '"'


class AddNewPayerTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())
        self.scenario = AddNewPayerTestScenario(self.testSession.get_driver())

    def test_add_valid_payer(self):
        data_set = ['Adam', 'Żółcimiąłżyciel', 'Olaf-Poru', 'Walo Salo']
        for d in data_set:
            self.scenario.run(d)
            self.scenario.validate_correct_scenario(d)

    def test_add_invalid_payer(self):
        data_set = ['', 'l33t guy', '</option><option>hehe</option><option>', '" some_argument="5"', 'Walo Salo']
        for d in data_set:
            self.scenario.run(d)
            self.scenario.validate_incorrect_scenarion(d)
        

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()