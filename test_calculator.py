"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)
        assert 12 == calculator.add(7, 5)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
        assert 3 == calculator.subtract(7, 4)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)
        assert 100 == calculator.multiply(10, 10)

    def test_divide(self):
        assert 4 == calculator.divide(8, 2)
        assert 2 == calculator.divide(34, 17