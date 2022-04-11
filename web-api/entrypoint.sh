#!/usr/bin/env bash

cd web-api/app

# Apply Migrations
flask db upgrade

# Init users
# python manage.py init
flask create-users

cd ..

gunicorn --config web-api/app/gunicorn-cfg.py app.wsgi:flask_app