import os.path

import pytest
import pytest_html
from selenium import webdriver

url_link = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
driver = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url(url_link))
        xfail = hasattr(report, "wasxfail")
        print("driver")
        print(driver)
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html(html))
        report.extras = extras


def pytest_html_report_title(report):
    report.title = "My very own title!"


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get(url_link)
    return driver

