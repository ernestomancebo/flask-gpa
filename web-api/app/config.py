"""
Custom settings for the application
---
It's expected that the environment was loaded previously
"""

from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    environ.get("POSTGRES_USER"),
    environ.get("POSTGRES_PASSWORD"),
    environ.get("POSTGRES_HOSTNAME"),
    environ.get("POSTGRES_PORT"),
    environ.get("APPLICATION_DB"),
)
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
