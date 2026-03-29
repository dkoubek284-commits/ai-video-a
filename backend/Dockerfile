# Dockerfile

# Use python:3.11-slim as base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create uploads directory
RUN mkdir -p uploads

# Expose port 8001
EXPOSE 8001

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8001/health || exit 1
