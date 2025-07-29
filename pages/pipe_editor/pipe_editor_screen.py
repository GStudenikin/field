import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PipeEditorScreen(BasePage):
    
    ELEMENTS = {
        "Геопозиция": (AppiumBy.XPATH, "//android.widget.TextView[@text='Точность геопозиции ~ 5,00 м']"),
        "Применить лучший": (AppiumBy.XPATH, "//android.widget.TextView[@text='Скрыть']/following-sibling::android.widget.Button"),
        "Скрыть": (AppiumBy.XPATH, "//android.widget.TextView[@text='Скрыть']/following-sibling::android.widget.Button"),
        "Местоположение": (AppiumBy.XPATH, "//android.view.View[@content-desc='Добавить/обновить местоположение']/following-sibling::android.widget.Button"),
        "Сохранить": (AppiumBy.XPATH, "//android.view.View[@content-desc='Принять']/following-sibling::android.widget.Button"),
    }

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_element(self, element):
        self.click(self.ELEMENTS[element])

    def set_tab(self, tab_name):
        """
        Переключает на вкладку с заданным именем.
        
        Аргументы:
            tab_name (str): Название вкладки, на которую нужно переключиться.
        
        Примечание:
            Метод не выполняет поиск вкладки.
            Свайп выполняется только влево (по оси X).
        """
        target_locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{tab_name}']/following-sibling::android.view.View")
        self.swipe_until_find(target_locator, -350, 0, (AppiumBy.XPATH, "//android.view.View[@content-desc='Панель выбора вкладки']"))
        self.click(target_locator)