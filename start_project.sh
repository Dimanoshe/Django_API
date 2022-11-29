#!/bin/bash

echo 'Export MY_API_KEY'
export MY_API_KEY='yhdemX0*n3nr84$59ghIjdgbe#4hfodjnf'

echo 'Run Django server...'

echo 'Make migrations...'
python3 manage.py makemigrations &&
python3 manage.py migrate &&

echo 'Create default Superuser'
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '123')" | python manage.py shell &&
echo 'Superuser is ready'
echo 'Run server!'
python3 manage.py runserver

