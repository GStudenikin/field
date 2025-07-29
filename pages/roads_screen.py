import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class RoadsScreen(BasePage):

    BUTTONS = {
        "+": (AppiumBy.XPATH, "//android.view.View[@content-desc='Создать дорогу']"),
        "Поиск": (AppiumBy.XPATH, "//android.view.View[@content-desc='Поиск']"),
        "Заполнить вручную": (AppiumBy.XPATH, "//android.widget.TextView[@text='Заполнить вручную']"),
        "Импорт из текстового файла": (AppiumBy.XPATH, "//android.widget.TextView[@text='Импорт из текстового файла']")
    }

    SEARCH_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Поиск дороги']]")
    
    # TODO: Реализовать взаимодействие с существующими дорогами
    def __init__(self, driver):
        super().__init__(driver)

    def click_button(self, name):
        self.click(self.BUTTONS[name])
    
    def select_road_swipe(self, road_name):
        self.swipe_select((AppiumBy.XPATH, f"//android.widget.TextView[@text='{road_name}']"))
    
    def set_search_field(self, text):
        input_field = self.find(self.SEARCH_FIELD)
        input_field.send_keys(text)