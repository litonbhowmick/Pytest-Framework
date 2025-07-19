import pytest
from Main.Pagefactory.Login_Page import LoginPage
import os
import json
from Test.conftest import data_parser
class TestLoginScenarios:

    @pytest.mark.regression
    @pytest.mark.parametrize("data", data_parser("LoginPage"))
    def test_findcountofjavacources(self, data, init_driver):
        self.driver = init_driver
        login = LoginPage(self.driver)
        courses = login.logintopage(data["username"], data["password"])
        count = courses.courses_count("java")
        assert count == 9, "Count didn't matched"
