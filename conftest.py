import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, en, ru, fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    def get_browser_for_language(browser_name, user_language):
        if browser_name == "chrome":
            print("\nstart Chrome browser for test...")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print("\nstart Firefox browser for test...")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            return webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    if user_language in ('es', 'en', 'ru', 'fr'):
        print(f"\nstart browser for language '{user_language}'...")
        browser = get_browser_for_language(browser_name, user_language)
    else:
        raise pytest.UsageError("--language should be one of the 'es', 'en', 'ru' or 'fr'")
    yield browser
    print("\nquit browser..")
    browser.quit()
