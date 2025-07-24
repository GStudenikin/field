import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PipesScreen(BasePage):
    
    ELEMENTS = {
        "Сортировка": (AppiumBy.XPATH, "//android.view.View[@content-desc='Сортировка']"),
        "Фильтр": (AppiumBy.XPATH, "//android.view.View[@content-desc='Фильтр']"),
        # ДЕФЕКТ!!! Необходимо исправить
        "+": (AppiumBy.XPATH, "//android.view.View[@content-desc='Добавить дорогу']"),
        ################################
        "Создать новую": (AppiumBy.XPATH, "//android.widget.TextView[@text='Создать новую']"),
        "Импорт обменного формата": (AppiumBy.XPATH, "//android.widget.TextView[@text='Выбрать из шаблонов']")
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_element(self, element):
        self.click(self.ELEMENTS[element])
    
    def set_sorting(self,sorting_type):
        self.click_element("Сортировка")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{sorting_type}']"))