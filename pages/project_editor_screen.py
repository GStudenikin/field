import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

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
        self.click(self.ELEMENTS[element])
    
    def select_examination_type(self, examination_name):
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{examination_name}']"))
    
    def project_name(self, name):
        self.set_text(self.ELEMENTS["Название проекта"], name)
    
    def comment(self, text):
        self.set_text(self.ELEMENTS["Комментарий"], text)