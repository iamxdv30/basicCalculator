# Quick Start Guide

The **fastest** way to get your calculator running!

## For Complete Beginners

### Windows Users

1. **Double-click** `start.bat`
2. Wait for installation to complete
3. Browser will show the calculator at `http://localhost:5000`
4. Press `CTRL+C` in the terminal window to stop

**That's it!** The script does everything automatically.

---

### Mac/Linux Users

1. Open Terminal in the project folder
2. Make the script executable:
   ```bash
   chmod +x start.sh
   ```
3. Run the script:
   ```bash
   ./start.sh
   ```
4. Open browser to `http://localhost:5000`
5. Press `CTRL+C` in terminal to stop

---

## What the Script Does

The `start.sh` / `start.bat` script automatically:

✅ Checks if Python is installed
✅ Creates a virtual environment
✅ Installs all dependencies
✅ Runs tests to verify everything works
✅ Starts the web server
✅ Shows you the URL to open

## Using Docker Instead

If you prefer Docker (recommended for production):

```bash
docker-compose up --build
```

Then open: `http://localhost:5000`

Stop with: `CTRL+C` then `docker-compose down`

---

## Need More Details?

See **DEPLOYMENT_GUIDE.md** for:
- Step-by-step explanations
- Production deployment
- Cloud hosting options
- Troubleshooting

## First Time Setup

**Install Python first:**
- Windows: [python.org/downloads](https://www.python.org/downloads/)
- Mac: `brew install python` (needs Homebrew)
- Linux: `sudo apt install python3 python3-venv`

**For Docker:**
- All platforms: [docker.com/get-started](https://www.docker.com/get-started)

---

## Using the Calculator

1. **Basic Mode:** Standard calculator operations
2. **Scientific Mode:** Click "Scientific" for advanced functions
3. **History:** Click "History" to see past calculations
4. **Keyboard:** Works with keyboard shortcuts too!

---

**Having issues?** Check DEPLOYMENT_GUIDE.md → Troubleshooting section
