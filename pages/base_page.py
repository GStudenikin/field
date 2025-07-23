from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        element.click()
    
    def is_displayed(self, locator, timeout=10):
        try:
            element = self.find(locator, timeout)
            return element.is_displayed()
        except:
            return False
    
    def get_location(self, locator):
        return self.find(locator).location
    
    def get_size(self, locator):
        return self.find(locator).size

    def get_center(self, locator):
        location = self.get_location(locator)
        size = self.get_size(locator)
        return {'x': location['x'] + size['width'] / 2, 'y': location['y'] + size['height'] / 2}
    
    def swipe_select(self, locator):
        finger = PointerInput("touch", "finger1")
        actions = ActionBuilder(self.driver, mouse=finger)
        coordinates = self.get_center(locator)
        size = self.driver.get_window_size()
        actions.pointer_action.move_to_location(coordinates['x'], coordinates['y'])
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(coordinates['x']+size['width']/2, coordinates['y'])
        actions.pointer_action.pointer_up()
        actions.perform()
    
    def clear_text_field(self, locator):
        element = self.find(locator)
        element.click()
        self.driver.press_keycode(29, metastate=4096)
        self.driver.press_keycode(67)
    
    def set_text(self, locator, text):
        element = self.find(locator)
        element.click()
        element.send_keys(text)
