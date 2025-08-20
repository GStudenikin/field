import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SettingsScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    def click_element(self, element):
        if element == "Документация":
            self.click((AppiumBy.XPATH, "//android.widget.TextView[@text='Документация']/following-sibling::android.view.View[@content-desc='Раскрыть']/following-sibling::android.widget.Button"))
        else:
            self.click((AppiumBy.XPATH, f"//android.view.View[@content-desc='Раскрыть']/following-sibling::android.widget.TextView[@text='{element}']"))
    
    def get_version(self):
        version = self.find((AppiumBy.XPATH, "//android.widget.TextView[@text='Версия приложения: ']/following-sibling::android.widget.TextView"))
        return version.text