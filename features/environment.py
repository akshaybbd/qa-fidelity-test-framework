# created by Abhijeet Thorat at 2023-06-13 17:22.
#

from behave.fixture import fixture_call_params
from fixtures.connection_fixture import (
    use_fixture_by_tag,
    chrome_driver_setup,
    appium_server_setup,
 )
import utilities.py_logger as py_logger

logger = py_logger.get_logger(logger_name=__name__)

def fixture_registries(context):
    """The registries that exist in the function scenarios.
    :param context: The behave context
    :returns: Dict object with registries
    """
    return {
        "chrome.driver": fixture_call_params(chrome_driver_setup),
        "appium.server": fixture_call_params(appium_server_setup),
    }

def before_tag(context, tag):
    """This method is ran everytime it notices a tag. Either from the entire feature file or scenarios."""
    if tag.startswith("chrome.") or tag.startswith("appium."):
        return use_fixture_by_tag(tag, context, fixture_registries(context))
