#!/bin/sh

sleep 2
python manage.py migrate
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --noinput \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py collectstatic --noinput

echo "Connecting Celery..."
celery -A _settings worker -l INFO &
celery -A _settings beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &
echo "Celery connected!"

gunicorn _settings.wsgi:application --bind 0.0.0.0:8000


exec "$@"
