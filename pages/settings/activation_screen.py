import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ActivationScreen(BasePage):

    ELEMENTS = {
        "Серийный номер": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Серийный номер']]"),
        "Получить": (AppiumBy.XPATH, "//android.widget.TextView[@text='ПОЛУЧИТЬ']/following-sibling::android.widget.Button"),
        "Активировать": (AppiumBy.XPATH, "//android.widget.TextView[@text='АКТИВИРОВАТЬ']/following-sibling::android.widget.Button"),
        "Обработка данных": (AppiumBy.XPATH, "//android.widget.TextView[@text='Обработка данных']")
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_element(self, element):
        """
        Выполняет нажатие на элемент по ключу из словаря ELEMENTS.

        Аргументы:
            element (str): Ключ элемента в словаре ELEMENTS.
        """
        self.click(self.ELEMENTS[element])
    
    def set_serial(self, serial_number):
        self.set_text(self.ELEMENTS["Серийный номер"], serial_number.replace("-", ""))
    
    def activate(self, serial_number):
        self.set_serial(serial_number)
        self.click_element("Активировать")
        self.wait_until_disappears(self.ELEMENTS["Обработка данных"])
        self.back_click()