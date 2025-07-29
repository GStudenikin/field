from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=10):
        for attempt in range(3):
            try:
                element = self.find(locator, timeout)
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
    
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
        actions.pointer_action.move_to_location(100, coordinates['y'])
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(100+size['width']/2, coordinates['y'])
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

    def back_click(self):
        self.click((AppiumBy.XPATH, "//android.view.View[@content-desc='Назад']"))
    
    def swipe(self, point_start, point_end):
        finger = PointerInput("touch", "finger1")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(point_start[0], point_start[1])
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(point_end[0], point_end[1])
        actions.pointer_action.pointer_up()
        actions.perform()

    def swipe_until_find(self, target_locator, step_x, step_y, outside_object_locator=None):
        """
        Выполняет свайп по элементу или экрану до появления целевого элемента.

        Аргументы:
            target_locator: локатор элемента, который должен появиться на экране.
            step_x: шаг по оси X. Положительное значение — свайп влево, отрицательное — вправо.
            step_y: шаг по оси Y. Положительное значение — свайп вниз, отрицательное — вверх.
            outside_object_locator (опционально): локатор элемента, по которому выполнять свайп.
                Если не указан — свайп выполняется от центра экрана.

        Примечания:
            - Функция предполагает, что местоположение target_locator известно.
            - Автоматический поиск target_locator пока не реализован.
        """
        if outside_object_locator != None:
            size = self.get_size(outside_object_locator)
            location = self.get_location(outside_object_locator)
            start_point = {
                "x": location["x"] + size["width"]/2,
                "y": location["y"] + size["height"] - 30
            }
        else:
            start_point = {
                "x": self.driver.get_window_size()["width"]/2,
                "y": self.driver.get_window_size()["height"]/2
            }
        while self.is_displayed(target_locator, 1) != True:
            self.swipe([start_point["x"], start_point["y"]], [start_point["x"] - step_x, start_point["y"] - step_y])
    
    def set_dropdown(self, value):
        """
        Выбирает элемент из выпадающего списка по тексту.

        Аргументы:
            value (str): Текстовое значение элемента, который нужно выбрать.
        """
        self.swipe_until_find((AppiumBy.XPATH, f"//android.widget.TextView[@text='{value}']"), 0, 100, (AppiumBy.XPATH, "//android.widget.ScrollView"))
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{value}']"))