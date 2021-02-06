web: gunicorn <your_project_name>.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
