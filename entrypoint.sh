python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000