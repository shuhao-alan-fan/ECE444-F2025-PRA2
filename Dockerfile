# Dockerfile
FROM python:3.11-2

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (can be overridden)
CMD ["python", "hello.py"]