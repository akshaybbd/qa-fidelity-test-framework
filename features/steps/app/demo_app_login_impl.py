from appium.webdriver.appium_service import AppiumService
from behave import *
from appium.webdriver import *
from helper.app.demo_app_helper import app_Helper
from utilities.pulse_logger import *
import time
from appium.options.android import UiAutomator2Options
#import os

logger = get_logger(logger_name=__name__, console=True)
appium_service = AppiumService()
APP_OBJ=app_Helper()
@given('I Open one app on device')
def step_im(context):
   driver=context.driver
   logger.info("started")
   driver.get_log('logcat')
   time.sleep(10)

@when('I enter valid msisdn "{msisdn}"')
def step_imp(context, msisdn):
   APP_OBJ.enter_msisdn(context.driver, msisdn)

@then('I enter valid pin "{pin}"')
def step_imp(context, pin):
   APP_OBJ.enter_pin(context.driver, pin)

@then('I enter valid otp "{OTP}"')
def step_imp(context, OTP):
   APP_OBJ.enter_otp(context.driver, OTP)

@then('I verify and click on shop menu and then I do swipe up and swipe down')
def step_imp(context, OTP):
   APP_OBJ.select_Shopmenu(context.driver, OTP)
