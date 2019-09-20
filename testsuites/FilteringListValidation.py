import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class FilteringListValidationScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)

        expenseList.open_filter_dropdown()
        f_text = testData[0]
        exp_rows = testData[1]

        expenseList.select_filter_dropdown_value(f_text)
        
        assert  expenseList.get_filter_value() == f_text, expenseList.get_filter_value() + '!=' + f_text
        assert  expenseList.get_number_of_visible_rows() == len(exp_rows), str(expenseList.get_number_of_visible_rows()) + '!=' + str(len(exp_rows))
        for exp_row in exp_rows:
            assert expenseList.list_row_is_present(exp_row)        


class ExpenseListValidation(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())

        self.scenario = FilteringListValidationScenario(self.testSession.get_driver())

    def test_filtering_is_correct(self):
        data_set = [
            ['Amine',[['Escape Game', 'Paid by Amine', '85.00 $'],['Beer', 'Paid by Amine', '15.00 $']]], 
            ['Kévin',[['Costumes', 'Paid by Kévin', '135.00 $'],['Dinner', 'Paid by Kévin', '115.00 $']]],
            ['Julie',[['Movies', 'Paid by Julie', '35.00 $']]],
        ]
        for d in data_set:
            self.scenario.run(d)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()