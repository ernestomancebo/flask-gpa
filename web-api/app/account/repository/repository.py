from app.account.domain.account import Account as DomainAccount
from app.account.repository.account import Account
from app.transactions.domain.transaction import Transaction
from app.transactions.domain.transaction_type import TransactionType
from app.user.domain.user import User
from flask_sqlalchemy import SQLAlchemy


class AccountRepository:
    """Repository for Account"""

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def create_account(self, account: Account, user: User):
        """Creates a new account"""
        account.owner = user.id
        new_account = self.db.session.add(account)
        self.db.session.commit()

        return new_account

    def get_user_accounts(self, user: User):
        """Get all the accounts given the user"""
        user_accounts = (
            self.db.session.query(Account).filter(Account.owner == user.id).all()
        )

        return user_accounts

    def get_account_by_number(self, account_number: int, user: User):
        """Retrieves the given account by the given account number"""
        user_account = (
            self.db.session.query(Account)
            .filter(
                Account.account_number == account_number and Account.owner == user.id
            )
            .first()
        )

        return user_account

    def update_account(self, account: DomainAccount):
        pass

    def update_account_balance(
        self, account: DomainAccount, transaction: Transaction, user: User
    ):
        """Updates the account account balance given the transaction"""
        # Debit goes as posivite, Credit as negative
        transaction_amount = abs(transaction.amount)
        if transaction.transaction_type == TransactionType.CREDIT:
            transaction_amount = -1 * transaction_amount

        # Update the corresponding account
        self.db.session.query(account).filter(
            Account.account_number == account.account_number
            and Account.owner == user.id
        ).update(
            {Account.balance: Account.balance + transaction_amount},
            synchronize_session=False,
        )
        self.db.session.commit()
