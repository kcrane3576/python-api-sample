# Use a slim, secure base image
FROM python:3.11-slim

# Set non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential gcc curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY . .

# Set permissions and switch to non-root
RUN chown -R appuser:appgroup /app
USER appuser

# Default command (override in docker-compose or CLI)
CMD ["pytest", "tests"]