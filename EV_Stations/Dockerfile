# Use official python alpine image
FROM python:3.10-alpine as web

# Set working directory
WORKDIR /home/app/web

# Install build dependencies needed for mysqlclient and others in one step
RUN apk update && apk add --no-cache \
    mariadb-connector-c-dev \
    build-base \
    python3-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Prevent Python from writing pyc files to container
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Copy requirements first to leverage docker cache if unchanged
COPY ./requirements.txt ./

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install gunicorn \
    && pip install --no-cache-dir -r requirements.txt

# Copy rest of the project files
COPY . .

# Default command (adjust accordingly)
CMD ["gunicorn", "EV_Stations.wsgi:application", "--bind", "0.0.0.0:8000"]
