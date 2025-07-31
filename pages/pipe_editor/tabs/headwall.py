import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class Headwall(BasePage):
    """
    Класс реализует взаимодействие с элементами вкладки 'Оголовки'.
    """
    ELEMENTS = {
        "Левый": (AppiumBy.XPATH, "//android.widget.TextView[@text='Левый']"),
        "Правый": (AppiumBy.XPATH, "//android.widget.TextView[@text='Правый']"),
        "Галерея": (AppiumBy.XPATH, "//android.view.View[@content-desc='Иконка для перехода в галерею']"),
        "Счетчик фото": (AppiumBy.XPATH, "//android.view.View[@content-desc='Иконка для перехода в галерею']/following-sibling::android.widget.TextView"),
        "Камера": (AppiumBy.XPATH, "//android.view.View[@content-desc='Иконка для перехода в камеру']"),
        "Режим работы": (AppiumBy.XPATH, "//android.widget.TextView[@text='Режим работы']"),
        "Тип": (AppiumBy.XPATH, "//android.widget.TextView[@text='Тип']"),
        "Материал": (AppiumBy.XPATH, "//android.widget.TextView[@text='Материал']"),
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
        "Добавить из галереи": (AppiumBy.XPATH, "//android.widget.TextView[@text='Добавить из галереи']/following-sibling::android.widget.Button"),
        "Да": (AppiumBy.XPATH, "//android.widget.TextView[@text='Да']/following-sibling::android.widget.Button"),
        "Нет": (AppiumBy.XPATH, "//android.widget.TextView[@text='Нет']/following-sibling::android.widget.Button")
    }
    
    def click_element(self, element):
        """
        Выполняет нажатие на элемент по ключу из словаря ELEMENTS.

        Аргументы:
            element (str): Ключ элемента в словаре ELEMENTS.
        """
        self.click(self.ELEMENTS[element])
    
    def get_current_side(self):
        """
        Возвращает название текущей активной стороны оголовка.

        Возвращает:
            str: Текст из элемента, обозначающего активный оголовок.
        """
        current_side = self.find((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Активный оголовок']"))
        return current_side.get_attribute("text")
    
    def set_side(self, side):
        """
        Переключает на оголовок на указанной стороне.
        Если уже открыта сторона 'side', ничего не происходит.

        Аргументы:
            side (str): Название стороны на которую нужно переключиться
        """
        if self.get_current_side() != side:
            self.click_element(side)
    
    # TODO: Реализовать работу с хранилищем
    # TODO: Реализовать работу с экраном галереи
    def open_gallery(self):
        """
        Открывает галерею фотографий оголовка
        """
        self.click_element("Галерея")
    
    def photo_camera(self):
        """
        Открывает камеру для создания фото оголовка.
        """
        self.click_element("Камера")
        self.click_element("Сделать новое фото")
    
    def photo_gallery(self):
        """
        Открывает галерею устройства для добавления фото оголовка.
        """
        self.click_element("Камера")
        self.click_element("Добавить из галереи")
    
    def get_photo_count(self):
        """
        Возвращает количество фотографий оголовка.

        Возвращает:
            int: число фотографий
        """
        counter = self.find(self.ELEMENTS["Счетчик фото"])
        return int(counter.get_attribute("text"))
    
    def set_mode(self, mode):
        """
        Устанавливает значение поля 'Режим работы'.

        Аргументы:
            mode (str): Режим работы, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Режим работы"], mode)
    
    def set_type(self, name):
        """
        Устанавливает значение поля 'Тип'.

        Аргументы:
            name (str): Тип, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Тип"], name)
    
    def set_material(self, material):
        """
        Устанавливает значение поля 'Материал'.

        Аргументы:
            material (str): Материал, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Материал"], material)
    
    def set_slope_protection(self, name):
        """
        Устанавливает значение поля 'Укрепление откоса'.

        Аргументы:
            name (str): Тип, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Укрепление откоса"], name)

    def set_apron_reinforcement(self, name):
        """
        Устанавливает значение поля 'Укрепление лотка'.

        Аргументы:
            name (str): Тип, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Укрепление лотка"], name)
    
    def set_channel_stabilization(self, name):
        """
        Устанавливает значение поля 'Укрепление русла'.

        Аргументы:
            name (str): Тип, который нужно выбрать из выпадающего списка.
        """
        self.set_dropdown(self.ELEMENTS["Укрепление русла"], name)

    def set_invert_elevation(self, value):
        """
        Устанавливает значение поля 'Высота до отверстия'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Высота до отверстия"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Высота до отверстия"])
        self.set_text(self.ELEMENTS["Высота до отверстия"], str(value))
    
    def set_portal_width(self, value):
        """
        Устанавливает значение поля 'Ширина портала'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Ширина портала"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Ширина портала"])
        self.set_text(self.ELEMENTS["Ширина портала"], str(value))

    def set_flare_width(self, value):
        """
        Устанавливает значение поля 'Ширина раструба'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Ширина раструба"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Ширина раструба"])
        self.set_text(self.ELEMENTS["Ширина раструба"], str(value))

    def set_flare_depth(self, value):
        """
        Устанавливает значение поля 'Глубина раструба'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Глубина раструба"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Глубина раструба"])
        self.set_text(self.ELEMENTS["Глубина раструба"], str(value))

    def set_wing_thickness(self, value):
        """
        Устанавливает значение поля 'Толщина открылков'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Толщина открылков"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Толщина открылков"])
        self.set_text(self.ELEMENTS["Толщина открылков"], str(value))

    def set_headwall_height(self, value):
        """
        Устанавливает значение поля 'Высота оголовка'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Высота оголовка"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Высота оголовка"])
        self.set_text(self.ELEMENTS["Высота оголовка"], str(value))

    def set_portal_thickness(self, value):
        """
        Устанавливает значение поля 'Толщина портала'

        Аргументы:
            value (int): Значение, которое будет установлено
        """
        self.swipe_until_find(self.ELEMENTS["Толщина портала"], 0, 200)
        self.clear_text_field(self.ELEMENTS["Толщина портала"])
        self.set_text(self.ELEMENTS["Толщина портала"], str(value))

    def switch_raised_headwall(self):
        """
        Переключает чекбокс 'Повышенный (конусный) оголовок'.
        """
        self.swipe_until_find(self.ELEMENTS["Повышенный"], 0, 200)
        self.click_element("Повышенный")
    
    def copy_headwall(self):
        """
        Копирует параметры текущего оголовка в противоположную сторону.
        """
        current = self.get_current_side()
        if current == "Левый":
            self.click_element("Скопировать в правый")
        else:
            self.click_element("Скопировать в левый")
        self.click_element("Да")