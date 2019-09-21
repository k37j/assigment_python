import unittest
from pyunitreport import HTMLTestRunner
from datetime import datetime

if __name__ == "__main__":
    execution_time = datetime.now().strftime("%d%m%Y_%H%M%S")
    test_suite = unittest.TestLoader().discover('./testsuites/expense_page', '*Test.py', '.')
    i = 0
    for suite in test_suite._tests:
        if len(suite._tests) > 0:
            
            runner = HTMLTestRunner(**{
                "output": execution_time,
                "report_name": 'expense_page_test_' + str(i),
                "failfast": False
            })
            runner.run(suite)
            i += 1
            