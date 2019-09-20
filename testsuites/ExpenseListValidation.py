import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class ExpenseListValidationScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        assert expenseList.list_row_is_present(testData)
        


class ExpenseListValidation(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())
        self.scenario = ExpenseListValidationScenario(self.testSession.get_driver())

    def test_default_data_is_visible(self):
        data_set = [
            ['Escape Game', 'Paid by Amine', '85.00 $'], 
            ['Beer', 'Paid by Amine', '15.00 $'], 
            ['Costumes', 'Paid by Kévin', '135.00 $'],
            ['Movies', 'Paid by Julie', '35.00 $'], 
            ['Dinner', 'Paid by Kévin', '115.00 $']
        ]
        for d in data_set:
            self.scenario.run(d)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()