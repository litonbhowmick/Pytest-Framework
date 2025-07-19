import pytest
from Main.Pagefactory.Login_Page import LoginPage
import os
import json
from Test.conftest import data_parser
class TestLoginScenarios:

    @pytest.mark.smoke
    @pytest.mark.parametrize("json_data", data_parser("LoginPage"))
    def test_logintest(self, init_driver, json_data):
        self.driver = init_driver
        login = LoginPage(self.driver)
        login.logintopage(json_data["username"], json_data["password"])
