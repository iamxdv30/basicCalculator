"""
Calculator Service Layer
Business logic for calculator operations, acts as an interface between routes and operators.
"""
from typing import Dict, Any
from Operators.Operator import Operator, CalculatorError


class CalculatorService:
    """
    Service class that handles calculator operations and validation.
    Implements single responsibility principle by separating business logic from routes.
    """

    @staticmethod
    def calculate(operation: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process calculator operation based on operation type.

        Args:
            operation: Type of operation to perform
            data: Dictionary containing operation parameters

        Returns:
            Dictionary with result or error

        Raises:
            CalculatorError: If calculation fails
        """
        try:
            if operation in ['+', '-', '*', '/']:
                return CalculatorService._handle_basic_operation(operation, data)
            elif operation in ['sin', 'cos', 'tan', 'cot']:
                return CalculatorService._handle_trigonometric_operation(operation, data)
            elif operation == 'log':
                return CalculatorService._handle_logarithm(data)
            elif operation == 'power':
                return CalculatorService._handle_power(data)
            elif operation == 'mod':
                return CalculatorService._handle_modulo(data)
            elif operation == 'pi':
                return CalculatorService._handle_pi()
            else:
                raise CalculatorError(f"Unknown operation: {operation}")

        except CalculatorError as e:
            raise e
        except Exception as e:
            raise CalculatorError(f"Unexpected error: {str(e)}")

    @staticmethod
    def _handle_basic_operation(operator: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle basic arithmetic operations."""
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))

        result = Operator.perform_basic_operation(operator, num1, num2)
        return {
            'success': True,
            'result': result,
            'operation': f"{num1} {operator} {num2}"
        }

    @staticmethod
    def _handle_trigonometric_operation(operator: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle trigonometric operations."""
        num1 = data.get('num1')
        angle = float(data.get('angle', 0))

        # If num1 is provided, multiply result by num1, otherwise just calculate trig function
        if num1 is not None and num1 != '':
            num1 = float(num1)
            result = Operator.perform_trigonometric_operation(operator, num1, angle)
            operation_desc = f"{num1} × {operator}({angle}°)"
        else:
            result = Operator.perform_trigonometric_function(operator, angle)
            operation_desc = f"{operator}({angle}°)"

        return {
            'success': True,
            'result': result,
            'operation': operation_desc
        }

    @staticmethod
    def _handle_logarithm(data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle logarithm operation."""
        number = float(data.get('number', 1))
        base = float(data.get('base', 10))

        result = Operator.perform_logarithm(number, base)
        return {
            'success': True,
            'result': result,
            'operation': f"log_{base}({number})"
        }

    @staticmethod
    def _handle_power(data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle power operation."""
        base = float(data.get('base', 0))
        exponent = float(data.get('exponent', 0))

        result = Operator.perform_power(base, exponent)
        return {
            'success': True,
            'result': result,
            'operation': f"{base}^{exponent}"
        }

    @staticmethod
    def _handle_modulo(data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle modulo operation."""
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 1))

        result = Operator.perform_modulo(num1, num2)
        return {
            'success': True,
            'result': result,
            'operation': f"{num1} mod {num2}"
        }

    @staticmethod
    def _handle_pi() -> Dict[str, Any]:
        """Handle pi constant."""
        result = Operator.get_pi()
        return {
            'success': True,
            'result': result,
            'operation': 'π'
        }
