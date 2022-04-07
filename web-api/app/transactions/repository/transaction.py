import datetime

from app.extensions import db
from app.transactions.domain.transaction_type import TransactionType
from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship


class Transaction(db.Model):
    __tablename__ = "transaction"

    def __init__(
        self,
        id,
        transaction_type,
        amount,
        note,
        account_id,
        performed_by,
        occurred_at,
        period,
    ):
        self.id = id
        self.transaction_type = transaction_type
        self.amount = amount
        self.note = note
        self.account_id = account_id
        self.performed_by = performed_by
        self.occurred_at = occurred_at
        self.period = period

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
    occurred_at = Column(DateTime(), default=datetime.datetime.now())
    period = Column(String(6), nullable=False)

    # Relationships
    user = relationship("User")
    account = relationship("Account")
