import datetime

from app.extensions import db
from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Time,
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

    id = Column(Integer(), primary_key=True)
    account_number = Column(Integer(), nullable=False)
    owner = Column(Integer(), ForeignKey("user.id"), nullable=False)
    description = Column(String(100), nullable=False)
    balance = Column(Float(), nullable=False)
    creation_date = Column(Time(timezone=True), default=datetime.datetime.utcnow)

    # Relationships
    user = relationship("User")
