# Use Python 3.10 slim image for smaller size
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (remove AWS CLI, add Azure CLI if needed)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements-docker.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-docker.txt

# Copy application code
COPY . .

# Install the package in editable mode
RUN pip install -e .

# Expose port for Azure Container Instances
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]