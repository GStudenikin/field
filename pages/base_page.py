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
        """
        Ожидает появления элемента на экране и возвращает его.

        Аргументы:
            locator (tuple): локатор элемента.
            timeout (int, по умолчанию 10): максимальное время ожидания в секундах.

        Возвращает:
            WebElement: найденный элемент.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=10):
        """
        Выполняет клик по элементу, повторяя попытку до 3 раз при StaleElementReferenceException.

        Аргументы:
            locator (tuple): локатор элемента.
            timeout (int, по умолчанию 10): максимальное время ожидания в секундах.
        """
        for attempt in range(3):
            try:
                element = self.find(locator, timeout)
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
    
    def is_displayed(self, locator, timeout=10):
        """
        Проверяет, отображается ли элемент на экране.

        Аргументы:
            locator (tuple): локатор элемента.
            timeout (int, по умолчанию 10): максимальное время ожидания в секундах.

        Возвращает:
            bool: True, если элемент отображается, иначе False.
        """
        try:
            element = self.find(locator, timeout)
            return element.is_displayed()
        except:
            return False
    
    def get_location(self, locator):
        """
        Возвращает координаты левого верхнего угла элемента.

        Аргументы:
            locator (tuple): локатор элемента.

        Возвращает:
            dict: Словарь с координатами {'x': int, 'y': int}.
        """
        return self.find(locator).location
    
    def get_size(self, locator):
        """
        Возвращает ширину и высоту элемента по локатору.

        Аргументы:
            locator (tuple): локатор элемента.

        Возвращает:
            dict: Словарь с размерами {'width': int, 'height': int}.
        """
        return self.find(locator).size

    def get_center(self, locator):
        """
        Вычисляет координаты центра элемента.

        Аргументы:
            locator (tuple): локатор элемента.
        
        Возвращает:
            dict: словарь с координатами центра {'x': int, 'y': int}
        """
        location = self.get_location(locator)
        size = self.get_size(locator)
        return {'x': location['x'] + size['width'] / 2, 'y': location['y'] + size['height'] / 2}
    
    def swipe_select(self, locator):
        """
        Выполняет горизонтальный свайп по элементу.

        Аргументы:
            locator (tuple): локатор элемента, который будет выбран с помощью свайпа.
        """
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
        """
        Очищает поле соответствующее локатору.

        Аргументы:
            locator (tuple): поле, которое необходимо очистить.
        """
        element = self.find(locator)
        element.click()
        self.driver.press_keycode(29, metastate=4096) # Ctrl+A
        self.driver.press_keycode(67) # Delete
    
    def set_text(self, locator, text):
        """
        Устанавливает в поле ввода текст.

        Аргументы:
            locator (tuple): поле, в которое необходимо ввести текст.
            text (str): текст, который необходимо ввести
        """
        element = self.find(locator)
        element.click()
        element.send_keys(text)

    def back_click(self):
        """
        Выполняет нажатие на кнопку назад.
        """
        self.click((AppiumBy.XPATH, "//android.view.View[@content-desc='Назад']"))
    
    def swipe(self, point_start, point_end):
        """
        Выполняет свайп от начальной до конечной точки на экране.

        Аргументы:
            point_start (list[int]): Координаты начальной точки в формате [x, y].
            point_end (list[int]): Координаты конечной точки в формате [x, y].
        """
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
            step_x (int): шаг по оси X. Положительное значение — свайп влево, отрицательное — вправо.
            step_y (int): шаг по оси Y. Положительное значение — свайп вниз, отрицательное — вверх.
            outside_object_locator (tuple, optional): локатор элемента, по которому выполнять свайп.
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
    
    def set_dropdown(self, field, value, swipe=False):
        """
        Открывает выпадающий список и выбирает указанное значение.

        Аргументы:
            field (tuple): локатор поля, которое нужно открыть для выбора значения.
            value (str): текстовое значение элемента, который нужно выбрать.
            swipe (bool, по умолчанию False): если True - предварительно прокручивает экран до обнаружения поля.
        """
        if swipe:
            self.swipe_until_find(field, 0, 200)
        self.click(field)
        self.swipe_until_find((AppiumBy.XPATH, f"//android.widget.TextView[@text='{value}']"), 0, 100, (AppiumBy.XPATH, "//android.widget.ScrollView"))
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{value}']"))