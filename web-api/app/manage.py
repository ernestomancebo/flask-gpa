# encoding: utf-8

import click

# from flask.cli import with_appcontext


@click.group()
def cli():
    """Main entrypoint"""
    pass


# @with_appcontext
@cli.command("create-db")
def init_db():
    """Create tables if don't exist"""
    from app.extensions import db

    click.echo("Creating tables if don't exists")
    db.create_all()


# @with_appcontext
@cli.command("init")
def init():
    """Create users"""
    from app.extensions import db
    from app.user.domain.user_roles import UserRoles
    from app.user.repository.user import User

    users = [
        User(
            id=None,
            username="admin",
            email="admin@mail.com",
            password="admin",
            role=UserRoles.ADMIN,
        ),
        User(
            id=None,
            username="johndoe",
            email="johndoe@mail.com",
            password="john",
            role=UserRoles.USER,
        ),
    ]

    for u in users:
        existing_user = User.query.filer(User.username == u.username).first()
        if not existing_user:
            click.echo(f"Creating user '{u.username}'")
            db.session.add(u)

    db.session.commit()
    click.echo(f"Created user")


if __name__ == "__main__":
    cli()
