#!/bin/bash
# Quick start script for Mac/Linux

echo "🧮 Scientific Calculator - Quick Start Script"
echo "=============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3.11 or higher from python.org"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
echo "✓ Dependencies installed"

# Run tests
echo ""
echo "🧪 Running tests..."
python -m pytest tests/ -q
if [ $? -eq 0 ]; then
    echo "✓ All tests passed!"
else
    echo "⚠️  Some tests failed, but continuing anyway..."
fi

# Start the application
echo ""
echo "🚀 Starting the calculator application..."
echo ""
echo "=============================================="
echo "  Calculator will open at:"
echo "  👉 http://localhost:5000"
echo ""
echo "  Press CTRL+C to stop the server"
echo "=============================================="
echo ""

python main.py
