"""
Unit tests for Operator class
Tests all calculator operations including edge cases and error handling.
"""
import pytest
import math
from Operators.Operator import Operator, CalculatorError


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_addition(self):
        assert Operator.perform_basic_operation('+', 5, 3) == 8
        assert Operator.perform_basic_operation('+', -5, 3) == -2
        assert Operator.perform_basic_operation('+', 0, 0) == 0
        assert Operator.perform_basic_operation('+', 1.5, 2.5) == 4.0

    def test_subtraction(self):
        assert Operator.perform_basic_operation('-', 5, 3) == 2
        assert Operator.perform_basic_operation('-', 3, 5) == -2
        assert Operator.perform_basic_operation('-', 0, 0) == 0
        assert Operator.perform_basic_operation('-', 10.5, 0.5) == 10.0

    def test_multiplication(self):
        assert Operator.perform_basic_operation('*', 5, 3) == 15
        assert Operator.perform_basic_operation('*', -5, 3) == -15
        assert Operator.perform_basic_operation('*', 0, 100) == 0
        assert Operator.perform_basic_operation('*', 2.5, 4) == 10.0

    def test_division(self):
        assert Operator.perform_basic_operation('/', 10, 2) == 5
        assert Operator.perform_basic_operation('/', 7, 2) == 3.5
        assert Operator.perform_basic_operation('/', -10, 2) == -5

    def test_division_by_zero(self):
        with pytest.raises(CalculatorError, match="Division by zero"):
            Operator.perform_basic_operation('/', 10, 0)

    def test_invalid_operator(self):
        with pytest.raises(CalculatorError, match="Invalid operator"):
            Operator.perform_basic_operation('%', 10, 2)


class TestTrigonometricOperations:
    """Test trigonometric operations."""

    def test_sin(self):
        result = Operator.perform_trigonometric_function('sin', 0)
        assert abs(result - 0) < 1e-10

        result = Operator.perform_trigonometric_function('sin', 90)
        assert abs(result - 1) < 1e-10

        result = Operator.perform_trigonometric_function('sin', 30)
        assert abs(result - 0.5) < 1e-10

    def test_cos(self):
        result = Operator.perform_trigonometric_function('cos', 0)
        assert abs(result - 1) < 1e-10

        result = Operator.perform_trigonometric_function('cos', 90)
        assert abs(result - 0) < 1e-10

        result = Operator.perform_trigonometric_function('cos', 60)
        assert abs(result - 0.5) < 1e-10

    def test_tan(self):
        result = Operator.perform_trigonometric_function('tan', 0)
        assert abs(result - 0) < 1e-10

        result = Operator.perform_trigonometric_function('tan', 45)
        assert abs(result - 1) < 1e-10

    def test_cot(self):
        result = Operator.perform_trigonometric_function('cot', 45)
        assert abs(result - 1) < 1e-10

    def test_trigonometric_with_multiplication(self):
        result = Operator.perform_trigonometric_operation('sin', 2, 30)
        assert abs(result - 1.0) < 1e-10  # 2 * sin(30°) = 2 * 0.5 = 1.0

        result = Operator.perform_trigonometric_operation('cos', 3, 60)
        assert abs(result - 1.5) < 1e-10  # 3 * cos(60°) = 3 * 0.5 = 1.5

    def test_invalid_trig_operator(self):
        with pytest.raises(CalculatorError):
            Operator.perform_trigonometric_function('invalid', 45)


class TestLogarithm:
    """Test logarithm operations."""

    def test_log_base_10(self):
        result = Operator.perform_logarithm(100, 10)
        assert abs(result - 2) < 1e-10

        result = Operator.perform_logarithm(1000, 10)
        assert abs(result - 3) < 1e-10

    def test_log_base_2(self):
        result = Operator.perform_logarithm(8, 2)
        assert abs(result - 3) < 1e-10

        result = Operator.perform_logarithm(16, 2)
        assert abs(result - 4) < 1e-10

    def test_log_base_e(self):
        result = Operator.perform_logarithm(math.e, math.e)
        assert abs(result - 1) < 1e-10

    def test_log_negative_number(self):
        with pytest.raises(CalculatorError, match="Logarithm requires positive number"):
            Operator.perform_logarithm(-10, 10)

    def test_log_invalid_base(self):
        with pytest.raises(CalculatorError, match="Logarithm base must be positive"):
            Operator.perform_logarithm(10, -10)

        with pytest.raises(CalculatorError, match="not equal to 1"):
            Operator.perform_logarithm(10, 1)


class TestPower:
    """Test power operations."""

    def test_power_positive(self):
        assert Operator.perform_power(2, 3) == 8
        assert Operator.perform_power(5, 2) == 25
        assert Operator.perform_power(10, 0) == 1

    def test_power_negative_exponent(self):
        result = Operator.perform_power(2, -1)
        assert abs(result - 0.5) < 1e-10

        result = Operator.perform_power(10, -2)
        assert abs(result - 0.01) < 1e-10

    def test_power_fractional(self):
        result = Operator.perform_power(9, 0.5)
        assert abs(result - 3) < 1e-10

        result = Operator.perform_power(8, 1/3)
        assert abs(result - 2) < 1e-10


class TestModulo:
    """Test modulo operations."""

    def test_modulo(self):
        assert Operator.perform_modulo(10, 3) == 1
        assert Operator.perform_modulo(20, 7) == 6
        assert Operator.perform_modulo(15, 5) == 0

    def test_modulo_by_zero(self):
        with pytest.raises(CalculatorError, match="Modulo by zero"):
            Operator.perform_modulo(10, 0)


class TestPiConstant:
    """Test Pi constant."""

    def test_get_pi(self):
        pi_value = Operator.get_pi()
        assert abs(pi_value - math.pi) < 1e-10
        assert abs(pi_value - 3.14159265358979) < 1e-10
