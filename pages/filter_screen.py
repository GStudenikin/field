import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from components.date_picker import DatePicker
from appium.webdriver.common.appiumby import AppiumBy

class FilterScreen(BasePage):

    ELEMENTS = {
        "Начало": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Начало']]"),
        "Конец": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Конец']]"),
        "Начальная дата": (AppiumBy.XPATH, "//android.widget.TextView[@text='Дата изменения']/following-sibling::android.widget.EditText[1]"),
        "Конечная дата": (AppiumBy.XPATH, "//android.widget.TextView[@text='Дата изменения']/following-sibling::android.widget.EditText[2]"),
        "ОЧИСТИТЬ": (AppiumBy.XPATH, "//android.widget.TextView[@text='ОЧИСТИТЬ']/following-sibling::android.widget.Button"),
        "ПРИМЕНИТЬ": (AppiumBy.XPATH, "//android.widget.TextView[@text='ПРИМЕНИТЬ']/following-sibling::android.widget.Button")
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
    
    def set_start(self, start):
        """
        Устанавливает значение в поле "Начало".

        Аргументы:
            start (int): значение, которое будет установлено.
        """
        self.click_element("Начало")
        self.set_text(self.ELEMENTS["Начало"], str(start))

    def set_end(self, end):
        """
        Устанавливает значение в поле "Конец".

        Аргументы:
            end (int): значение, которое будет установлено.
        """
        self.click_element("Конец")
        self.set_text(self.ELEMENTS["Конец"], str(end))

    def set_date(self, field, date):
        """
        Открывает поле даты и устанавливает указанную дату через компонент DatePicker.

        Аргументы:
            field (str): Ключ из словаря ELEMENTS для поля даты.
            date (str): Дата в формате 'ДД.ММ.ГГГГ'.
        """
        self.click_element(field)
        date_picker = DatePicker(self.driver)
        date_picker.set_date(date)
    
    def clear(self):
        """
        Очищает фильтр нажатием на кнопку 'ОЧИСТИТЬ'
        """
        self.click_element("ОЧИСТИТЬ")
    
    def accept(self):
        """
        Применяет фильтр нажатием на кнопку 'ПРИМЕНИТЬ'
        """
        self.click_element("ПРИМЕНИТЬ")