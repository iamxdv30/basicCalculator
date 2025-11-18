"""
Flask Application Factory
Initializes and configures the Flask application following best practices.
"""
from flask import Flask
from flask_cors import CORS


def create_app():
    """
    Application factory pattern for creating Flask app instance.

    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['JSON_SORT_KEYS'] = False

    # Enable CORS for all routes
    CORS(app)

    # Register blueprints
    from app.routes import calculator_bp
    app.register_blueprint(calculator_bp)

    return app
