#!/bin/sh

set -e  # crash the exec immediately if error encountered

python manage.py wait_for_db
# collect all static files and put them in configured static folder
python manage.py collectstatic --noinput
python manage.py migrate

# run uwsgi service
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
