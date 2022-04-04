import datetime

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Time, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.transactions.domain.transaction_type import TransactionType

# Base = declarative_base()
from app.extensions import db

class Transaction(db.Model):
    __tablename__ = "transaction"

    id = Column(Integer(), primary_key=True)
    transaction_type = Column(
        String(6),
        CheckConstraint(
            f"transaction_type IN ('{TransactionType.DEBIT}', '{TransactionType.CREDIT}')"
        ),
    )
    amount = Column(Float(), nullable=False)
    note = Column(String(255), nullable=False)
    account = Column(Integer(), ForeignKey("account.id"))
    performed_by = Column(Integer(), ForeignKey("user.id"))
    occurred_at = Column(Time(timezone=True), default=datetime.datetime.utcnow)
    period = Column(String(6))

    # Relationships
    user = relationship("User")
    account = relationship("Account")
