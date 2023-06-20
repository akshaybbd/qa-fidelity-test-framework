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
    CONFIG = read_config_file(path_to_config=XPATH_CON, section="fid_xpath")

    def launch_url(self, driver: Chrome):
        """will launch desired url"""
        driver.get(CONFIG['fid_url'])
    def about_us(self,driver: Chrome):
        """will verify about us menu"""
        fed_obj = CorePage(driver)
        fed_obj.assert_text(CONFIG['fid_aboutus'],"About Us")

    def product_services_menu(self,driver: Chrome):
        """this will verify and click on Our Products & Services menu"""
        fed_obj = CorePage(driver)
        fed_obj.assert_text(CONFIG['fid_products'],"Our Products & Services")
        fed_obj.mouse_click(CONFIG['fid_products'])
        sleep(2)
        allure_screenshot(driver,"Our Products & Services page")

    def verify_product_services(self, driver:Chrome):
        """THis will verify all the product and services tabs"""
        fed_obj = CorePage(driver)
        fed_obj.assert_text(CONFIG['fid_security_services_tab'],"Fidelity Security Services")
        fed_obj.assert_text(CONFIG['fid_adt_tab'],"Fidelity ADT")
        fed_obj.assert_text(CONFIG['fid_cashmaster_tab'],"Fidelity CashMaster")
        fed_obj.scroll_down()
        fed_obj.assert_text(CONFIG['fid_cash_solution_tab'],"Fidelity Cash Solutions")
        fed_obj.assert_text(CONFIG['fid_securr_drive_tab'],"Fidelity SecureDrive")
        fed_obj.assert_text(CONFIG['fid_fire_solution_tab'],"Fidelity Fire Solutions")
        fed_obj.scroll_down()
        fed_obj.assert_text(CONFIG['fid_sensormatic_smaas_tab'],"Sensormatic & SMAAS")
        fed_obj.assert_text(CONFIG['fid_cleaning_services_tab'],"Fidelity Cleaning Services")
        fed_obj.assert_text(CONFIG['fid_specialized_services_tab'],"Specialised Services")
        fed_obj.scroll_down()
        fed_obj.assert_text(CONFIG['fid_2rm_tab'],"Fidelity 2RM")
        fed_obj.assert_text(CONFIG['fid_insure_tab'],"Fidelity inSure")
