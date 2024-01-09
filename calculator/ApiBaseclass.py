from calculator_helper import CalculatorHelper
from calculator_api.configuration import Configuration
from calculator_api.api_client import ApiClient
from calculator_api.models.calculation import Calculation
from calculator_api.models.response import Response
from calculator_api.api.calculator_api import CalculatorApi
import pytest



class ApiBaseTest:
    @classmethod
    def setup_class(cls):
        cfg = Configuration()
        cfg.host = "http://192.168.1.113:5000"
        client = ApiClient(cfg)
        cls.api = CalculatorApi(client)

        

    def teardown_method(self):
        pass

