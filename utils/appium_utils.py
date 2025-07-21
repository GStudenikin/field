# utils/appium_utils.py
from appium import webdriver
from appium.options.android import UiAutomator2Options  # Или другой драйвер

def initialize_appium_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "BV7100RU0006330"
    options.app_package = "com.indorsoft.indorfield"
    options.app_activity = "com.indorsoft.indorfield.MainActivity"
    options.no_reset = True

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    return driver