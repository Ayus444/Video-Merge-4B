FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y ffmpeg gcc python3-dev build-essential && \
    apt-get clean

# Create venv and install dependencies
RUN python3 -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port for gunicorn
EXPOSE 8000

# Run both gunicorn and your bot using the same virtual environment
CMD ["sh", "-c", "venv/bin/gunicorn -b 0.0.0.0:8000 app:app & venv/bin/python3 bot.py"]
