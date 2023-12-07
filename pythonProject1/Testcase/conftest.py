from selenium import webdriver
import pytest
import pytest_html
import pytest_html.extras
import random
import os
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pathlib import Path

driver = None

Baseurl = "https://www.tripozo.com/"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = ".\\Reports\\screenshot"+str(random.randint(1,100))+".png"
            driver.get_screenshot_as_file(file_name)
            file_name = file_name[10:]
            html1 = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
            print("__________________"+html1)
            extra.append(pytest_html.extras.html(html1))
            # os.remove(file_name)
        report.extra = extra



def pytest_html_report_title(report):
    report.title = "Automation Report"


@pytest.fixture()
def browser():
    global driver
    driver = webdriver.Chrome()
    driver.get(Baseurl)
    driver.implicitly_wait(10)
    return driver
