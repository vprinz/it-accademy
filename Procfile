release: python manage.py migrate
release: celery -A store worker --loglevel=debug --concurrency=4
web: gunicorn store.wsgi