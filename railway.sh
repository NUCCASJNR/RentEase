gunicorn RentEase.wsgi --log-file -
celery -A RentEase worker -l DEBUG -E -f celery.log
