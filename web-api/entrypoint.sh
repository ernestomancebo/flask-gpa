#!/usr/bin/env bash

cd /app/web-api/app

# Create tables
flask create-tables

# Apply Migrations
flask db upgrade

# Init users
# python manage.py init
flask create-users

cd ..

gunicorn --config app/gunicorn-cfg.py app.wsgi:flask_app