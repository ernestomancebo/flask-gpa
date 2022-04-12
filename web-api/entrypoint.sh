#!/usr/bin/env bash

cd /app/web-api/app

# Create tables
flask create-tables

# Apply Migrations
flask db upgrade

# Init users
flask create-users

# Moves a level up, so can recognize wsgi as part of the module
cd ..

gunicorn --config app/gunicorn-cfg.py app.wsgi:flask_app