"""
Main application entry point.
Runs the Flask web application server.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run Flask development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )