# Complete Deployment Guide - Scientific Calculator Web App

This guide will walk you through **every step** needed to run and deploy your calculator application, from testing locally to deploying in production.

---

## Table of Contents
1. [Running Locally (Testing)](#1-running-locally-testing)
2. [Docker Deployment (Local)](#2-docker-deployment-local)
3. [Production Deployment](#3-production-deployment)
4. [Troubleshooting](#4-troubleshooting)

---

## 1. Running Locally (Testing)

This is the **easiest way** to test your application on your own computer.

### Prerequisites

Before you start, you need these tools installed:

#### Check if you have Python
Open your terminal (Mac/Linux) or Command Prompt (Windows) and type:
```bash
python --version
```
or
```bash
python3 --version
```

**Expected output:** `Python 3.11.x` or higher

**If you don't have Python:**
- **Windows:** Download from [python.org](https://www.python.org/downloads/)
  - ✅ Check "Add Python to PATH" during installation
- **Mac:** `brew install python@3.11` (requires Homebrew)
- **Linux:** `sudo apt install python3.11 python3.11-venv`

---

### Step 1: Navigate to Your Project

Open your terminal and go to your project folder:

```bash
cd /path/to/basicCalculator
```

**Example:**
- Windows: `cd C:\Users\YourName\basicCalculator`
- Mac/Linux: `cd ~/basicCalculator`

**What this does:** Changes your current directory to where your project files are located.

---

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project's dependencies separate from other Python projects.

**Create the virtual environment:**
```bash
python -m venv venv
```

**What this does:** Creates a folder called `venv` containing an isolated Python environment.

**Activate the virtual environment:**

- **Windows (Command Prompt):**
  ```bash
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**
  ```bash
  venv\Scripts\Activate.ps1
  ```

  *If you get an error, run this first:*
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

**How to know it worked:** Your terminal prompt should now start with `(venv)`, like this:
```
(venv) C:\Users\YourName\basicCalculator>
```

---

### Step 3: Install Dependencies

Install all the Python packages your app needs:

```bash
pip install -r requirements.txt
```

**What this does:** Reads `requirements.txt` and installs:
- Flask (web framework)
- flask-cors (allows browser access)
- gunicorn (production server)
- pytest (for running tests)
- And other dependencies

**Expected output:** You'll see packages being downloaded and installed. This takes 1-2 minutes.

---

### Step 4: Run the Application

Start the Flask development server:

```bash
python main.py
```

**What this does:** Starts a web server on your computer that serves the calculator application.

**Expected output:**
```
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

**🎉 Success!** Your app is now running!

---

### Step 5: Open in Your Browser

Open your web browser (Chrome, Firefox, Safari, Edge) and go to:

```
http://localhost:5000
```

or

```
http://127.0.0.1:5000
```

**What you should see:** A beautiful calculator interface with purple/pink gradients.

---

### Step 6: Test the Calculator

Try these operations to verify everything works:

1. **Basic math:** Click `5`, `+`, `3`, `=` → Should show `8`
2. **Scientific mode:** Click the "Scientific" button
3. **Sine function:** Type `30`, click `sin` → Should show `0.5`
4. **History:** Click "History" to see your calculations

---

### Step 7: Stop the Server

When you're done testing:

1. Go back to your terminal
2. Press `CTRL + C` (Windows/Mac/Linux)
3. Deactivate the virtual environment: `deactivate`

---

## 2. Docker Deployment (Local)

Docker packages your entire application into a container that runs the same way on any computer.

### Prerequisites

#### Install Docker

**Windows/Mac:**
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Install and start Docker Desktop
3. Verify installation:
   ```bash
   docker --version
   docker-compose --version
   ```

**Linux:**
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Log out and back in

# Install docker-compose
sudo apt install docker-compose
```

**Expected output:**
```
Docker version 24.x.x
docker-compose version 1.29.x
```

---

### Step 1: Navigate to Project Directory

```bash
cd /path/to/basicCalculator
```

---

### Step 2: Build and Run with Docker Compose

**One command to do everything:**

```bash
docker-compose up --build
```

**What this does (step by step):**

1. **Reads `Dockerfile`** - Instructions for creating a Docker image
2. **Downloads base image** - Gets Python 3.11 slim image
3. **Installs dependencies** - Installs packages from `requirements.txt`
4. **Copies your code** - Puts your app files into the container
5. **Creates container** - Builds a runnable container
6. **Starts the server** - Runs Gunicorn with 4 workers
7. **Maps port 5000** - Makes it accessible at `http://localhost:5000`

**Expected output:**
```
Building calculator
Step 1/15 : FROM python:3.11-slim AS builder
...
Creating scientific-calculator ... done
Attaching to scientific-calculator
scientific-calculator | [2025-11-18 12:00:00] [1] [INFO] Starting gunicorn 21.2.0
scientific-calculator | [2025-11-18 12:00:00] [1] [INFO] Listening at: http://0.0.0.0:5000
```

**⏱️ First build takes 3-5 minutes.** Subsequent builds are faster due to caching.

---

### Step 3: Access the Application

Open your browser:
```
http://localhost:5000
```

**🎉 Your containerized app is running!**

---

### Step 4: View Logs

Open a new terminal and run:

```bash
docker logs -f scientific-calculator
```

**What this does:** Shows real-time logs from your container. Press `CTRL + C` to stop viewing.

---

### Step 5: Stop the Application

**Option A - Graceful shutdown:**
```bash
docker-compose down
```
**What this does:** Stops and removes containers, keeping the image for faster restart.

**Option B - Quick stop (keeps containers):**
```bash
docker-compose stop
```

**Option C - Complete cleanup:**
```bash
docker-compose down --volumes --rmi all
```
**What this does:** Removes everything (containers, images, volumes). Use this to start completely fresh.

---

### Step 6: Restart Quickly

After stopping, restart instantly:

```bash
docker-compose up
```

**Note:** No `--build` needed since the image already exists.

---

## 3. Production Deployment

Deploy your calculator to the internet so anyone can access it!

### Option A: Deploy to Render (Free & Easy)

**Render** is a cloud platform with a free tier perfect for learning.

#### Step 1: Push to GitHub

```bash
# If not already initialized
git init
git add .
git commit -m "Initial commit"

# Create a repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

#### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (click "Sign Up" → "GitHub")

#### Step 3: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name:** `scientific-calculator`
   - **Environment:** `Docker`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Plan:** `Free`

4. Click **"Create Web Service"**

#### Step 4: Wait for Deployment

**What happens:**
1. Render clones your repo
2. Builds Docker image (5-10 minutes first time)
3. Starts the container
4. Assigns a URL like: `https://scientific-calculator.onrender.com`

**Status indicators:**
- 🟡 **Building** - Wait...
- 🟢 **Live** - Ready! Click the URL to open

#### Step 5: Access Your Live App

Click the URL Render provides, or find it under:
- Dashboard → Your service → URL at the top

**🎉 Your calculator is now live on the internet!**

---

### Option B: Deploy to Railway (Alternative Free Option)

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway auto-detects Docker and deploys

**Deployment takes:** 5-10 minutes

**Your URL:** `https://YOUR_APP.up.railway.app`

---

### Option C: Deploy to DigitalOcean (Professional)

**Cost:** ~$6/month for a basic droplet

#### Step 1: Create Droplet

1. Go to [digitalocean.com](https://www.digitalocean.com)
2. Create account → Create Droplet
3. Choose:
   - **Image:** Ubuntu 22.04 LTS
   - **Plan:** Basic ($6/month)
   - **Region:** Closest to you
   - **Authentication:** SSH key (recommended) or Password

4. Click **"Create Droplet"**

#### Step 2: Connect to Your Server

```bash
ssh root@YOUR_DROPLET_IP
```

**Example:** `ssh root@143.198.100.50`

#### Step 3: Install Docker on Server

```bash
# Update system
apt update && apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
apt install docker-compose -y

# Verify
docker --version
docker-compose --version
```

#### Step 4: Clone Your Repository

```bash
# Install git if needed
apt install git -y

# Clone your repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

#### Step 5: Run with Docker Compose

```bash
docker-compose up -d --build
```

**The `-d` flag means:** Run in background (detached mode)

#### Step 6: Configure Firewall

```bash
# Allow port 5000
ufw allow 5000/tcp

# Enable firewall (if not already)
ufw enable
```

#### Step 7: Access Your App

Open browser:
```
http://YOUR_DROPLET_IP:5000
```

**Example:** `http://143.198.100.50:5000`

---

### Option D: Deploy with Custom Domain (Professional Setup)

**After deploying to DigitalOcean:**

#### Step 1: Install Nginx (Reverse Proxy)

```bash
apt install nginx -y
```

**What Nginx does:** Acts as a middleman, forwarding requests from port 80 (HTTP) to your app on port 5000.

#### Step 2: Configure Nginx

```bash
nano /etc/nginx/sites-available/calculator
```

**Paste this configuration:**

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Save:** Press `CTRL + X`, then `Y`, then `ENTER`

#### Step 3: Enable Site

```bash
ln -s /etc/nginx/sites-available/calculator /etc/nginx/sites-enabled/
nginx -t  # Test configuration
systemctl restart nginx
```

#### Step 4: Configure Domain DNS

In your domain registrar (GoDaddy, Namecheap, etc.):

1. Go to DNS settings
2. Add **A Record:**
   - **Host:** `@` (or blank)
   - **Value:** Your droplet IP
   - **TTL:** 3600

3. Add **A Record** for www:
   - **Host:** `www`
   - **Value:** Your droplet IP
   - **TTL:** 3600

**Wait:** DNS propagation takes 5 minutes to 48 hours (usually ~30 minutes)

#### Step 5: Add HTTPS with Let's Encrypt (Free SSL)

```bash
# Install Certbot
apt install certbot python3-certbot-nginx -y

# Get SSL certificate
certbot --nginx -d your-domain.com -d www.your-domain.com

# Follow prompts:
# - Enter email
# - Agree to terms
# - Choose redirect HTTP to HTTPS (option 2)
```

**🎉 Your calculator now has HTTPS!**

Access at: `https://your-domain.com`

---

## 4. Troubleshooting

### Problem: "Port 5000 already in use"

**Solution 1 - Find and kill the process:**

**Mac/Linux:**
```bash
lsof -i :5000
kill -9 PID_NUMBER
```

**Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID PID_NUMBER /F
```

**Solution 2 - Use a different port:**

Edit `docker-compose.yml`:
```yaml
ports:
  - "8000:5000"  # Change 5000 to 8000
```

Then access at: `http://localhost:8000`

---

### Problem: Docker build fails with "permission denied"

**Linux:**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**Windows:**
- Start Docker Desktop as Administrator

---

### Problem: "Module not found" errors when running locally

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problem: Tests fail

**Solution:**
```bash
# Run tests with verbose output
pytest tests/ -v

# Check specific failing test
pytest tests/test_api.py::TestHealthEndpoint::test_health_check -v
```

---

### Problem: Can't access from other devices on network

**When running locally:**

1. Find your local IP:
   ```bash
   # Mac/Linux
   ifconfig | grep inet

   # Windows
   ipconfig
   ```

2. Run Flask with:
   ```bash
   python main.py
   ```

3. Access from other devices:
   ```
   http://YOUR_LOCAL_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

---

### Problem: Docker image is too large

**Solution - Clean up unused images:**

```bash
docker system prune -a
docker-compose build --no-cache
```

---

## Quick Reference Commands

### Local Development
```bash
# Start
python main.py

# Run tests
pytest tests/ -v

# Stop
CTRL + C
```

### Docker
```bash
# Start (build first time)
docker-compose up --build

# Start (subsequent times)
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker logs -f scientific-calculator

# Stop
docker-compose down

# Rebuild
docker-compose build --no-cache
```

### Production (DigitalOcean/VPS)
```bash
# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Restart
docker-compose restart

# Update code
git pull
docker-compose up -d --build

# Check Nginx
systemctl status nginx
nginx -t
```

---

## Next Steps

After deployment:

1. **Monitor your app:**
   - Check logs regularly: `docker logs -f scientific-calculator`
   - Set up uptime monitoring (e.g., UptimeRobot)

2. **Improve security:**
   - Change secret key in `app/__init__.py`
   - Set up HTTPS (Let's Encrypt)
   - Enable firewall rules

3. **Performance optimization:**
   - Increase Gunicorn workers for high traffic
   - Add Redis caching
   - Use CDN for static files

4. **CI/CD (Advanced):**
   - Set up GitHub Actions for auto-deployment
   - Add automated testing before deployment

---

## Need Help?

- **Check logs:** First step in debugging
- **Read error messages:** They usually tell you what's wrong
- **Google the error:** Someone has likely solved it before
- **Stack Overflow:** Great community for specific issues

**Common resources:**
- Flask docs: https://flask.palletsprojects.com/
- Docker docs: https://docs.docker.com/
- Render docs: https://render.com/docs

---

**Congratulations!** You now know how to deploy a professional web application! 🎉
