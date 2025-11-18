"""
API Routes
Defines REST API endpoints for calculator operations.
"""
from flask import Blueprint, request, jsonify, render_template
from app.calculator_service import CalculatorService
from Operators.Operator import CalculatorError

calculator_bp = Blueprint('calculator', __name__)


@calculator_bp.route('/')
def index():
    """Render the calculator web interface."""
    return render_template('index.html')


@calculator_bp.route('/api/calculate', methods=['POST'])
def calculate():
    """
    Main calculator API endpoint.

    Expects JSON body with:
    {
        "operation": str,  # Operation type (+, -, *, /, sin, cos, tan, cot, log, power, mod, pi)
        "num1": float,     # First number (optional for some operations)
        "num2": float,     # Second number (for basic operations)
        "angle": float,    # Angle for trigonometric operations
        "number": float,   # Number for logarithm
        "base": float,     # Base for logarithm or power
        "exponent": float  # Exponent for power operation
    }

    Returns:
        JSON response with result or error
    """
    try:
        # Get JSON data with silent=True to handle malformed JSON
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400

        operation = data.get('operation')
        if not operation:
            return jsonify({
                'success': False,
                'error': 'Operation not specified'
            }), 400

        result = CalculatorService.calculate(operation, data)
        return jsonify(result), 200

    except CalculatorError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

    except ValueError as e:
        return jsonify({
            'success': False,
            'error': f'Invalid input: {str(e)}'
        }), 400

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500


@calculator_bp.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring.

    Returns:
        JSON response indicating service health
    """
    return jsonify({
        'status': 'healthy',
        'service': 'Calculator API',
        'version': '1.0.0'
    }), 200
