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
        "Высота насыпи": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Высота насыпи, м']]"),
        "Глубина заложения": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Глубина заложения, м']]"),
        "Толщина засыпки": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Толщина засыпки, м']]"),
        "Помеха": (AppiumBy.XPATH, "//android.widget.TextView[@text='Помеха']"),
        "Угол пересечения": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Угол пересечения, º']]"),
        "Наименование водотока": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Наименование водотока']]"),
        "Тип трубопровода": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип трубопровода']"),
        "Осевая нагрузка": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Осевая нагрузка, т']]"),
        "Год постройки": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Год постройки (реконструкции)']]"),
        "Год капремонта": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Год капремонта']]"),
        "Комментарий": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Комментарий']]"),
        # TODO: Запросить у отдела разработки добавить идентификатор для кнопки записи звука, а также для звуковых файлов
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
        self.set_dropdown(self.ELEMENTS["Положение"], position)
    
    def set_pipe_length(self, length):
        self.click_element("Длина трубы")
        self.set_text(self.ELEMENTS["Длина трубы"], str(length))
    
    def set_pipe_slope(self, slope):
        self.click_element("Уклон трубы")
        self.set_text(self.ELEMENTS["Уклон трубы"], str(slope))
    
    def set_bottom_reinforcement(self, reinforcement):
        self.set_dropdown(self.ELEMENTS["Укреп. дна"], reinforcement, True)
    
    def set_pipe_encasemant(self, encasement):
        self.set_dropdown(self.ELEMENTS["Изоляция"], encasement, True)
    
    def set_subgrade_soil(self, soil):
        self.set_dropdown(self.ELEMENTS["Грунт основания"], soil, True)

    def set_base_type(self, type):
        self.set_dropdown(self.ELEMENTS["Тип основания"], type, True)
    
    def set_foundation_type(self, type):
        self.set_dropdown(self.ELEMENTS["Тип фундамента"], type, True)
    
    def set_foundation_material(self, material):
        self.set_dropdown(self.ELEMENTS["Материал фундамента"], material, True)
    
    def set_embankment_height(self, height):
        self.swipe_until_find(self.ELEMENTS["Высота насыпи"], 0, 200)
        self.click_element("Высота насыпи")
        self.set_text(self.ELEMENTS["Высота насыпи"], str(height))
    
    def set_embedment_depth(self, depth):
        self.swipe_until_find(self.ELEMENTS["Глубина заложения"], 0, 200)
        self.click_element("Глубина заложения")
        self.set_text(self.ELEMENTS["Глубина заложения"], str(depth))
    
    def set_backfill_thickness(self, value):
        self.swipe_until_find(self.ELEMENTS["Толщина засыпки"], 0, 200)
        self.click_element("Толщина засыпки")
        self.set_text(self.ELEMENTS["Толщина засыпки"], str(value))
    
    def set_obstruction(self, obstruction):
        self.set_dropdown(self.ELEMENTS["Помеха"], obstruction, True)
    
    def set_intersection_angle(self, angle):
        self.swipe_until_find(self.ELEMENTS["Угол пересечения"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Угол пересечения"])
        self.click_element("Угол пересечения")
        self.set_text(self.ELEMENTS["Угол пересечения"], str(angle))
    
    def set_watercourse_name(self, name):
        self.swipe_until_find(self.ELEMENTS["Наименование водотока"], 0, 200)
        self.click_element("Наименование водотока")
        self.set_text(self.ELEMENTS["Наименование водотока"], name)
    
    def set_pipeline_type(self, type):
        self.set_dropdown(self.ELEMENTS["Тип трубопровода"], type, True)
    
    def set_axial_load(self, load):
        self.swipe_until_find(self.ELEMENTS["Осевая нагрузка"], 0, 200)
        self.click_element("Осевая нагрузка")
        self.set_text(self.ELEMENTS["Осевая нагрузка"], str(load))
    
    def set_construction_year(self, year):
        self.swipe_until_find(self.ELEMENTS["Год постройки"], 0, 200)
        self.click_element("Год постройки")
        self.set_text(self.ELEMENTS["Год постройки"], str(year))
    
    def set_capital_repair_year(self, year):
        self.swipe_until_find(self.ELEMENTS["Год капремонта"], 0, 200)
        self.click_element("Год капремонта")
        self.set_text(self.ELEMENTS["Год капремонта"], str(year))
    
    def set_comment(self, comment):
        self.swipe_until_find(self.ELEMENTS["Комментарий"], 0, 200)
        self.click_element("Комментарий")
        self.set_text(self.ELEMENTS["Комментарий"], comment)