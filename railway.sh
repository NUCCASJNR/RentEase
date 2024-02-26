gunicorn RentEase.wsgi --log-file - &
celery -A RentEase worker --loglevel=INFO