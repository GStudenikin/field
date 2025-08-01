import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.appium_utils import initialize_appium_driver
from pages.main_menu_screen import MainMenu
from pages.projects_screen import ProjectsScreen
from pages.project_editor_screen import ProjectEditorScreen
from pages.roads_screen import RoadsScreen
from pages.road_editor_screen import RoadEditorScreen
from pages.pipes_screen import PipesScreen
from pages.filter_screen import FilterScreen


driver = initialize_appium_driver()

ms = MainMenu(driver)
ms.click_button("Проекты")

ps = ProjectsScreen(driver)
ps.click_button("+")
ps.click_button("Новый проект")

pes = ProjectEditorScreen(driver)
pes.set_project_name("Тестовый проект9")
pes.set_examination_type("Расширенное")
pes.set_start_date("03.05.1970")
pes.set_end_date("25.05.1995")
pes.set_comment("Бла-бла-бла")
pes.click_element("СОХРАНИТЬ")
ps.back_click()

ms = MainMenu(driver)
ms.click_button("Дороги")
rs = RoadsScreen(driver)
rs.click_button("+")
rs.click_button("Заполнить вручную")
res = RoadEditorScreen(driver)
res.set_name("Тестовая дорога")
res.set_inventory_number("322")
res.set_road_code("223.322")
res.set_status("Региональная")
res.set_category("IВ")
res.set_class("Скоростная дорога")
res.click_element("СОХРАНИТЬ")
ps.back_click()
ps.back_click()
ms = MainMenu(driver)
ms.click_button("Дорожные объекты")
ms.click_button("Трубы")

ps = PipesScreen(driver)
ps.set_sorting("По возрастанию номера трубы")
ps.click_element("Фильтр")

fs = FilterScreen(driver)
fs.set_start(10)
fs.set_end(15)
fs.set_date("Начальная дата", "23.12.1995")
fs.set_date("Конечная дата", "23.12.1995")
fs.accept()

ps = PipesScreen(driver)
ps.click_element("Фильтр")

fs = FilterScreen(driver)
fs.clear()
fs.back_click()

ps = PipesScreen(driver)
ps.back_click()