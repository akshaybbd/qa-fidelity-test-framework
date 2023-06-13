# created by Abhijeet Thorat at 2023-06-13 17:38.
#

from jmespath import Options
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def initialize_edge_driver():
    """
    Initilizing edge driver
    :returns: The web driver with correct options and configurations
    """

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return driver
