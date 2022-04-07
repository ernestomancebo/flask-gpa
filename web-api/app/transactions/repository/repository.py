from flask_sqlalchemy import SQLAlchemy
from app.transactions.repository.transaction import Transaction
from app.user.repository.user import User
from app.account.repository.account import Account


class TransactionRepository:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def add_transaction(self, transaction: Transaction):
        self.db.session.add(transaction)
        self.db.session.commit()

    def get_transactions_by(self, account_id: int, period: str = None):
        query = self.db.session.query(Transaction).filer(
            Transaction.account == account_id
        )

        if period:
            query = query.filer(Transaction.period == period)

        return query.all()
