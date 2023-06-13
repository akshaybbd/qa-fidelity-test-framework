# created by Abhijeet Thorat at 2023-06-13 17:26.
#
from behave import *
from utilities.pulse_logger import *
from helper.fidelity_demo.fedility_services_helper import FidilityHelper
from utilities.pulse_logger import *
FIDE_OBJ = FidilityHelper()

logger = get_logger(logger_name=__name__)

@given("I am on Fidelity services group home page")
def step_impl(context):
    FIDE_OBJ.launch_url(context.driver)

@then('I verify about us menu')
def step_imp(context):
    FIDE_OBJ.about_us(context.driver)

@then('I verify and click Our Products & Services menu')
def step_imp(context):
    FIDE_OBJ.product_services_menu(context.driver)
