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

    def get_transactions_by(
        self, current_user: User, account: Account, date_start, date_end
    ):
        query = self.db.session.query(Transaction).filter(
            Transaction.performed_by == current_user.id
        )
        query = query.filter(Transaction.occurred_at >= date_start)
        query = query.filter(Transaction.occurred_at <= date_end)

        if account:
            query = query.filter(Transaction.account_id == account.id)

        # Load the account, so we can get the number in the frontend
        query = query.join(Account)
        return query.all()
