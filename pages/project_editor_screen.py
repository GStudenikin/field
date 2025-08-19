import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from components.date_picker import DatePicker
from appium.webdriver.common.appiumby import AppiumBy

#Необходимо реализовать функционал для режима редактирования

class ProjectEditorScreen(BasePage):
    ELEMENTS = {
        "Название проекта": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Название проекта']]"),
        "Вид обследования": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Вид обследования']]"),
        "Начало": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Начало']]"),
        "Окончание": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Окончание']]"),
        "Комментарий": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Комментарий']]"),
        "СОХРАНИТЬ": (AppiumBy.XPATH, "//android.widget.TextView[@text='СОХРАНИТЬ']/following-sibling::android.widget.Button")
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
    
    def set_examination_type(self, examination_name):
        """
        Устанавливает вид обследования из выпадающего списка.

        Аргументы:
            examination_name (str): текстовое значение, которое нужно выбрать.
        """
        self.set_dropdown(self.ELEMENTS["Вид обследования"], examination_name)
    
    def set_project_name(self, name):
        """
        Устанавливает значение в поле 'Вид обследования'.

        Аргументы:
            name (str): текстовое значение, которое будет установлено.
        """
        self.click_element("Название проекта")
        self.set_text(self.ELEMENTS["Название проекта"], name)
    
    def set_comment(self, text):
        self.click_element("Комментарий")
        self.set_text(self.ELEMENTS["Комментарий"], text)
    
    def set_start_date(self, date):
        self.click_element("Начало")
        date_picker = DatePicker(self.driver)
        date_picker.set_date(date)

    def set_end_date(self, date, method = "input"):
        self.click_element("Окончание")
        date_picker = DatePicker(self.driver)
        date_picker.set_date(date)