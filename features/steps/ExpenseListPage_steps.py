from libs.pages.ExpenseListPage import ExpenseListPage
from libs.utils.utils import converse_to_float
from behave import given, when, then
import time

@given('Expense List Page is loaded')
def expense_page_is_loaded(context):
    ExpenseListPage(context.browser)


@then('Expense List Page {has_or_not} expense with title "{title}", payer "{payer}" and amount "{amount}"')
def expense_list_has_payment(context, has_or_not, title, payer, amount):
    title = title if title != 'n/a' else ''
    payer = payer if payer != 'n/a' else ''
    amount = amount if amount != 'n/a' else ''
    elp = ExpenseListPage(context.browser)
    if has_or_not == 'has':
        assert elp.list_row_is_present([title, payer, amount]), 'Row with ' + str([title, payer, amount]) + ' is not present'
    else:
        assert not elp.list_row_is_present([title, payer, amount]), 'Row with ' + str([title, payer, amount]) + ' is present'

@when('Perform filtering on "{payer}"')
def perform_filtering(context, payer):
    elp = ExpenseListPage(context.browser)
    elp.open_select_dropdown('filter')
    elp.select_value_in_select_dropdown('filter', payer)
    # for closing
    elp.open_select_dropdown('filter')

@when('Add new expense with title "{title}", payer "{payer}" and amount "{amount}"')
def add_expense(context, title, payer, amount):
    title = title if title != 'n/a' else ''
    payer = payer if payer != 'n/a' else ''
    amount = amount if amount != 'n/a' else ''
    elp = ExpenseListPage(context.browser)
    elp.add_new_expense([title, payer, amount])

@given('Expense List has "{expected_count}" entries')
@then('Expense List has "{expected_count}" entries')
def list_has_number_of_entries(context, expected_count):
    elp = ExpenseListPage(context.browser)
    ui_entires = elp.get_number_of_visible_rows()
    assert int(expected_count) == ui_entires, 'Incorrect number of entires visible on ui : ' + str(ui_entires)

@given('Expense List Sum is equal to "{expected_sum}"')
@then('Expense List Sum is equal to "{expected_sum}"')
def expense_sum_is_equal_to(context, expected_sum):
    elp = ExpenseListPage(context.browser)
    assert converse_to_float(expected_sum) == elp.get_sum_of_expenses()

@when('Add new payer with name "{payer_name}"')
def add_new_payer(context, payer_name):
    payer_name = payer_name if payer_name != 'n/a' else ''

    elp = ExpenseListPage(context.browser)
    elp.add_new_payer(payer_name)

@given('Filter {has_or_not} "{payer_name}" as selectable value')
@then('Filter {has_or_not} "{payer_name}" as selectable value')
def filter_has_value(context, has_or_not, payer_name):
    payer_name = payer_name if payer_name != 'n/a' else ''
    elp = ExpenseListPage(context.browser)
    if has_or_not == 'has':
        assert elp.select_dropdown_has_value('filter', payer_name), 'Filter does not have option: ' + payer_name + '"'
    else:
        assert not elp.select_dropdown_has_value('filter', payer_name), 'Filter has option: ' + payer_name + '"'

@given('Dropdown for payer in new expense {has_or_not} "{payer_name}" as selectable value')
@then('Dropdown for payer in new expense {has_or_not} "{payer_name}" as selectable value')
def add_expense_payer_has_value(context, has_or_not, payer_name):
    payer_name = payer_name if payer_name != 'n/a' else ''

    elp = ExpenseListPage(context.browser)
    if has_or_not == 'has':
        assert elp.select_dropdown_has_value('add exp payer', payer_name), 'New expense Payer dropdown does not have option: "' + payer_name + '"'
    else:
        assert not elp.select_dropdown_has_value('add exp payer', payer_name),  'New expense Payer dropdown has option: "' + payer_name + '"'
