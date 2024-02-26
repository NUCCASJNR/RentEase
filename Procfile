web: gunicorn RentEase.wsgi --log-file -
worker: celery -A RentEase worker -l DEBUG -E -f celery.log