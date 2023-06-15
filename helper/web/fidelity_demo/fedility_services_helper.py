# created by Abhijeet Thorat at 2023-06-13 17:31.
#

from time import sleep
from page_objects.selenium_methods.web_core_method import CorePage
from utilities.allure_methods import *
from utilities.path_configs import get_path_to_file
from utilities.read_properties import read_config_file
from utilities.py_logger import get_logger
from utilities.allure_methods import *
from selenium.webdriver import Chrome

logger = get_logger(logger_name=__name__)

class FidilityHelper:
    global XPATH_CON, CONFIG

    XPATH_CON = get_path_to_file('config', 'web', 'fidelity_demo', 'x_paths.ini')
    CONFIG = read_config_file(path_to_config=XPATH_CON, section="FIDEPATH")

    def launch_url(self, driver: Chrome):
        """will launch desired url"""
        driver.get(CONFIG['fide_url'])
    def about_us(self,driver: Chrome):
        """will verify about us menu"""
        fed_obj = CorePage(driver)
        fed_obj.assert_text(CONFIG['fide_aboutus'],"About Us")

    def product_services_menu(self,driver: Chrome):
        """this will verify and click on Our Products & Services menu"""
        fed_obj = CorePage(driver)
        fed_obj.assert_text(CONFIG['fide_products'],"Our Products & Services")
        fed_obj.mouse_click(CONFIG['fide_products'])
        sleep(2)
        allure_screenshot(driver,"Our Products & Services page")
