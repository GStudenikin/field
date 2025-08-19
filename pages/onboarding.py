import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class Onboarding(BasePage):
    BUTTONS = {
        "Пропустить": (AppiumBy.XPATH, "//android.widget.TextView[@text='Пропустить']/following-sibling::android.widget.Button"),
        "Далее": (AppiumBy.XPATH, "//android.widget.TextView[@text='Далее']/following-sibling::android.widget.Button"),
        "Начать": (AppiumBy.XPATH, "//android.widget.TextView[@text='Начать']/following-sibling::android.widget.Button")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, element):
        """
        Выполняет нажатие на кнопку по ключу из словаря BUTTONS.

        Аргументы:
            element (str): Ключ элемента в словаре BUTTONS.
        """
        self.click(self.BUTTONS[element])