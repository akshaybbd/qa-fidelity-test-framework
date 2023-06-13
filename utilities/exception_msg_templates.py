# created by Abhijeet Thorat at 2023-06-13 17:39.
#

import allure
import warnings

warnings.simplefilter("always", DeprecationWarning)


def assertion_templates(a, result):

    assertion_template = "Step Validation Failed with {0}. Returned value is: {1}"
    message = assertion_template.format(type(a).__name__, result)
    with allure.step("Response Error Message: {}".format(message)):
        pass
    assert False
    return message


def exception_templates(ae):
    exception_template = "An exception of type {0} occurred."
    message = exception_template.format(type(ae).__name__)
    with allure.step("Response Error Message: {}".format(message)):
        pass
    assert False
    return message


def log_to_allure(var_a, var_b):
    warnings.warn("The function will be deprecated. Consider using the 'allure_methods.py'", DeprecationWarning, stacklevel=2)
    with allure.step(var_a + ": {}".format(var_b)):
        pass
