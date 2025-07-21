# Use a slim, secure base image
FROM python:3.11-slim@sha256:139020233cc412efe4c8135b0efe1c7569dc8b28ddd88bddb109b764f8977e30

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

# Copy app code requirements
COPY ./app /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set permissions and switch to non-root
RUN chown -R appuser:appgroup /app
USER appuser

# Default command (override in docker-compose or CLI)
CMD ["pytest", "tests"]