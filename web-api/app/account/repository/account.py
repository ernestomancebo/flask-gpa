import datetime

from app.extensions import db
from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship


class Account(db.Model):
    __tablename__ = "account"
    # Multiple users can have the same account number, but must be unique per user
    __table_args__ = (
        # Table Args tuple
        UniqueConstraint("account_number", "owner", name="unique_account_number_owner"),
    )

    def __init__(self, id, account_number, owner, description, balance, creation_date):
        self.id = id
        self.account_number = account_number
        self.owner = owner
        self.description = description
        self.balance = balance
        self.creation_date = creation_date

    id = Column(Integer(), primary_key=True)
    account_number = Column(String(), nullable=False)
    owner = Column(Integer(), ForeignKey("user.id"), nullable=False)
    description = Column(String(100), nullable=False)
    balance = Column(Float(), nullable=False)
    creation_date = Column(DateTime(), default=datetime.datetime.now())

    # Relationships
    user = relationship("User")
