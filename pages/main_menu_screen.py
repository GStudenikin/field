import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class MainMenu(BasePage):
    
    BUTTONS = {
        "Активный проект": (AppiumBy.XPATH, "//android.widget.TextView[@text='Активный проект: ']"),
        "Активная дорога": (AppiumBy.XPATH, "//android.widget.TextView[@text='Активная дорога: ']"),
        "Проекты": (AppiumBy.XPATH, "//android.widget.TextView[@text='Проекты']"),
        "Дороги": (AppiumBy.XPATH, "//android.widget.TextView[@text='Дороги']"),
        "Дорожные объекты": (AppiumBy.XPATH, "//android.widget.TextView[@text='Дорожные объекты']"),
        "Карта": (AppiumBy.XPATH, "//android.widget.TextView[@text='Карта']"),
        "Экспорт": (AppiumBy.XPATH, "//android.widget.TextView[@text='Экспорт']"),

        #Road objects buttons
        "Трубы": (AppiumBy.XPATH, "//android.widget.TextView[@text='Трубы']"),
        "Мосты": (AppiumBy.XPATH, "//android.widget.TextView[@text='Мосты']"),
        "Столбы": (AppiumBy.XPATH, "//android.widget.TextView[@text='Столбы']"),
        "Метки": (AppiumBy.XPATH, "//android.widget.TextView[@text='Метки']"),

        #Export buttons
        "Обменный формат": (AppiumBy.XPATH, "//android.widget.TextView[@text='Обменный формат']"),
        "Архив CSV": (AppiumBy.XPATH, "//android.widget.TextView[@text='Архив CSV']"),
        "Отчет": (AppiumBy.XPATH, "//android.widget.TextView[@text='Отчет']")
    }


    def __init__(self, driver):
        super().__init__(driver)

    def click_button(self, name):
        """
        Выполняет нажатие на элемент по ключу из словаря BUTTONS.

        Аргументы:
            name (str): Ключ элемента в словаре BUTTONS.
        """
        self.click(self.BUTTONS[name])