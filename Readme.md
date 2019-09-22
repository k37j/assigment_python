## Test Automation Solution

- Foreword
- What more to do
- Prerequisites
- To execute
- Testing

#### Foreword:
I've created two solutions, since code to be later used in Behave needed to be written either way, and i was curious how it would look in non-gherkin style in python.

Basic test scenarios were implemented covering all desired functionalities:
- See the list of each expense with its title, the name of the payer and the amount paid
- Filter on the list by user
- Add a new expense to the list by filling what it is, who paid it and how much it cost
- See the total expenses of the displayed list
- Add a new payer

> Implementation in pure python took about 2h, `select` element took some time before i found python selenium Select object

> Getting to know Behave and implementing it on top of existing python code took around 2h

> Minor refactors that were not required but nice to have and and implementing reports and runners took together another 2h 

> Testing application by hand for around 1h while developing solution

> Documentation, setting repository and environment took around 1h

5 commits were pushed, to give outlook how solution evolved

Some tests are failing due to UI behavior that in my opinion is a bug
Not all edge case or particular case scenarios (i.e US number notation, filtering on users with same name) are not implemented, they can be easily created with existing steps/code though.

##### What more to do:
 - Select which aproach is better suited for project requirements
 - Cover edge cases 
 - Adjust scenarios after consulting with developer/ux what is bug what a `feature`
 - Extend runners to allow running tests in paralell
 - Add jenkinsfile and plug this to jenkins
 - Add some html reporter for Gherkin
 - Merge html report/find way to have single report from Python tests


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

## Testing 
Application has basic functionalities but:

#### There's no user input validation on any field
In general it looks bad, but in case of invalid (empty/non-number) `New Expense Amount` it crashes application after page refresh and requires clean of local-storage (or at least deleting incorrect entry from it)

#### Filtering is broken for users with same name
Since no validation, we can add multiple users with same Name

ex. two users A and B, each with Name `Isabell`
When we add one expense to Isabell-A and another to Isabell-B
And we then perform filtering on Isabell-A
Then we will see expenses of Isabell-A and Isabell-B

Could be fixed by generating some random uuid for each user, but in general that should not be allowed to do

#### Hardcoded currency
It's kinda shortcut that was taken, but since it's possible to put 34 EUR it should not be converted to 34 $

#### Amount Rounding
Impossible to have decimals, user inputs gets rounded-down / trimmed after `.` or `,`

#### Does not support thousand separators used in different parts of world
`US - 1,654`, `Europes 1 654` or `Italys 1.654` 
gets truncated to 1.00 $ instad of showing proper 1654.00 $


#### Unfriendly UX
No infinite scrolling nor pagination - easier to test and implement but UX is suffering when scrolling of whole UI starts, especially on the tablet 
No information when new Person was added - one has to check filter/add payer to expense to see new Person was added
Some Labels with test describing what parts UI are - Filter is quite obvious, but adding new expense less, adding new Person is a bit misleading since User has different conotations. Header for table could clarify this a bit.
Total expenses are lost at bottom, not visible when list rows amount causes scrolling

#### I'm not a fun of how selects are implemented
As per error in console, `select` should have `value` property set correctly

#### Application logging
Shipping app with error in console on opening/reloading page,
verbose logging of left when adding expense (which shows all data used for table, not only added)

#### Localization
If we're using $, putting test data and placeholders in English lets have `All` instead of `Tous`
