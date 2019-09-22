Prerequisites:
- chromedriver in PATH (if not, hardcode it TestSetup)
- python 3.6.5 (higher should work too) added in PATH
    - libraries : 
        - selenium==3.12.0 (https://pypi.org/project/selenium/)
        - pyunitreport==0.1.4 
        - behave==1.2.6
        
To execute (from root folder):
    Python Single Test file:
        # no report generated
        python -m unittest testsuites/expense_page/ExpenseListtest.py

    Python Suite:
        # html report generated after full execution
        python .\libs\runners\PythonRunner.py

    Behave tests:
        # no report generated
        behave

    Behave tests:
        python .\libs\runners\BehaveRunner.py   (optional `-t fails` argument to run tests with @fails tag)