import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

#Необходимо реализовать функционал для режима редактирования

class RoadEditorScreen(BasePage):
    ELEMENTS = {
        "Название": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Название']]"),
        "Учётный номер": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Учётный номер']]"),
        "Шифр": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Шифр']]"),
        "Статус": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Статус']]"),
        "Категория": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Категория']]"),
        "Класс": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Класс']]"),
        "СОХРАНИТЬ": (AppiumBy.XPATH, "//android.widget.TextView[@text='СОХРАНИТЬ']/following-sibling::android.widget.Button")
    }
    
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, element):
        self.click(self.ELEMENTS[element])
    
    def set_name(self, name):
        self.click_element("Название")
        self.set_text(self.ELEMENTS["Название"], name)

    def set_inventory_number(self, number):
        self.click_element("Учётный номер")
        self.set_text(self.ELEMENTS["Учётный номер"], number)
    
    def set_road_code(self, code):
        self.click_element("Шифр")
        self.set_text(self.ELEMENTS["Шифр"], code)
    
    def set_status(self, status):
        self.click_element("Статус")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{status}']"))

    def set_category(self, category):
        self.click_element("Категория")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{category}']"))
    
    def set_class(self, class_name):
        self.click_element("Класс")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{class_name}']"))