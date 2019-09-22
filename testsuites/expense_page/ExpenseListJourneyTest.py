import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup
from libs.utils.utils import converse_to_float 


class ExpenseListTestScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        base_sum = converse_to_float(expenseList.get_sum_of_expenses())
        expenseList.add_new_payer(testData[1])
        expenseList.add_new_expense(testData)
        final_sum = expenseList.get_sum_of_expenses()
        assert converse_to_float(final_sum) == base_sum + converse_to_float(testData[2])
        

class ExpenseListTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())
        self.scenario = ExpenseListTestScenario(self.testSession.get_driver())

    def test_default_data_is_visible(self):
        data_set = ['Wheels', 'Adam', '312.00 $']
        self.scenario.run(data_set)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()