import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class Segments(BasePage):
    
    ELEMENTS = {
        "Количество участков": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Количество участков']]"),
        "Тип": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип']"),
        "Материал": (AppiumBy.XPATH, "//android.widget.TextView[@text='Материал']"),
        "Кол-во очков": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Кол-во очков']]"),

        # Отображение следующих элементов зависит от поля Тип
        # Тип - Круглая: Диаметр
        # Тип - Прямоугольная: Высота, Ширина
        # Тип - Овоидальная: Высота, Ширина, Диаметр узкой части
        # Тип - Арочная: Высота, Ширина
        # Тип - Сводчатая: Высота, Ширина, Диаметр узкой части
        # Тип - Прочее: Высота, Ширина
        
        "Высота": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Высота, м']]"),
        "Диаметр": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Диаметр, м']]"),
        "Диаметр узкой части": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Диаметр узкой части, м']]"),
        "Ширина": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Ширина, м']]"),
        
        ########################################################

        "Длина": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Длина, м']]"),
        "Толщина стенки": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Толщина стенки, см']]"),
        "Зазор между звеньями": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Зазор между звеньями, см']]"),
        "Схема участка": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='количество звеньев x длина звена + …']]"),
        "Тип входного звена": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Тип входного звена']]"),
        "Тип выходного звена": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Тип выходного звена']]")
    }

    # TODO: реализовать настройку участков после того, как разработчики реализуют идентификатор для активного участка

    def click_element(self, element):
        self.click(self.ELEMENTS[element])
    
    def set_number_of_sections(self, number):
        self.clear_text_field(self.ELEMENTS["Количество участков"])
        self.set_text(self.ELEMENTS["Количество участков"], str(number))
    
    def set_segment_type(self, type):
        self.click_element("Тип")
        self.set_dropdown(type)

    def set_material(self, name):
        self.click_element("Материал")
        self.set_dropdown(name)
    
    def set_number_of_joints(self, number):
        self.clear_text_field(self.ELEMENTS["Кол-во очков"])
        self.set_text(self.ELEMENTS["Кол-во очков"], str(number))
    
    def set_height(self, height):
        self.set_text(self.ELEMENTS["Высота"], str(height))
    
    def set_diameter(self, diameter):
        self.set_text(self.ELEMENTS["Диаметр"], str(diameter))
    
    def set_min_diameter(self, diameter):
        self.set_text(self.ELEMENTS["Диаметр узкой части"], str(diameter))
    
    def set_width(self, width):
        self.set_text(self.ELEMENTS["Ширина"], str(width))
    
    def set_length(self, length):
        self.swipe_until_find(self.ELEMENTS["Длина"], 0, 200)
        self.set_text(self.ELEMENTS["Длина"], str(length))

    def set_wall_thickness(self, thickness):
        self.swipe_until_find(self.ELEMENTS["Толщина стенки"], 0, 200)
        self.set_text(self.ELEMENTS["Толщина стенки"], str(thickness))

    def set_joint_gap(self, gap):
        self.swipe_until_find(self.ELEMENTS["Зазор между звеньями"], 0, 200)
        self.set_text(self.ELEMENTS["Зазор между звеньями"], str(gap))
    
    def set_culvert_layout(self, layout):
        # TODO: необходимо реализовать разбор схемы
        pass

    def set_inlet_type(self, type):
        self.swipe_until_find(self.ELEMENTS["Тип входного звена"], 0, 200)
        self.set_text(self.ELEMENTS["Тип входного звена"], type)
    
    def set_outlet_type(self, type):
        self.swipe_until_find(self.ELEMENTS["Тип входного звена"], 0, 200)
        self.set_text(self.ELEMENTS["Тип выходного звена"], type)