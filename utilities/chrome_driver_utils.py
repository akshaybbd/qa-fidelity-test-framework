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
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}

    return webdriver.Chrome(options=chrome_options)
