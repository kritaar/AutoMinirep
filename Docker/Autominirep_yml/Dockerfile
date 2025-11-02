FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# deps del sistema que suele pedir psycopg y build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# requirements: está en Docker/Autominirep_yml dentro del repo
COPY Docker/Autominirep_yml/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copia TODO el proyecto (ahora sí incluye manage.py, apps, etc.)
COPY . /app

EXPOSE 8000

CMD ["/bin/sh","-lc", "\
python manage.py migrate && \
python manage.py collectstatic --noinput && \
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 \
"]
