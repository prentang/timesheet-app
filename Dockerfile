# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into container
COPY . .

# Run script
CMD ["python", "app.py"]
