import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class Headwall(BasePage):
    
    ELEMENTS = {
        "Левый": (AppiumBy.XPATH, "//android.widget.TextView[@text='Левый']"),
        "Правый": (AppiumBy.XPATH, "//android.widget.TextView[@text='Правый']"),
        "Галерея": (AppiumBy.XPATH, "//android.view.View[@content-desc='Иконка для перехода в галерею']"),
        "Камера": (AppiumBy.XPATH, "//android.view.View[@content-desc='Иконка для перехода в камеру']"),
        "Режим работы": (AppiumBy.XPATH, "//android.widget.TextView[@text='Режим работы']"),
        "Тип": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип']"),
        "Укрепление откоса": (AppiumBy.XPATH, "//android.widget.TextView[@text='Укрепление откоса']"),
        "Укрепление лотка": (AppiumBy.XPATH, "//android.widget.TextView[@text='Укрепление лотка']"),
        "Укрепление русла": (AppiumBy.XPATH, "//android.widget.TextView[@text='Укрепление русла']"),

        # Отображение следующих элементов зависит от поля Тип
        # Тип - Раструбный: Высота до отверстия, Ширина портала, Ширина раструба, Глубина раструба, Толщина открылков, Высота оголовка, Толщина портала
        # Тип - Портальный: Высота до отверстия, Ширина портала, Высота оголовка, Толщина портала
        # Тип - Без оголовка: пусто
        # Тип - Коридорный: Высота до отверстия, Ширина портала, Ширина раструба, Глубина раструба, Толщина открылков, Высота оголовка, Толщина портала
        # Тип - Воротниковый: Высота до отверстия, Высота оголовка, Толщина портала
        # Тип - Обтекаемый: Высота до отверстия, Ширина портала, Высота оголовка, Толщина портала

        "Высота до отверстия": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Высота до отверстия, м']]"),
        "Ширина портала": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Ширина портала, м']]"),
        "Ширина раструба": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Ширина раструба, м']]"),
        "Глубина раструба": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Глубина раструба, м']]"),
        "Толщина открылков": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Толщина открылков, м']]"),
        "Высота оголовка": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Высота оголовка, м']]"),
        "Толщина портала": (AppiumBy.XPATH, "//android.widget.EditText[.//android.widget.TextView[@text='Толщина портала, м']]"),

        ########################################################

        "Повышенный": (AppiumBy.XPATH, "//android.widget.TextView[@text='Повышенный (конусный) оголовок']/preceding-sibling::android.widget.CheckBox"),
        "Скопировать в правый": (AppiumBy.XPATH, "//android.widget.TextView[@text='СКОПИРОВАТЬ В ПРАВЫЙ']/following-sibling::android.widget.Button"),
        "Скопировать в левый": (AppiumBy.XPATH, "//android.widget.TextView[@text='СКОПИРОВАТЬ В ЛЕВЫЙ']/following-sibling::android.widget.Button"),
        "Сделать новое фото": (AppiumBy.XPATH, "//android.widget.TextView[@text='Сделать новое фото']/following-sibling::android.widget.Button"),
        "Добавить из галереи": (AppiumBy.XPATH, "//android.widget.TextView[@text='Добавить из галереи']/following-sibling::android.widget.Button")
    }
    
    def click_element(self, element):
        self.click(self.ELEMENTS[element])