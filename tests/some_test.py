import pytest
import os
from selenium import webdriver
from selenium.webdriver.common import by

class TestSomething():

    @pytest.fixture
    def driver(self, request):
        _geckodriver  = os.path.join(os.getcwd(), 'vendor', 'geckodriver')
        if os.path.isfile(_geckodriver):
            _service = FireFoxService(executable_path = _geckodriver)
            driver_ = webdriver.FireFox(service=_service)
        else:
            driver_ = webdriver.FireFox()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_
    
    def test_something(self, driver):
        driver.get("url")
        pass


    

    