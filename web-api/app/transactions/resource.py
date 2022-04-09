from datetime import datetime, timedelta

from app.account.repository.repository import AccountRepository
from app.auth.token_required import token_required
from app.extensions import db
from app.transactions.domain.transaction import Transaction
from app.transactions.repository.repository import TransactionRepository
from app.transactions.repository.transaction import Transaction as TransactionModel
from app.user.repository.user import User
from flask_restful import Resource, request


class TransactionResource(Resource):
    """User related operations"""

    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self):
        self.transaction_schema = Transaction()
        self.transaction_list_schema = Transaction(many=True)
        self.transaction_repo = TransactionRepository(db)
        self.accounts_repo = AccountRepository(db)

    @token_required
    def post(self, current_user: User):
        """
        ---
        description: Allow user to register a atransation in an account
        security:
            - jwt: []
        parameters:
            - in: body
              name: data
              required: true
              schema:
                type: Transaction
              description: bla bla
        responses:
            "201":
                description: bla bla bla
            "401":
                description: Bad Request. Invalid parameters.
            "403":
                description: Bad Request. Unauthorized.
        tags:
            - Transaction Functions
        """
        j = request.json
        j["performed_by"] = current_user.id
        # 202201 for 2022 January
        j["period"] = datetime.now().strftime("%Y%m")

        errors = self.transaction_schema.validate(j)

        if errors:
            return {
                "status": "error",
                "message": str(errors),
            }, 400

        transaction: Transaction = self.transaction_schema.load(j)
        subject_account = self.accounts_repo.get_account_by_number(
            transaction.account_id, current_user
        )
        # Validate that the account exists
        if not subject_account:
            return {
                "status": "error",
                "message": f"Account {transaction.account_id} not found",
            }, 404

        transaction.id = None
        transaction.account_id = subject_account.id
        # Append the transaction and update the account balance
        self.transaction_repo.add_transaction(transaction)
        self.accounts_repo.update_account_balance(
            subject_account, transaction, current_user
        )

        return {
            "status": "success",
            "message": "Transaction registered succesfully",
        }, 201

    @token_required
    def get(self, current_user: User):
        """
        ---
        description: Retrieves all the transactions for an account at a given period
        security:
            - jwt: []
        parameters:
            - in: body
              name: data
              required: true
              schema:
                type: Transaction
              description: bla bla
        responses:
            "201":
                description: bla bla bla
            "401":
                description: Bad Request. Invalid parameters.
            "403":
                description: Bad Request. Unauthorized.
        tags:
            - Transaction Functions
        """
        (account_number, date_start, date_end) = (
            request.args.get("account_number", None),
            request.args.get("date_start", None),
            request.args.get("date_end", None),
        )

        try:
            (date_start, date_end) = self.extract_date_range(date_start, date_end)
        except ValueError as err:
            return {"status": "error", "message": str(err)}, 400
        except RuntimeError as err:
            return {"status": "error", "message": str(err)}, 500

        # If account number is present
        subject_account = None
        if account_number:
            subject_account = self.accounts_repo.get_account_by_number(
                account_number, current_user
            )

            if not subject_account:
                return {"status": "error", "message": "Account not found"}, 404

        transactions = self.transaction_repo.get_transactions_by(
            current_user, subject_account, date_start, date_end
        )

        return self.transaction_list_schema.dump(transactions), 200

    def extract_date_range(self, date_start: str, date_end: str):

        if date_start and date_end:
            try:
                date_start = datetime.strptime(date_start, self.DATE_FORMAT)
                date_end = datetime.strptime(date_end, self.DATE_FORMAT)
                # Put it at the end of the day
                date_end = date_end.replace(hour=23, minute=59, second=59)
            except ValueError as err:
                raise ValueError(f"Invalid values: {err}")
            else:
                raise RuntimeError(f"An error occurred: {err}")
            finally:
                return (date_start, date_end)

        today_date = datetime.now()
        if date_start and not date_end:
            try:
                date_start = datetime.strptime(date_start, self.DATE_FORMAT)
            except ValueError as err:
                raise ValueError(f"Invalid values: {err}")
            else:
                raise RuntimeError(f"An error occurred: {err}")
            finally:
                return (date_start, today_date)

        # there are no date_start and no date_end
        # We search from last week
        start_date = today_date.replace(
            hour=0, minute=0, second=0, microsecond=0
        ) - timedelta(days=7)
        return (start_date, today_date)
