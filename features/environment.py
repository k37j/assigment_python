from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome(options=get_capabilities_tablet())
    context.browser.get('http://localhost:3000')
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)

def after_scenario(context, scenario):
    context.browser.execute_script('window.localStorage.clear()')
    context.browser.refresh()

    
def get_capabilities_tablet():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=768,1024")
    return chrome_options