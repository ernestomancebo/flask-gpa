from os import environ

from flask import Flask, jsonify

from app.app import create_app
from app.doc.blueprint import API_URL
from app.doc.spec import spec


def init_documentation_spec(app: Flask):
    """Adds OpenAPI v3 documentation"""

    # inits documentations/specs
    with app.test_request_context():
        for fn_name in app.view_functions:
            if fn_name == "static":
                continue

            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)

        # Includes Swagger endpoint
        @app.route(API_URL)
        def create_swagger_spec():
            return jsonify(spec.to_dict())


config_mode = environ.get("ENV", "Development").capitalize()
DEBUG = config_mode == "Development"

flask_app = create_app()

# Put in here due to circular dependency if done at factory
init_documentation_spec(flask_app)

if DEBUG:
    flask_app.logger.info(f"DEBUG          = {DEBUG}")
    flask_app.logger.info(f"Environment    = {config_mode}")

if __name__ == "__main__":
    flask_app.run(port=flask_app.config["PORT"])
