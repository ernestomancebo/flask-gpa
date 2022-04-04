from app.user.repository.user import User
from flask_sqlalchemy import SQLAlchemy


class UserRepository:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def add_user(self, user: User):
        self.db.session.add(user)
        self.db.session.commit()

    def get_by_username(self, username: str):
        user = User.query.filter_by(username=username).first()
        return user
