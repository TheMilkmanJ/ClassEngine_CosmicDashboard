# Use a lightweight Python base image
FROM python:3.10-slim

# Prevent python from buffering stdout/stderr (keeps terminal logs real-time)
ENV PYTHONUNBUFFERED=1

# Install system dependencies (C/C++ compilers, Fortran, MPI)
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    openmpi-bin \
    libopenmpi-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-install PolyChord via Cobaya so it's baked into the image
RUN cobaya-install polychord -p /root/cobaya_packages_clean

# Copy the entire project into the container
COPY . .

# Expose the dashboard port and run the server
EXPOSE 8000
CMD ["python3", "scripts/cosmo_dashboard_backend.py"]