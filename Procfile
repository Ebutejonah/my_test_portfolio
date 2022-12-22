web: gunicorn mysite.wsgi:application --log-file - --log-level debug
python: manage.py migrate
python: manage.py collectstatic --noinput