import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class ExpenseListTestScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)
        assert expenseList.list_row_is_present(testData)
        

class ExpenseListTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())
        self.scenario = ExpenseListTestScenario(self.testSession.get_driver())

    def test_default_data_is_visible(self):
        data_set = [
            ['Escape Game', 'Amine', '85.00 $'], 
            ['Beer', 'Amine', '15.00 $'], 
            ['Costumes', 'Kévin', '135.00 $'],
            ['Movies', 'Julie', '35.00 $'], 
            ['Dinner', 'Kévin', '115.00 $']
        ]
        for d in data_set:
            self.scenario.run(d)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()