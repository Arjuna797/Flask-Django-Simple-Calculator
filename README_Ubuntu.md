# Flask-Django-Simple-Calculator - Ubuntu Migration Guide

This guide provides step-by-step instructions to migrate and run the Flask-Django-Simple-Calculator project on an Ubuntu Virtual Machine (VM) using VirtualBox, without relying on Docker.

## Prerequisites

- Ubuntu installed on VirtualBox VM (recommended version: 20.04 LTS or later)
- Internet connection for downloading dependencies
- Basic knowledge of Linux commands

## Step 1: Update Ubuntu System

First, update your Ubuntu system to ensure you have the latest packages:

```bash
sudo apt update && sudo apt upgrade -y
```

## Step 2: Install Python 3

Python 3 is usually pre-installed on Ubuntu, but ensure you have it:

```bash
python3 --version
```

If not installed:

```bash
sudo apt install python3 -y
```

## Step 3: Install pip for Python 3

Install pip, the Python package installer:

```bash
sudo apt install python3-pip -y
```

Verify installation:

```bash
pip3 --version
```

## Step 4: Install virtualenv

Install virtualenv to create isolated Python environments:

```bash
sudo apt install python3-venv -y
```

## Step 5: Clone or Transfer Project Files

Transfer the project files from your Windows machine to the Ubuntu VM. You can use:

- USB drive
- Shared folders in VirtualBox
- Git (if the project is in a repository)

Navigate to the project directory:

```bash
cd /path/to/your/project/Flask-Django-Simple-Calculator-main
```

## Step 6: Create Virtual Environment

Create a virtual environment for the project:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Your prompt should now show `(venv)` at the beginning.

## Step 7: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask==3.0.3
- Django==5.1.2

## Step 8: Run the Applications

### Option 1: Run Flask App

```bash
python app_flask.py
```

The Flask app will run on `http://localhost:8080`

### Option 2: Run Django App

```bash
python app_django.py
```

The Django app will run on `http://localhost:8081`

### Running Both Simultaneously

Since both apps serve the same frontend, you can run them in separate terminals:

1. Open two terminals
2. In terminal 1: `source venv/bin/activate && python app_flask.py`
3. In terminal 2: `source venv/bin/activate && python app_django.py`

## Step 9: Access the Applications

- Flask Calculator: Open your browser and go to `http://localhost:8080`
- Django Calculator: Open your browser and go to `http://localhost:8081`

## Step 10: Deactivate Virtual Environment (When Done)

When you're finished working on the project:

```bash
deactivate
```

## Troubleshooting

- If you encounter permission issues, use `sudo` for system installations
- Ensure the virtual environment is activated before running Python commands
- Check firewall settings if you can't access the apps from outside the VM
- If ports 8080 or 8081 are in use, modify the port numbers in `app_flask.py` and `app_django.py`

## Project Structure

- `app_flask.py`: Flask application entry point
- `app_django.py`: Django application entry point
- `templates/index.html`: HTML template for the calculator
- `static/`: CSS and JavaScript files
- `requirements.txt`: Python dependencies

## Notes

- This setup runs the applications in development mode
- For production deployment, additional configuration would be needed
- The project demonstrates how Flask and Django can serve the same frontend
