import datetime

# Base = declarative_base()
from app.extensions import db
from app.transactions.domain.transaction_type import TransactionType
from sqlalchemy import CheckConstraint, Column, Float, ForeignKey, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.account.repository.account import Account
from app.user.repository.user import User


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
    account_id = Column(Integer(), ForeignKey("account.id"), nullable=False)
    performed_by = Column(Integer(), ForeignKey("user.id"), nullable=False)
    occurred_at = Column(Time(timezone=True), default=datetime.datetime.utcnow)
    period = Column(String(6))

    # Relationships
    user = relationship("User")
    account = relationship("Account")
