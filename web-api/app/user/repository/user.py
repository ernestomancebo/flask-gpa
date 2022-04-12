from app.extensions import db, pwd_context
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = "user"

    def __init__(self, id, name, username, email, password, role):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    _password = Column("password", String(255), nullable=False)
    role = Column(String(15), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)

    def __repr__(self):
        return "<User %s>" % self.username
