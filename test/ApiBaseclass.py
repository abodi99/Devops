from calculator.calculator_helper import CalculatorHelper
from calculator.configuration import Configuration
from calculator.api_client import ApiClient
from calculator.models.calculation import Calculation
from calculator.models.response import Response
from calculator.api.calculator_api import CalculatorApi
import pytest



class ApiBaseTest:
    @classmethod
    def setup_class(cls):
        cfg = Configuration()
        cfg.host = "http://localhost:5000/"
        client = ApiClient(cfg)
        cls.api = CalculatorApi(client)

        

    def teardown_method(self):
        pass

