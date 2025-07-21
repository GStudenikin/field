from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        element.click()
    
    def is_displayed(self, locator, timeout=10):
        try:
            element = self.find(locator, timeout)
            return element.is_displayed()
        except:
            return False