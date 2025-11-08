# Use lightweight Python image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run Flask
CMD ["python", "app_flask.py"]
