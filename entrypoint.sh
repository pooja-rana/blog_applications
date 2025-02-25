#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to start..."
until python3 << END
import sys
import psycopg2
import time
import os

time.sleep(1)  # Wait 1 second before retrying

try:
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db",  # Matches service name in docker-compose.yml
        port=5432  # Default to 5432 if not set
    )
    conn.close()
except psycopg2.OperationalError:
    sys.exit(1)

sys.exit(0)
END
do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL is up and running!"

# Run migrations
python manage.py migrate --noinput

# Start Django server (without Gunicorn)
exec python manage.py runserver 0.0.0.0:8000
