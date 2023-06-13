# created by Abhijeet Thorat at 2023-06-13 17:37.
#

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import os
from utilities.path_configs import PathConfigs

def initialize_driver():
    """
    Initilizing chrome driver
    :returns: The web driver with correct options and configurations
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless") # Comment this out if you want to see the GUI
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('ignore-certificate-errors')
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}

    return webdriver.Chrome(
        executable_path=PathConfigs.path_to_chrome_driver_pipeline
        if "/tmp/workspace" in os.path.dirname(os.path.realpath(__file__))
        else PathConfigs.path_to_local_chrome_driver,
        options=chrome_options,
    )