import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class DatePicker(BasePage):
    
    TYPES = {
        "input": (AppiumBy.XPATH, "//android.view.View[@content-desc='Перейти в режим ввода текста']"),
        "pick": (AppiumBy.XPATH, "//android.view.View[@content-desc='Перейти в режим выбора даты']"),
    }

    ELEMENTS = {
        "Дата": (AppiumBy.XPATH, "//android.widget.EditText[//android.widget.TextView[@content-desc='Дата, DD.MM.YYYY']]"),
        "Выбрать": (AppiumBy.XPATH, "//android.widget.TextView[@text='Выбрать']"),
        "Отмена": (AppiumBy.XPATH, "//android.widget.TextView[@text='Отмена']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_input_type(self):
        for type in self.TYPES.keys():
            if type == "input":
                if self.is_displayed(self.TYPES[type]):
                    return "pick"
                else:
                    return "input"
    
    def click_type(self, type):
        self.click(self.TYPES[type])
    
    def click_element(self, name):
        self.click(self.ELEMENTS[name])

    def clear_date(self):
        self.clear_text_field(self.ELEMENTS["Дата"])
    
    def set_date(self, date):
        self.clear_date()
        self.set_text(self.ELEMENTS["Дата"], date)
        self.click_element("Выбрать")