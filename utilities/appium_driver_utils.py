# created by Abhijeet Thorat at 2023-06-13 20:13.
#
from appium import webdriver

def initialze_appium_driver(

    executor="http://127.0.0.1:4723/wd/hub", **capabilities: dict
):
    """Initializing the appium driver
    :desired_capabilities: Required capabilities for the driver
    :returns: The appium driver with correct options and configurations"""

    # TODO: Do error handling and give desired capabilities optional fields. Also,
    # TODO: make sure that you replace desired capabilities with Options class. desired caps has been deprecated.

    return webdriver.Remote(
        command_executor=executor, desired_capabilities=capabilities
    )
