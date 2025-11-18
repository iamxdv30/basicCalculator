# Scientific Calculator Web Application

A modern, professional web-based scientific calculator built with Flask, featuring a beautiful responsive UI and comprehensive mathematical operations.

![Calculator](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Tests](https://img.shields.io/badge/Tests-41%20Passed-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## Features

### Basic Operations
- **Addition** (+)
- **Subtraction** (-)
- **Multiplication** (×)
- **Division** (÷)

### Scientific Operations
- **Trigonometric Functions**: sin, cos, tan, cot (with degree input)
- **Logarithm**: Custom base logarithm
- **Power**: Exponentiation (x^y)
- **Modulo**: Remainder operation
- **Pi Constant**: Built-in π value

### UI Features
- Modern, responsive design with glass morphism effects
- Mobile-friendly interface
- Dual mode: Basic & Scientific calculator
- Calculation history with localStorage
- Keyboard support
- Smooth animations and transitions
- Professional icons from Font Awesome

## Architecture

This application follows **industry best practices** and **clean code principles**:

### Backend (Python/Flask)
```
basicCalculator/
├── app/
│   ├── __init__.py           # Application factory
│   ├── routes.py             # REST API endpoints
│   ├── calculator_service.py # Business logic layer
│   ├── static/               # Static assets (CSS, JS, images)
│   └── templates/            # HTML templates
├── Operators/
│   ├── __init__.py
│   └── Operator.py           # Calculator operations with error handling
├── tests/                    # Comprehensive test suite
│   ├── test_operator.py      # Unit tests
│   └── test_api.py           # Integration tests
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
├── Dockerfile                # Multi-stage Docker build
└── docker-compose.yml        # Docker orchestration
```

### Design Patterns Used
- **Application Factory Pattern** (Flask)
- **Service Layer Pattern** (Business logic separation)
- **Blueprint Pattern** (Route organization)
- **Single Responsibility Principle** (SOLID)
- **Custom Exception Handling**

### Code Quality
- Type hints throughout codebase
- Comprehensive docstrings
- PEP 8 compliant
- 41 unit and integration tests
- Error handling and input validation
- Security best practices (non-root Docker user, CORS, XSS prevention)

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Docker and Docker Compose (for containerized deployment)
- pip (Python package manager)

### Local Development

#### 1. Clone the repository
```bash
cd basicCalculator
```

#### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run tests
```bash
pytest tests/ -v
```

#### 5. Run the application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

### Development Mode with Auto-Reload
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python main.py
```

## Docker Deployment (Recommended)

### Quick Start with Docker Compose

#### 1. Build and run
```bash
docker-compose up --build
```

#### 2. Access the application
Open your browser and navigate to `http://localhost:5000`

#### 3. Stop the application
```bash
docker-compose down
```

### Manual Docker Build

#### Build the image
```bash
docker build -t scientific-calculator:latest .
```

#### Run the container
```bash
docker run -d \
  --name scientific-calculator \
  -p 5000:5000 \
  --restart unless-stopped \
  scientific-calculator:latest
```

#### View logs
```bash
docker logs -f scientific-calculator
```

#### Stop and remove container
```bash
docker stop scientific-calculator
docker rm scientific-calculator
```

### Docker Best Practices Implemented
- Multi-stage build for smaller image size
- Non-root user for security
- Health checks included
- Layer caching optimization
- `.dockerignore` for efficient builds
- Resource limits configured
- Production-ready with Gunicorn

## API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Health Check
```http
GET /api/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "Calculator API",
  "version": "1.0.0"
}
```

#### Calculate Operation
```http
POST /api/calculate
Content-Type: application/json
```

**Basic Operations (+, -, *, /)**
```json
{
  "operation": "+",
  "num1": 10,
  "num2": 5
}
```

**Trigonometric Operations (sin, cos, tan, cot)**
```json
{
  "operation": "sin",
  "num1": 2,
  "angle": 30
}
```

**Logarithm**
```json
{
  "operation": "log",
  "number": 100,
  "base": 10
}
```

**Power**
```json
{
  "operation": "power",
  "base": 2,
  "exponent": 8
}
```

**Modulo**
```json
{
  "operation": "mod",
  "num1": 10,
  "num2": 3
}
```

**Pi Constant**
```json
{
  "operation": "pi"
}
```

**Success Response:**
```json
{
  "success": true,
  "result": 15,
  "operation": "10 + 5"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Division by zero"
}
```

## Testing

### Run all tests
```bash
pytest tests/ -v
```

### Run with coverage
```bash
pytest tests/ --cov=. --cov-report=html
```

### Test categories
- **Unit Tests** (`test_operator.py`): Test all mathematical operations
- **Integration Tests** (`test_api.py`): Test API endpoints and error handling

## Production Deployment

### Environment Variables
```bash
export FLASK_ENV=production
export PORT=5000
```

### Using Gunicorn (Production Server)
```bash
gunicorn --bind 0.0.0.0:5000 \
         --workers 4 \
         --threads 2 \
         --timeout 60 \
         --access-logfile - \
         --error-logfile - \
         main:app
```

## Security Features

- **Non-root Docker user**: Application runs as non-privileged user
- **CORS enabled**: Cross-origin resource sharing configured
- **Input validation**: All inputs validated and sanitized
- **Error handling**: Comprehensive error handling prevents information leakage
- **XSS prevention**: HTML escaping in JavaScript
- **Type checking**: Type hints for code safety

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Keyboard Shortcuts

- **Numbers (0-9)**: Insert number
- **Operators (+, -, *, /)**: Set operation
- **Enter/=**: Calculate result
- **Backspace**: Delete last digit
- **Escape/C**: Clear display

## Troubleshooting

### Port already in use
```bash
# Find process using port 5000
lsof -i :5000  # On macOS/Linux
netstat -ano | findstr :5000  # On Windows

# Kill the process or use a different port
export PORT=8000
```

### Docker build issues
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

## License

This project is licensed under the MIT License.

---

**Built with Flask, Python, and Modern Web Technologies**
