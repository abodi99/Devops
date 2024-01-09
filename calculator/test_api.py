import pytest
import json
import requests


from calculator.calculator_helper import CalculatorHelper
from calculator_api.configuration import Configuration
from calculator_api.api_client import ApiClient
from calculator_api.models.calculation import Calculation
from calculator_api.models.response import Response
from calculator_api.api.calculator_api import CalculatorApi
from test.ApiBaseclass import ApiBaseTest


class TestCalculater(ApiBaseTest):

    def test_addition(self):
        res = self.api.operations_add_subtract_multiply_divide(Calculation(operation="add", operand1=3, operand2=3))

        assert  float(res.result) == float(6)

    def test_subtraction(self):
        res = self.api.operations_add_subtract_multiply_divide(Calculation(operation="subtract", operand1=3, operand2=3))

        assert  float(res.result) == float(0)

    def test_multiplication(self):
        res = self.api.operations_add_subtract_multiply_divide(Calculation(operation="multiply", operand1=3, operand2=3))

        assert  float(res.result) == float(9)

    def test_division(self):
        res = self.api.operations_add_subtract_multiply_divide(Calculation(operation="divide", operand1=3, operand2=3))

        assert  float(res.result) == float(1)



            

        
        
            




        
        
        
