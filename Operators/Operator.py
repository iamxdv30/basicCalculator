"""
Calculator Operations Module
Provides basic, advanced, and trigonometric operations following clean code principles.
"""
import math
from typing import Union


class CalculatorError(Exception):
    """Custom exception for calculator operations."""
    pass


class Operator:
    """
    Calculator operator class providing static methods for various mathematical operations.
    Follows single responsibility principle with separate methods for different operation types.
    """

    @staticmethod
    def perform_basic_operation(operator: str, num1: float, num2: float) -> float:
        """
        Perform basic arithmetic operations.

        Args:
            operator: One of '+', '-', '*', '/'
            num1: First operand
            num2: Second operand

        Returns:
            Result of the operation

        Raises:
            CalculatorError: If operator is invalid or division by zero
        """
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else None
        }

        if operator not in operations:
            raise CalculatorError(f"Invalid operator: {operator}")

        result = operations[operator](num1, num2)
        if result is None:
            raise CalculatorError("Division by zero")

        return result

    @staticmethod
    def perform_trigonometric_operation(operator: str, num1: float, angle_degrees: float) -> float:
        """
        Perform trigonometric operations on a number.

        Args:
            operator: One of 'sin', 'cos', 'tan', 'cot'
            num1: Number to multiply with trigonometric result
            angle_degrees: Angle in degrees

        Returns:
            Result of num1 * trig_function(angle)

        Raises:
            CalculatorError: If operator is invalid or calculation error occurs
        """
        angle_radians = math.radians(angle_degrees)

        try:
            operations = {
                "sin": lambda a: math.sin(a),
                "cos": lambda a: math.cos(a),
                "tan": lambda a: math.tan(a),
                "cot": lambda a: 1 / math.tan(a)
            }

            if operator not in operations:
                raise CalculatorError(f"Invalid trigonometric operator: {operator}")

            return num1 * operations[operator](angle_radians)

        except (ValueError, ZeroDivisionError) as e:
            raise CalculatorError(f"Trigonometric calculation error: {str(e)}")

    @staticmethod
    def perform_trigonometric_function(operator: str, angle_degrees: float) -> float:
        """
        Perform standalone trigonometric function.

        Args:
            operator: One of 'sin', 'cos', 'tan', 'cot'
            angle_degrees: Angle in degrees

        Returns:
            Result of trigonometric function

        Raises:
            CalculatorError: If operator is invalid or calculation error occurs
        """
        angle_radians = math.radians(angle_degrees)

        try:
            operations = {
                "sin": lambda a: math.sin(a),
                "cos": lambda a: math.cos(a),
                "tan": lambda a: math.tan(a),
                "cot": lambda a: 1 / math.tan(a)
            }

            if operator not in operations:
                raise CalculatorError(f"Invalid trigonometric operator: {operator}")

            return operations[operator](angle_radians)

        except (ValueError, ZeroDivisionError) as e:
            raise CalculatorError(f"Trigonometric calculation error: {str(e)}")

    @staticmethod
    def perform_logarithm(number: float, base: float) -> float:
        """
        Calculate logarithm with specified base.

        Args:
            number: Number to calculate log of
            base: Logarithm base

        Returns:
            Logarithm result

        Raises:
            CalculatorError: If inputs are invalid
        """
        try:
            if number <= 0:
                raise CalculatorError("Logarithm requires positive number")
            if base <= 0 or base == 1:
                raise CalculatorError("Logarithm base must be positive and not equal to 1")
            return math.log(number, base)
        except (ValueError, ZeroDivisionError) as e:
            raise CalculatorError(f"Logarithm calculation error: {str(e)}")

    @staticmethod
    def perform_power(base: float, exponent: float) -> float:
        """
        Calculate base raised to exponent.

        Args:
            base: Base number
            exponent: Exponent

        Returns:
            Result of base^exponent

        Raises:
            CalculatorError: If calculation error occurs
        """
        try:
            return base ** exponent
        except (ValueError, OverflowError) as e:
            raise CalculatorError(f"Power calculation error: {str(e)}")

    @staticmethod
    def perform_modulo(num1: float, num2: float) -> float:
        """
        Calculate modulo operation.

        Args:
            num1: Dividend
            num2: Divisor

        Returns:
            Remainder of num1 / num2

        Raises:
            CalculatorError: If divisor is zero
        """
        if num2 == 0:
            raise CalculatorError("Modulo by zero")
        return num1 % num2

    @staticmethod
    def get_pi() -> float:
        """
        Get the value of Pi.

        Returns:
            Value of Pi
        """
        return math.pi