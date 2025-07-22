import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ProjectsScreen(BasePage):

    BUTTONS = {
        "+": (AppiumBy.XPATH, "//android.view.View[@content-desc='Кнопка для создания нового проекта']"),
        "Новый проект": (AppiumBy.XPATH, "//android.widget.TextView[@text='Новый проект']"),
        "Импорт обменного формата": (AppiumBy.XPATH, "//android.widget.TextView[@text='Импорт обменного формата']"),
    }
    # To do: Написать взаимодействие с существующим проектом
    def __init__(self, driver):
        super().__init__(driver)

    def click_button(self, name):
        self.click(self.BUTTONS[name])