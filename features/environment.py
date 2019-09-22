from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:3000')
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)

def after_scenario(context, scenario):
    context.browser.execute_script('window.localStorage.clear()')
    context.browser.refresh()