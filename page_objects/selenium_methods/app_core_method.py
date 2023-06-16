# created by Abhijeet Thorat at 2023-06-13 19:56.
#

import warnings
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from utilities.allure_methods import allure_screenshot
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.py_logger import get_logger
warnings.simplefilter("always", DeprecationWarning)


logger = get_logger(logger_name=__name__)
class AppCorePage:
    """A class that contains reusable selenium modules"""

    appium_service = AppiumService()

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def app_click(self, ui_xpath: str):
        """Click a clickable element"""
        content = self.driver.find_element("xpath", ui_xpath)
        logger.info(f"{content.text}: Button is clickable")
        self.driver.find_element("xpath", ui_xpath).click()
    # def app_appium_click(self, ui_xpath: str):
    #     """Click a clickable element"""

    #     content = self.driver.find_element(by=AppiumBy.XPATH, value=ui_xpath)
    #     logger.info(f"{content.text}: Button is clickable")
    #     content.click()

    def app_input(self, ui_xpath: str, userinfo: str):
        """A method that sets text into an editable element (text bar, text area, button)"""

      #  self.driver.find_element("xpath", ui_xpath).clear()
        self.driver.find_element("xpath", ui_xpath).send_keys(userinfo)
        logger.info(f"Enter value is {userinfo}")

    def app_explicitWait(self, ui_xpath: str, timeout: float = 30):
        """A method that will help with waiting until a specific condition is met"""

        wait = WebDriverWait(self.driver, timeout=timeout)
        wait.until(EC.element_to_be_clickable((By.XPATH, ui_xpath)))

    def app_get_text(self, ui_xpath):
        """Text variable present in an element. It will fetch the values of the element"""

        value = self.driver.find_element("xpath", ui_xpath).text
        logger.info(f"Text retrieved : {value}")

        return value

    def assert_text(self, ui_xpath: str, expected_value: str):
        """Text assersion. Checking whether the text is available or not. To be deprecated"""

        warnings.warn(
            "The function will be deprecated", DeprecationWarning, stacklevel=2
        )

        try:
            value = self.driver.find_element("xpath", ui_xpath).text
            if value.__contains__(expected_value):
                logger.info(f"Verified text is: {expected_value}")
                assert True, "Text verified"
                allure_screenshot(self.driver,message=value+" is verified")
        except Exception:
            logger.exception(f"{expected_value} is not verified")

    def app_select_index(self, ui_xpath: str, index_value):
        """Select drop down by index"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_index(index_value)

    def app_select_value(self, ui_xpath: str, value):
        """Select drop down by value"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_value(value)

    def app_select_text(self, ui_xpath: str, text):
        """Select drop down by text"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_visible_text(text)

    def app_deselect_index(self, ui_xpath: str, index_value):
        """Deselect drop down by index"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_index(index_value)

    def app_deselect_value(self, ui_xpath: str, value):
        """Deselect dropdown by value"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_value(value)

    def app_deselect_text(self, ui_xpath, text):
        """Deselect dropdown by text"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_visible_text(text)

    def submit_btn(self, ui_xpath):
        """A method in selenium that submits a form. Users can use it only along
        with form or with form elements only"""

        self.driver.find_element("xpath", ui_xpath).submit()

    def file_upload(self, ui_xpath, file_location):
        """Upload a file"""

        uplaod = self.driver.find_element("xpath", ui_xpath)
        uplaod.send_keys(file_location)

    def stop_appium(self):
        """Stop the appium server from running"""

        self.appium_service.stop()
        logger.info("Stopping a appium server...")

    def app_screenshot(self, message: str):
        """To be deprecated. This is a allure method. It should not be inside the core class."""
        warnings.warn(
            "The function will be deprecated", DeprecationWarning, stacklevel=2
        )

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=message,
            attachment_type=AttachmentType.PNG,
        )

    def app_swipe(
        self, startx: float, starty: float, endx: float, endy: float, duration: float
    ):
        """Swiping to a specified location on the app"""

        self.driver.swipe(startx, starty, endx, endy, duration)

    def navigateBack(self):
        """Go back one index history behind"""

        self.driver.back()

    def click_wait_until_found(self, ui_xpath: str, timeout: float=30):
        """Wait until an element is found"""

        condition = EC.presence_of_all_elements_located(locator=(By.XPATH, ui_xpath))

        try:
            WebDriverWait(self.driver, timeout).until(condition)[0].click()
        except TimeoutException:
            logger.exception("Unable to find the element")

    def is_element_available(self, ui_xpath: str):
        """Returning a boolean if element is not found"""

        try:
            self.driver.find_element(By.XPATH, ui_xpath)
        except NoSuchElementException:
            return False
        return True

    def tear_down(self):
        """to quite all current driver sessions"""
        self.driver.quit()

    def scroll_gesture_down(self):
        logger.info("scrolling down")
        self.driver.execute_script('mobile: scrollGesture', {
        'left': 100, 'top': 100, 'width': 200, 'height': 500,
        'direction': 'down',
        'percent': 3.0
        })
    def scroll_gesture_up(self):
        self.driver.execute_script('mobile: scrollGesture', {
        'left': 100, 'top': 100, 'width': 200, 'height': 500,
        'direction': 'up',
        'percent': 3.0
        })

    def swipe_left(self):
        self.driver.execute_script('mobile: scrollGesture', {
        'left': 100, 'top': 100, 'width': 200, 'height': 200,
        'direction': 'left',
        'percent': 0.75
        })

    def swipe_right(self):
        self.driver.execute_script('mobile: scrollGesture', {
        'left': 100, 'top': 100, 'width': 200, 'height': 200,
        'direction': 'right',
        'percent': 0.75
        })
    def click_gesture(self,ui_xpath):
        content = self.driver.find_element("xpath", ui_xpath)
        logger.info(f"{content.text}: is clickable")
        self.driver.execute_script('mobile: clickGesture', {content})
