import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 
from libs.utils.utils import converse_to_float 


class ExpenseSumTestScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        assert expenseList.get_sum_of_expenses() == testData
        

class ExpenseSumUpdateScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)

        current_sum = expenseList.get_sum_of_expenses()
        expenseList.add_new_expense(testData)

        assert expenseList.get_sum_of_expenses() == current_sum + converse_to_float(testData[2])



class ExpenseSumTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())

    def test_expense_sum_is_correct(self):
        expected_sum = 385
        ExpenseSumTestScenario(self.testSession.get_driver()).run(expected_sum)

    def test_expense_sum_update_is_correct(self):
        data_set = ['Diving', 'Amine', '12.00 $']
        ExpenseSumUpdateScenario(self.testSession.get_driver()).run(data_set)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()