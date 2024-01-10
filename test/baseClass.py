from calculator.calculator_helper import CalculatorHelper

class BaseTest:
     @classmethod
     def setup_class(cls):
        cls.calc =  CalculatorHelper()
    
     @classmethod
     def teardown_class(cls):
        del cls.calc