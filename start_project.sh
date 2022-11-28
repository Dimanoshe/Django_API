#!/bin/bash


echo 'Run Django server...'

echo 'Make migrations...'
python3 manage.py makemigrations &&
python3 manage.py migrate &&
echo 'Run server!'
python3 manage.py runserver

