# created by Abhijeet Thorat at 2023-06-13 19:53.
#

from asyncio import sleep
import time
from page_objects.selenium_methods.app_core_method import AppCorePage
from utilities.path_configs import get_path_to_file
from utilities.read_properties import read_config_file
from utilities.pulse_logger import *
from appium.webdriver import Remote
from utilities.allure_methods import *

global XPATH_CON, CONFIG
logger = get_logger(logger_name=__name__)
XPATH_CON=get_path_to_file('config', 'app', 'demo_app', 'x_paths.ini')
CONFIG=read_config_file(path_to_config=XPATH_CON, section="demo_xpaths")
class app_Helper():

    XPATH_CON = get_path_to_file('config', 'app', 'demo_app', 'x_paths.ini')
    CONFIG = read_config_file(path_to_config=XPATH_CON, section="demo_xpaths")
    def enter_msisdn(self, driver:Remote, msisdn):
        """entering valid msisdn for login"""
        app_obj=AppCorePage(driver)
        time.sleep(10)
        try:
            app_obj.app_click(ui_xpath=CONFIG['switch_account'])
            app_obj.app_click(CONFIG['switch_account'])
        except:
            logger.info("new apk is being installed")
        time.sleep(10)
        app_obj.app_input(CONFIG['enter_msisdn'],msisdn)
        allure_screenshot(driver,message="Vodapay login screen")
        app_obj.app_click(CONFIG['next_button'])
        time.sleep(5)

    def enter_pin(self, driver:Remote, pin):
        """entering valid pin for respective msisdn"""
        app_obj=AppCorePage(driver)
        app_obj.app_input(CONFIG['enter_pin'],pin)

    def enter_otp(self, driver:Remote, otp):
        """entering valid otp for respective msisdn"""
        app_obj=AppCorePage(driver)
        time.sleep(10)
        allure_screenshot(driver,message="OTP screen")
        app_obj.app_input(CONFIG['enter_otp'],otp)
        time.sleep(10)
        allure_screenshot(driver,message="Login home screen")
        try:
            app_obj.app_click(CONFIG['allow_btn'])
        except:
            logger.info("allowed button noe visible")
        time.sleep(25)
        allure_screenshot(driver,message="after handling allow pop-up")
        time.sleep(10)

    def select_Shopmenu(self,driver:Remote):
        """this will verify Sho menu tab and also do swipe up and swipe down on shop menu page"""
        app_obj=AppCorePage(driver)
        app_obj.assert_text(CONFIG['shop_menu'],"Shop")
        app_obj.app_click(CONFIG['shop_menu'])
        time.sleep(10)
        app_obj.scroll_gesture_down()
        app_obj.scroll_gesture_down()
        allure_screenshot(driver,message="after scroll down")
        app_obj.scroll_gesture_up()
        app_obj.scroll_gesture_up()
        allure_screenshot(driver,message="after scroll up")
