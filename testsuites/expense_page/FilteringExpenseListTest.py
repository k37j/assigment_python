import unittest
from libs.pages.ExpenseListPage import ExpenseListPage 
from libs.utils.TestSetup import TestSetup 


class FilteringExpenseListScenario(object):
    def __init__(self, driver):
        self.driver = driver

    def run(self, testData):
        self.driver.get('http://localhost:3000')
        expenseList = ExpenseListPage(self.driver)

        expenseList.open_select_dropdown('filter')
        f_text = testData[0]
        exp_rows = testData[1]
        expenseList.select_value_in_select_dropdown('filter', f_text)
        
        assert  expenseList.get_select_dropdown_value('filter') == f_text, expenseList.get_select_dropdown_value('filter') + '!=' + f_text
        assert  expenseList.get_number_of_visible_rows() == len(exp_rows), str(expenseList.get_number_of_visible_rows()) + '!=' + str(len(exp_rows))
        for exp_row in exp_rows:
            assert expenseList.list_row_is_present(exp_row)        


class FilteringExpenseListTest(unittest.TestCase):

    def setUp(self):
        self.testSession = TestSetup()
        self.testSession.open_test_session(options=self.testSession.get_capabilities_tablet())

        self.scenario = FilteringExpenseListScenario(self.testSession.get_driver())

    def test_filtering_is_correct(self):
        data_set = [
            ['Amine',[['Escape Game', 'Amine', '85.00 $'],
                     ['Beer', 'Amine', '15.00 $']]], 
            ['Kévin',[['Costumes', 'Kévin', '135.00 $'],
                     ['Dinner', 'Kévin', '115.00 $']]],
            ['Julie',[['Movies', 'Julie', '35.00 $']]],
            ['Tous',[['Movies', 'Julie', '35.00 $'],
                    ['Costumes', 'Kévin', '135.00 $'],
                    ['Dinner', 'Kévin', '115.00 $'],
                    ['Escape Game', 'Amine', '85.00 $'],
                    ['Beer', 'Amine', '15.00 $']]]
        ]        
        for d in data_set:
            self.scenario.run(d)

    def tearDown(self):
        self.testSession.close_test_session()

if __name__ == "__main__":
    unittest.main()