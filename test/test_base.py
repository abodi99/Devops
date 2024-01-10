import pytest
from baseClass import BaseTest

class TestCalculater(BaseTest):
    def test_add(self):
        result = self.calc.add(5, 3)
        assert result == 8

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        assert result == 2

    def test_multiply(self):
        result = self.calc.multiply(5, 3)
        assert result == 15

    def test_divide(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    @pytest.mark.parametrize("a, b, expected_result", [
    (3, 3, 6),
    (3, -3, 0),
    (0, 0, 0),  # Additional test case
    (-5, 5, 0),  # Additional test case
    (10, 5, 15),  # Additional test case
    ])

    def test_addMult(self, a, b, expected_result):
        result = self.calc.add(a,b)
        assert result == expected_result

   
