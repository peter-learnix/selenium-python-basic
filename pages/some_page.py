from selenium.webdriver.common.by import By

class SomePage:
    _some_locator1 = {"by":By.ID, "value":"somevalue"}
    _some_locator2 = {"by":By.CSS_SELECTOR, }
    _some_locator3 = {"by":By.CSS_SELECTOR, "value":"somevalue"}

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("url")

    def some_action_on_page_(self, param1, param2):
        self.driver.find_element(self._some_locator1["by]"],
                                 self._some_locator1["value"]).send_keys(param1)
        self.driver.find_element(self._some_locator2["by]"],
                                 self._some_locator2["value"]).send_keys(param2)
        
    def some_check_on_page_(self):
        return self.driver.find_element(
                self._some_locator3["by"], self._some_locator3["value"]).is_displayed()