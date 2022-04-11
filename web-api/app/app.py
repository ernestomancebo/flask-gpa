from os import environ, path

from dotenv import load_dotenv
from flask import Flask
# from flask_cors import CORS

from app.doc.blueprint import SWAGGER_URL
from app.doc.blueprint import blueprint as swagger_ui_blueprint
from app.extensions import db, migrate
from app.views import blueprint as views_blueprint


def create_app():
    """
    Web API Application factory
    """
    config_mode = environ.get("ENV", "Development").capitalize()
    basedir = path.abspath(path.dirname(__file__))

    if config_mode == "Development":
        # Some stuffs are required for testing
        load_dotenv(path.join(basedir, ".testenv"))
    elif config_mode == "Production":
        # Replace environment variables with
        # production variables
        load_dotenv(path.join(basedir, ".env"))
    load_dotenv(path.join(basedir, ".flaskenv"))

    app = Flask("api_service")
    # CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_pyfile(path.join(basedir, "config.py"))

    app.logger.info(f"Configuration    = {app.config}")

    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_extensions(app: Flask):
    """
    Inits the application extensions; i.e. SQL Alchemy.
    """
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask):
    """
    Register the Flask app blueprints.
    """
    app.register_blueprint(views_blueprint)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
