import pytest
from selenium import webdriver
import os
from _pytest.runner import runtestprotocol
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.fixture
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

    desired_cap = {
        'platform': 'Mac OS X 10.13',
        'browserName': 'safari',
        'version': '11.1',
        'build': 'Onboarding Sample App - Python + Pytest',
        'name': '2-user-site',
        'username': sauce_username,
        'accessKey': sauce_access_key,

        # This setting is for using Sauce Connect Proxy tunnel
        # Typically you use this setting if you need to run your tests from behind a secure network firewall
        'tunnelIdentifier': 'demo-python-tunnel'
    }

    browser = webdriver.Remote(remote_url, desired_capabilities=desired_cap)
    yield browser
    browser.quit()

# Here is our actual test code. In this test we open the saucedemo app in chrome and assert that the title is correct.
def test_should_open_chrome(driver):
    # Substitute 'http://www.saucedemo.com' for your own application URL
    driver.get("http://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title