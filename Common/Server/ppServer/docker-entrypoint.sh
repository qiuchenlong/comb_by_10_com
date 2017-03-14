/code/manage.py
/usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000
