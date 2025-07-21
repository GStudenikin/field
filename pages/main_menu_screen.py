import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class MainMenuScreen(BasePage):
    
    active_project = (AppiumBy.XPATH, "//android.widget.TextView[@text='Активный проект: ']")
    active_road = (AppiumBy.XPATH, "//android.widget.TextView[@text='Активная дорога: ']")
    projects_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Проекты']")
    roads_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Дороги']")
    road_objects_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Дорожные объекты']")
    map_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Карта']")
    export_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Экспорт']")

    def __init__(self, driver):
        super().__init__(driver)
        self.active_project = self.find(self.active_project)
        self.active_road = self.find(self.active_road)
        self.projects_button = self.find(self.projects_button)
        self.roads_button = self.find(self.roads_button)
        self.road_objects_button = self.find(self.road_objects_button)
        self.map_button = self.find(self.map_button)
        self.export_button = self.find(self.export_button)