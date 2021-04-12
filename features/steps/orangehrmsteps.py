
# You can implement step definitions for undefined steps with these snippets:
from behave import *   # 'instead using given, when, then' simple use -> *
from selenium import webdriver
import pytest
import time
# THIS IS REUSABLE FILE U CAN MODIFY BASE ON NEEDS *_^

@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()
    #webdriver.implicitly_wait(5)




@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")



@then(u'verify that the logo present on page')
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()