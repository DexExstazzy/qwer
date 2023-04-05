from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
#def pytest_addoption(parser):
  #parser.addoption('--language', default = 'ru')
def pytest_addoption(parser):
    parser.addoption('--language', default="en")
    parser.addoption('--browser_name', default='chrome')
    
@pytest.fixture
def driver(request):
  #language = request.config.getoption('language')
  browser_name = request.config.getoption('browser_name')
  driver = None
  if browser_name == 'chrome':
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    driver = webdriver.Chrome()
  elif browser_name == 'firefox':
     driver = webdriver.Firefox()
  else:
     raise pytest.UsageError('browser_name should be chrome or firefox')
  print('create browser...')
  yield driver
  print('delite browser...')
  driver.quit()

