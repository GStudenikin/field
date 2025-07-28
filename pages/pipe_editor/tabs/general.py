import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class General(BasePage):

    ELEMENTS = {
        "Состояние": (AppiumBy.XPATH, "//android.widget.TextView[@text='Состояние']"),
        "Км": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Км']]"),
        "м": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='м']]"),
        "Смещение": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Смещение']]"),
        "Направление смещения": (AppiumBy.XPATH, "//android.widget.TextView[@text='Смещение']/following-sibling::android.widget.Button"),
        "Номер трубы": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Номер трубы']]"),
        "Положение": (AppiumBy.XPATH, "//android.widget.TextView[@text='Положение']"),
        "Длина трубы": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Длина трубы, м']]"),
        "Уклон трубы": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Уклон трубы, ‰']]"),
        "Укреп. дна": (AppiumBy.XPATH, "//android.widget.TextView[@text='Укреп. дна']"),
        "Изоляция": (AppiumBy.XPATH, "//android.widget.TextView[@text='Изоляция']"),
        "Грунт основания": (AppiumBy.XPATH, "//android.widget.TextView[@text='Грунт основания']"),
        "Тип основания": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип основания']"),
        "Тип фундамента": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип фундамента']"),
        "Материал фундамента": (AppiumBy.XPATH, "//android.widget.TextView[@text='Материал фундамента']"),
        "Высота насыпи": (AppiumBy.XPATH, "//android.widget.TextView[@text='Высота насыпи, м']"),
        "Глубина заложения": (AppiumBy.XPATH, "//android.widget.TextView[@text='Глубина заложения, м']"),
        "Толщина засыпки": (AppiumBy.XPATH, "//android.widget.TextView[@text='Толщина засыпки, м']"),
        "Помеха": (AppiumBy.XPATH, "//android.widget.TextView[@text='Помеха']"),
        "Угол пересечения": (AppiumBy.XPATH, "//android.widget.TextView[@text='Угол пересечения, º']"),
        "Наименование водотока": (AppiumBy.XPATH, "//android.widget.TextView[@text='Наименование водотока']"),
        "Тип трубопровода": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип трубопровода']"),
        "Осевая нагрузка": (AppiumBy.XPATH, "//android.widget.TextView[@text='Осевая нагрузка, т']"),
        "Год постройки": (AppiumBy.XPATH, "//android.widget.TextView[@text='Год постройки (реконструкции)']"),
        "Год капремонта": (AppiumBy.XPATH, "//android.widget.TextView[@text='Год капремонта']"),
        "Комментарий": (AppiumBy.XPATH, "//android.widget.TextView[@text='Комментарий']"),
        #Отсутствует идентификатор
        "Запись звука": "ПРОПУСК"
    }
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self, element):
        self.click(self.ELEMENTS[element])
    
    def set_condition(self, condition):
        self.click_element("Состояние")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{condition}']"))
    
    def set_km_plus(self, km, m=None):
        self.click_element("Км")
        self.set_text(self.ELEMENTS["Км"], str(km))
        if m != None:
            self.click_element("м")
            self.set_text(self.ELEMENTS["м"], str(m))
    
    def set_offset(self, offset):
        self.click_element("Смещение")
        self.set_text(self.ELEMENTS["Смещение"], str(offset))
    
    def set_pipe_number(self, number):
        self.click_element("Номер трубы")
        self.set_text(self.ELEMENTS["Номер трубы"], str(number))
    
    def set_position(self, position):
        self.click_element("Положение")
        self.click((AppiumBy.XPATH, f"//android.widget.TextView[@text='{position}']"))
    
    def set_pipe_length(self, length):
        self.click_element("Длина трубы")
        self.set_text(self.ELEMENTS["Длина трубы"], str(length))
    
    def set_pipe_slope(self, slope):
        self.click_element("Уклон трубы")
        self.set_text(self.ELEMENTS["Уклон трубы"], str(slope))
    
