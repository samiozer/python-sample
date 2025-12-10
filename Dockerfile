# Stage 1: Builder
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .

# Compile app.py to C extension
RUN python build.py build_ext --inplace

# Remove source files to ensure we only have compiled code
RUN rm app.py build.py app.c

# Stage 2: Runner
FROM python:3.9-slim as runner

WORKDIR /app

# Create a non-root user
RUN useradd -m appuser

# Copy installed packages from builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copy only the necessary compiled files and other assets
# We copy everything remaining in /app from builder, which should rely on the cleanup done there
COPY --from=builder --chown=appuser:appuser /app /app

# Make sure scripts in .local are usable:
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONPATH=/home/appuser/.local/lib/python3.9/site-packages

# Switch to non-root user
USER appuser

EXPOSE 8000

# Run app.py using Uvicorn with WSGI interface
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--interface", "wsgi", "--workers", "4"]
