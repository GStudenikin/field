import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PipesScreen(BasePage):
    
    ELEMENTS = {
        "Сортировка": (AppiumBy.XPATH, "//android.view.View[@content-desc='Сортировка']"),
        "Фильтр": (AppiumBy.XPATH, "//android.view.View[@content-desc='Фильтр']"),
        "+": (AppiumBy.XPATH, "//android.view.View[@content-desc='Создать трубу']"),
        "Создать новую": (AppiumBy.XPATH, "//android.widget.TextView[@text='Создать новую']"),
        "Импорт обменного формата": (AppiumBy.XPATH, "//android.widget.TextView[@text='Выбрать из шаблонов']")
    }

    # TODO: Реализовать взаимодействие с существующими трубами

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_element(self, element):
        """
        Выполняет нажатие на элемент по ключу из словаря ELEMENTS.

        Аргументы:
            element (str): Ключ элемента в словаре ELEMENTS.
        """
        self.click(self.ELEMENTS[element])
    
    def set_sorting(self,sorting_type):
        """
        Устанавливает тип сортировки из выпадающего списка.

        Аргументы:
            sorting_type (str): Текстовое значение сортировки, которое нужно выбрать.
        """
        self.click_element("Сортировка")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{sorting_type}']"))