#### Prerequisites:
- chromedriver in PATH
- python 3.6.5 (higher should work too) added in PATH
- libraries (installed preferably via pip): 
    - selenium==3.12.0
    - pyunitreport==0.1.4 
    - behave==1.2.6



#### To execute (from root folder):

Launch application on localhost:3000

> Python Single Test file:
> ( no report generated )
```python -m unittest testsuites/expense_page/ExpenseListtest.py```


> Python Suite:
> (html report generated after each test file execution)
``` python .\libs\runners\PythonRunner.py ```

> Behave tests:
> ( no report generated )
``` behave ```

> Behave tests:
> ( generates junit report, optional -t "tag" argument to run tests with @tag, single tag supported only)
``` python .\libs\runners\BehaveRunner.py ```
