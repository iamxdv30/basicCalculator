@echo off
REM Quick start script for Windows

echo.
echo ================================================
echo   Scientific Calculator - Quick Start Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.11 or higher from python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Show Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt
echo Dependencies installed!

REM Run tests
echo.
echo Running tests...
python -m pytest tests/ -q
if errorlevel 1 (
    echo WARNING: Some tests failed, but continuing anyway...
) else (
    echo All tests passed!
)

REM Start the application
echo.
echo ================================================
echo   Starting the calculator application...
echo ================================================
echo.
echo   Calculator will open at:
echo   http://localhost:5000
echo.
echo   Press CTRL+C to stop the server
echo ================================================
echo.

python main.py

pause
