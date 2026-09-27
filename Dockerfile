FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST
COPY requirements.txt .

# Install dependencies ONCE
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code AFTER
COPY . .

EXPOSE 8000

CMD ["uvicorn","app.api.main:app","--host","0.0.0.0","--port","8000"]