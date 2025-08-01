import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class DatePicker(BasePage):
# TODO: реализовать ввод с помощью пикера, а не поля ввода    
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
        """
        Определяет текущий способ ввода даты на экране.

        Возвращает:
            str: "pick", если отображается выбор даты из календаря,
                иначе "input" (ввод вручную).
        """
        return "pick" if self.is_displayed(self.TYPES["input"]) else "input"
    
    def click_type(self, type):
        """
        Выполняет клик по переключателю способа ввода даты.

        Аргументы:
        type (str): тип ввода, "input" или "pick".
        """
        self.click(self.TYPES[type])
    
    def click_element(self, name):
        """
        Выполняет нажатие на элемент по ключу из словаря ELEMENTS.

        Аргументы:
            element (str): Ключ элемента в словаре ELEMENTS.
        """
        self.click(self.ELEMENTS[name])

    def clear_date(self):
        """
        Очищает текстовое поле даты.
        """
        self.clear_text_field(self.ELEMENTS["Дата"])
    
    def set_date(self, date, method="input"):
        """
        Устанавливает дату в поле даты.

        Аргументы:
            date (str): дата в формате "дд.мм.гггг".
            method (str, по умолчанию "input"): способ установки — "input" (ручной ввод) или "pick" (календарь).

        Примечание:
            При выборе "pick" логика ещё не реализована.
        """
        if method == "input":
            self.click_type("input")
            self.clear_date()
            self.set_text(self.ELEMENTS["Дата"], date.replace(".", ""))
        else:
            pass
        self.click_element("Выбрать")