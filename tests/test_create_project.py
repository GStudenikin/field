import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.appium_utils import initialize_appium_driver
from appium.webdriver.common.appiumby import AppiumBy
from pages.onboarding import Onboarding
from pages.main_menu_screen import MainMenu
from pages.settings.activation_screen import ActivationScreen
from pages.settings.settings_screen import SettingsScreen
from pages.project_editor_screen import ProjectEditorScreen

def fill_project(
        name,
        driver=None,
        **kwargs
):
    """
    Заполняет форму проекта в мобильном приложении.

    Функция задаёт название проекта и при наличии дополнительных аргументов
    устанавливает соответствующие поля (тип обследования, даты, комментарий).
    После заполнения форма сохраняется.

    Аргументы:
        name (str): Название проекта.
        driver (Appium WebDriver, optional): Экземпляр драйвера Appium. 
            Если не передан, будет создан через `initialize_appium_driver()`.
        **kwargs: Дополнительные параметры для заполнения формы.
            - type (str): Тип обследования.
            - start_date (str): Дата начала проекта.
            - end_date (str): Дата окончания проекта.
            - comment (str): Комментарий к проекту.
    
    Примечание:
        В конце работы функция автоматически нажимает кнопку «Сохранить».
    """
    if driver is None:
        driver = initialize_appium_driver()
    project_editor_screen = ProjectEditorScreen(driver)
    project_editor_screen.set_project_name(name)
    
    mapping = {
        "type": project_editor_screen.set_examination_type,
        "start_date": project_editor_screen.set_start_date,
        "end_date": project_editor_screen.set_end_date,
        "comment": project_editor_screen.set_comment
    }

    for field_name, setter in mapping.items():
        value = kwargs.get(field_name)
        if value is not None:
            setter(value)
    
    project_editor_screen.click_element("Сохранить")


@pytest.fixture()
def driver():
    driver = initialize_appium_driver()
    yield driver
    main = MainMenu(driver)
    while main.is_displayed((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Главное меню")')) == False:
        main.back_click()
    main.click_button("Настройки")
    settings = SettingsScreen(driver)
    print("Версия: ", settings.get_version)
    settings.click_element("Лицензия")
    #driver.quit()


@pytest.fixture()
def close_onboarding(driver):
    onboarding = Onboarding(driver)
    onboarding.click_element("Пропустить")
    main_menu = MainMenu(driver)
    main_menu.click_button("Активировать")
    act = ActivationScreen(driver)
    act.activate("MBX-0434-6455-7923-4743-3682-1876-2612")
    act.back_click
    return driver


def test_simple(close_onboarding):
    main = MainMenu(close_onboarding)
    assert main.is_displayed((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Главное меню")'))