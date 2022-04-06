from os import environ

import click
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

"""
CLI commmands region.
May be a better place to put this.
"""


@flask_app.cli.command("create-users")
def create_users():
    """Create users"""
    from app.extensions import db
    from app.user.domain.user_roles import UserRoles
    from app.user.repository.user import User

    users = [
        User(
            id=None,
            name="Admin",
            username="admin",
            email="admin@mail.com",
            password="admin",
            role=UserRoles.ADMIN,
        ),
        User(
            id=None,
            name="John Doe",
            username="johndoe",
            email="johndoe@mail.com",
            password="john",
            role=UserRoles.USER,
        ),
    ]

    for u in users:
        existing_user = User.query.filter(User.username == u.username).first()
        if not existing_user:
            click.echo(f"Creating user '{u.username}'")
            db.session.add(u)

    db.session.commit()
    click.echo(f"Created user")


# Put in here due to circular dependency if done at factory
init_documentation_spec(flask_app)

if DEBUG:
    flask_app.logger.info(f"DEBUG          = {DEBUG}")
    flask_app.logger.info(f"Environment    = {config_mode}")

if __name__ == "__main__":
    flask_app.run(port=flask_app.config["PORT"])
