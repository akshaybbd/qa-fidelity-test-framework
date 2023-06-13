# created by Abhijeet Thorat at 2023-06-13 17:34.
#

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.pulse_logger import get_logger
from utilities.xutils import *

logger = get_logger(logger_name=__name__)


def log_to_allure(value_a, value_b):
    """Log a step to allure"""

    with allure.step(value_a + ": {}".format(value_b)):
        pass


def allure_screenshot(driver: webdriver.Chrome, message: str = "Result screenshot"):
    """Add a screenshot to the test results"""

    allure.attach(
        driver.get_screenshot_as_png(),
        name=message,
        attachment_type=AttachmentType.PNG,
    )

def log_to_allure_text(message = None, data = None):
    """ """
    with allure.step(message):
        allure.attach(message, data, allure.attachment_type.TEXT)


def assert_with_allure(condition: bool = None, message: str = None, data=None):
    """Assert a condition and log the step using allure"""

    if condition is None:
        raise TypeError("The condition must be a boolean")

    if message is None:
        raise TypeError("The message must supplied")

    data_printout = data if data != None else ''

    with allure.step(f"{message}: \n {pretty_dictionary(data_printout) if isinstance(data, dict) else data_printout}"):

        if not condition:
            logger.error("{}: \n{}".format(message, pretty_dictionary(data) if isinstance(data, dict) else data))
        else:
            logger.info("{}: \n{}".format(message, pretty_dictionary(data) if isinstance(data, dict) else data))

        assert condition, message


def automation_logger(message: str = None, data=None):
    """Log to allure and the local automation file"""

    if message is None:
        raise TypeError("The message must supplied")


    data_printout = data if data != None else ''

    with allure.step(f"{message}: {data_printout}"):
        logger.info("{}: \n{}".format(message, pretty_dictionary(data_printout) if isinstance(data, dict) else data_printout))
