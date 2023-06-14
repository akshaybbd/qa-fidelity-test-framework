__doc__="""
Notes:
======

 - Fixture code is implemented here
 - See documentation here:

   https://behave.readthedocs.io/en/stable/fixtures.html

"""
from behave import *
import utilities.py_logger as py_logger
from utilities.chrome_driver_utils import initialize_driver
from webdriver_manager.chrome import ChromeDriverManager
from appium.webdriver.appium_service import AppiumService
from utilities.appium_driver_utils import *
from utilities.path_configs import get_path_to_file
from utilities.read_properties import read_config_file
from selenium import webdriver
#from appium import webdriver


logger = py_logger.get_logger(logger_name=__name__)

@fixture
def chrome_driver_setup(context):
    """A setup and tear down for a chrome driver setup"""

    try:
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
       # context.driver = initialize_driver()
        context.driver.maximize_window()
        yield context.driver
    finally:
        context.driver.quit()

@fixture
def appium_server_setup(context):
    """A setup and tear"""
    appium_service = AppiumService()

    try:
        appium_service.start(args=[
            '--address', '127.0.0.1',
            '--port', '4723',
            "--base-path", '/wd/hub',
            ])

        context.driver = initialze_appium_driver(
            app=get_path_to_file('apk', read_config_file(section="app_cap", option="apk_name"),),
            appPackage=read_config_file(section="app_cap", option="ap_pPackage"),
            appActivity=read_config_file(section="app_cap", option="app_activity"),
            platformName=read_config_file(section="app_cap", option="platform_name"),
            noReset=read_config_file(section="app_cap", option="no_reset"),
            instrumentApp=read_config_file(section="app_cap", option="instrument_app")
            )
        yield context.driver
    except Exception:
        logger.exception("There was an error initializing the driver")

    finally:
        context.driver.quit()
        appium_service.stop()


def use_fixture_by_tag(tag = None, context = None, fixture_registry = None):
    """The method that uses a fixture based on a tag name that matches from the scenarios decorators
    :param tag: The tag from the feature files
    :param context: The Behave context
    :fixture registry: A dictionary of the regsitry
    :returns: The use_texture object
    """

    fixture_data = fixture_registry.get(tag, None)

    if fixture_data is None:
        logger.exception(f"Unknown fixture-tag: {tag}")
        raise LookupError(f"Unknown fixture-tag: {tag}")

    fixture_function, fixture_args, fixture_kwargs = fixture_data

    return use_fixture(fixture_function, context, *fixture_args, **fixture_kwargs)
