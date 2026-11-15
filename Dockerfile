FROM python:3.12-slim

# Prevent Python from generating cache files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required by OpenCV and ONNX Runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the complete project, including the ONNX model
COPY . .

# Create input and output directories
RUN mkdir -p /app/files /app/output

# Default input and output directories
VOLUME ["/app/files", "/app/output"]

# Run the application
ENTRYPOINT ["python", "main.py"]

CMD []
