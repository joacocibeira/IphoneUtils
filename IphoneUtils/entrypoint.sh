#!/bin/ash

echo "Apply database migrations"

python3 manage.py migrate --no-input 
python3 manage.py collectstatic --no-input

guinicorn IphoneUtils.wsgi:application --bind 0.0.0.0:8000

exec "$@"