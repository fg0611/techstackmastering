# Dockerfile
FROM python:3.8-slim

WORKDIR /app

# Instala las dependencias del sistema necesarias para psycopg2
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends libpq-dev gcc && \
#     rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]