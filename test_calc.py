import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self,12, 1) == 13

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self,13, 4) == 9

    def test_division_success(self):
        assert self.calculator.division(self,20, 10) == 2

    def test_multiply_success(self):
        assert self.calculator.multiply(self,2, 4) == 8