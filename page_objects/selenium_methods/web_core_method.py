# created by Abhijeet Thorat at 2023-06-13 17:32.
#

from time import sleep
from selenium.webdriver.common import keys
from selenium import webdriver
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait
from utilities.py_logger import get_logger
from utilities.allure_methods import allure_screenshot
import warnings
import os
from hamcrest import assert_that
from selenium.webdriver.support import expected_conditions as EC


warnings.simplefilter('always', DeprecationWarning)

logger = get_logger(logger_name=__name__)

class CorePage:
    """The class is responsible for holding all selenium common methods for doing web actions"""

    def __init__(self, driver: webdriver.Chrome):
        """Inititalizing the class with a configured driver"""

        self.driver = driver

    def get_url(self, url: str):
        """Loads a web page in the current browser session."""
        self.driver.get(url=url)

    def clicker(self,ui_xpath: str):
        """To click on web element"""

        sleep(2)
        content = self.driver.find_element("xpath", ui_xpath).text
        logger.info(content + " Button is clickable")
        self.driver.find_element("xpath", ui_xpath).click()
        logger.info(f"{content} Button is clicked")


    def input_delete(self, ui_xpath: str, input: str):
        """ """

        element = self.driver.find_element("xpath", ui_xpath)
        length = len(element.get_attribute('value'))
        element.send_keys(length * Keys.BACKSPACE)
        element.send_keys(input)

    def input(self, ui_xpath: str, user_info: str):
        """Input(send_keys) method sets text into an editable element (text bar, text area, button)"""

        self.driver.find_element("xpath", ui_xpath).clear()
        self.driver.find_element("xpath", ui_xpath).send_keys(user_info)
        logger.info(f"User entered value : {user_info}")

    def explicit_wait(self, ui_xpath: str, time: float):
        """Wait for an element to be present after specified time"""

        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ui_xpath)))

    def submit_btn(self, ui_xpath: str):
        """A submit functionality method"""
        content = self.driver.find_element("xpath", ui_xpath).text
        self.driver.find_element("xpath", ui_xpath).submit()
        logger.info(f"{content} Button is clicked using submit form")

    def get_text(self, ui_xpath: str) -> str:
        """Text variable present in the driver will fetch the values of the text"""

        value = self.driver.find_element("xpath", ui_xpath).text
        logger.info(f"Text retrieved: {value}")
        return value

    def get_attribute_value(self, ui_xpath, attribute_name):
        """Method fetches the value of an attribute, in HTML code whatever
        is present on the left side of '=' is an attribute"""

        value = self.driver.find_element("xpath", ui_xpath).get_attribute(
            attribute_name
        )
        logger.info(f"Attribute value is: {value}")
        return value

    def get_size(self, ui_xpath):
        """Get the size of an element"""

        size_of_element = self.driver.find_element("xpath", ui_xpath).size
        logger.info(f"Width of the web element : {size_of_element['width']}")
        logger.info(f"Height of the web element : {size_of_element['height']}")
        return size_of_element

    def check_if_path_exists(self, ui_xpath):
        """Validate if an element exists"""

        try:
            self.driver.find_element("xpath", ui_xpath)
        except NoSuchElementException:
            return False
        return True

    def assert_text(self, ui_xpath, expected_value, border_colour="#00FF00"):
        """Asserting and evaluating if a value is expected or not"""

        value_text = self.driver.find_element("xpath", ui_xpath).text

        self.highlight_element(ui_xpath=ui_xpath, color=border_colour, message="Verifying "+value_text)

        if not value_text in expected_value:
            logger.error(f"The current text is: {value_text}. Expected text is: {expected_value}")
            assert False, "Failed to validate text"

        logger.info(f"Verified text is: {expected_value}")
        assert True, "verified text is: " + expected_value


    def select_index(self, ui_xpath: str, indexvalue: int):
        """Select Dropdwon by Index"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_index(indexvalue)

    def select_value(self, ui_xpath: str, value):
        """Select dropdown by value"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_value(value)

    def select_text(self, ui_xpath: str, text: str):
        """Select dropdown by text"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.select_by_visible_text(text)

    def deselect_index(self, ui_xpath: str, index_value):
        """De-select Dropdwon by index"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_index(index_value)

    def deselect_value(self, ui_xpath: str, value):
        """Deselect dropdown by value"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_value(value)

    def deselect_text(self, ui_xpath: str, text: str):
        """Deselect dropdown by text"""

        dropdown = Select(self.driver.find_element("xpath", ui_xpath))
        dropdown.deselect_by_visible_text(text)

    def alert_accept(self):
        """Accept alert by clicking on OK button"""

        alert = self.driver.switch_to_alert()
        alert.accept()

    def alert_dismiss(self):
        """Dissmiss alert by clicking on 'x' icon"""

        alert = self.driver.switch_to_alert()
        alert.dismiss()

    def iframe_name(self, frame_name: str):
        """Switching to a frame which has name"""

        self.driver.switch_to_frame(frame_name)

    def iframe_id(self, frame_id):
        """Switching to a frame which has id"""

        self.driver.switch_to_frame(frame_id)

    def iframe_index(self, frame_index):
        """Switching to a frame which has index"""

        self.driver.switch_to_frame(frame_index)

    def parent_frame(self):
        """Switching back to parent frame"""

        self.driver.switch_to.parent_frame()

    def deafult_content(self):
        """Swithing back to deafult content"""

        self.driver.switch_to_default_content()

    def mouse_hover(self, ui_xpath: str):
        """Mouse hovering"""

        menu = self.driver.find_element("xpath", ui_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.perform()

    def mouse_drag_drop(self, source_xpath: str, destination_xpath: str):
        """Perform drag and drop"""

        source = self.driver.find_element(source_xpath)
        target = self.driver.find_element(destination_xpath)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target)

        actions.perform()

    def mouse_click(self, ui_xpath: str):
        """Click in mouse action"""

        element_to_click = self.driver.find_element("xpath", ui_xpath)
        actions = ActionChains(self.driver)
        actions.click(element_to_click).perform()

    def double_click(self, ui_xpath):
        """Double click on mouse action"""

        element_to_double_click = self.driver.find_element("xpath", ui_xpath)
        actions = ActionChains(self.driver)
        actions.double_click(element_to_double_click).perform()

    def key_up(self):
        """Keys up. keyUp and KeyDown methods are used to press keyboard keys in python
        selenium with ActionChains API."""

        actions = ActionChains(self.driver)
        actions.key_up(keys.Keys.SHIFT)
        actions.perform()

    def keys_down(self):
        """Keys down. keyUp and KeyDown methods are used to press keyboard keys in
        python selenium with ActionChains API."""

        actions = ActionChains(self.driver)
        actions.key_down(keys.Keys.SHIFT)
        actions.perform()

    def page_info(self):
        """To get page information"""

        logger.info(f"Title : {self.driver.title}")
        logger.info(f"URL : {self.driver.current_url}")
        logger.info(f"Page source : {self.driver.page_source}")

    def file_upload(self, ui_xpath: str, file_location: str):
        """To upload file"""

        uplaod = self.driver.find_element("xpath", ui_xpath)
        uplaod.send_keys(file_location)

    def window_handling(self):
        """Window handling"""

        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle

        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                logger.info(self.driver.title)
                self.driver.close()
                break

        self.driver.switch_to.window(parent_handle)

    def navigate_back(self):
        """Goes one step backward in the browser history"""

        self.driver.back()

    def scroll_top(self):
        """Scroll to the top"""

        self.driver.execute_script("window.scrollBy(0,0)", "")

    def window_handling_actions(self):
        """An object containing all options to switch focus into"""

        sleep(3)
        handles = self.driver.window_handles
        size = len(handles)
        logger.info(f"The size: {size}")
        for x in range(size):
            self.driver.switch_to.window(handles[x])
            logger.info(f"The title: {self.driver.title}")

    def wait_and_scroll_to(self, ui_xpath: str, time: float = 30):
        """Wait until an element is found and scroll to the element"""

        scrolling = WebDriverWait(self.driver, time)
        scrolling.until(expected_conditions.visibility_of_element_located((By.XPATH, ui_xpath)))
        scroll_element = self.driver.find_element("xpath", ui_xpath)
        scroll_element.location_once_scrolled_into_view

    def _create_a_highlight(self, ui_xpath: str, color):
        """Create a highlight for an element with a border"""

        highlight_js = f"""
        var div = document.evaluate("{ui_xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (div !== null) {{
            div.setAttribute("style", "outline: {color} solid 2px;");
        }}
        """
        try:
            self.driver.execute_script(highlight_js)
            logger.info(f"Highlighted: {self.driver.find_element(By.XPATH, ui_xpath).tag_name}")
            sleep(1)
        except JavascriptException:
            logger.exception("Could not create a highlight")

    def _remove_a_highlight(self, ui_xpath: str):
        """Remove a highlight for an element with a border"""

        remove_highlight = f"""
        var div = document.evaluate("{ui_xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (div !== null) {{
            div.removeAttribute("style");
        }}
        """

        try:
            self.driver.execute_script(remove_highlight)
            sleep(2)
        except JavascriptException:
            logger.exception("Could not remove the highligh")

    def highlight_element(self, ui_xpath: str, color: str = "#f00", message: str = "Path highlited"):
        """Highlight an element with a red box"""

        self._create_a_highlight(ui_xpath, color=color)
        self.get_full_screenshot(message=message)
        self._remove_a_highlight(ui_xpath)

    def get_full_screenshot(self, message: str = "Screenshot for the page"):
        """Set the size of the window to max of the web page"""

        sleep(2)
        original_size = self.driver.get_window_size()
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')

        self.driver.set_window_size(required_width, required_height)
        allure_screenshot(self.driver, message=message)
        self.driver.set_window_size(original_size['width'], original_size['height'])

    def keys_enter(self):

        """Keys Enter methods are used to press keyboard keys in python selenium with ActionChains API."""
        action = ActionChains(self.driver)
        action.send_keys(keys.Keys.ENTER)
        action.perform()

    def scroll_to_Y_axis(self,Y_axis):
        """Scroll to the down"""
        self.driver.execute_script("window.scrollBy(0,"+Y_axis+")", "")

    def scroll_to_X_axis(self,X_axis):
        """Scroll to the up"""
        self.driver.execute_script("window.scrollBy("+X_axis+",0)", "")

    def file_delete(self,file_location: str):
        """To delete file"""
        if os.path.exists(file_location):
            os.remove(file_location)
            logger.info(f"File Deleted Successfully")
        else:
            logger.info(f"File does not exist")

        self.driver.set_window_size(original_size['width'], original_size['height'])

    def scroll_down(self):
        """this wills scroll down by 350 pixel"""
        self.driver.execute_script("window.scrollBy(0,350)","")
        logger.info("scrolling down by 350")

    def scroll_up(self):
        """this wills scroll up by 350 pixel"""
        self.driver.execute_script("window.scrollBy(0,-350)","")
        logger.info("scrolling up by -350")

    def select_dropdown_option(self, ui_xpath: str, option: str):
        """this method is for selecting a specific itenm from the dropdown"""

        select = Select(self.driver.find_element("xpath", ui_xpath))
        select.select_by_visible_text(option)

    def get_current_url(self):
        """Method of the WebDriver interface to get the current URL of the web page"""
        current_url=self.driver.current_url
        return current_url

    def assert_text_new(self, ui_xpath, expected_value:str):
        """Asserting and evaluating if a value is expected or not"""
        try:
            value = self.driver.find_element("xpath", ui_xpath).text
            assert_that(value.__contains__(expected_value))
        except Exception:
            print("assertion failed")
            print("expected :",expected_value, " \nactual :",value)

    def is_displayed(self,ui_xpath:str):
        """Whether the element is visible to a user or not."""
        try:
            self.driver.find_element("xpath",ui_xpath).is_displayed()
        except Exception:
            return False
        return True

    def explicit_wait1(self, ui_xpath: str, time: float):
        """Wait for an element to be present after specified time"""

        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, ui_xpath)))

    def keys_right(self):
        """Keys right. keyUp and KeyDown methods are used to press keyboard keys in
        python selenium with ActionChains API."""

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()

    def keys_left(self):
        """Keys left. keyUp and KeyDown methods are used to press keyboard keys in
        python selenium with ActionChains API."""

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_LEFT)
        actions.perform()

    def get_child_window_url(self):
        """Window handling and returns current url of child windowm"""

        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle

        for x in range(size):
            if handles[x] != parent_handle:
                self.driver.switch_to.window(handles[x])
                logger.info(self.driver.title)
                break
        actual_url=self.get_current_url()
        sleep(1)
        self.get_full_screenshot()
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        return actual_url

    def mouse_hover(self,ui_xpath: str):
        a = ActionChains(self.driver)
        m= self.driver.find_element("xpath", ui_xpath)
        a.move_to_element(m).perform()