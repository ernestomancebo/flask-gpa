import json

from app.account.repository.repository import AccountRepository
from app.auth.token_required import token_required
from app.extensions import db
from app.http.request import json_body_required
from app.http.response import ResponseFailure, ResponseSuccess, ResponseTypes
from app.transactions.domain.transaction import TRANSACTION_PERIOD_PATTERN, Transaction
from app.transactions.repository.repository import TransactionRepository
from app.transactions.repository.transaction import Transaction
from app.user.repository.user import User
from flask import abort, make_response
from flask_restful import Resource, request


class TransactionResource(Resource):
    """User related operations"""

    def __init__(self):
        self.transaction_schema = Transaction()
        self.transaction_repo = TransactionRepository(db)
        self.accounts_repo = AccountRepository(db)

    # @json_body_required
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
        j = json.loads(bytes.decode(request.data))
        # This field is expected by the schema.
        # As we're creating, default this to zero
        # TODO: check if needed
        # j["id"] = 0
        errors = self.transaction_schema.validate(j)

        if errors:
            response = ResponseFailure(ResponseTypes.PARAMETERS_ERROR, errors)
            return response.value, 401

        transaction: Transaction = self.transaction_schema.load(j)
        subject_account = self.accounts_repo.get_account_by_number(
            transaction.account, current_user
        )
        # Validate that the account exists
        if not subject_account:
            return make_response("Account not found", 401)

        # transaction.account = subject_account.id
        transaction.user = current_user.id

        # Append the transaction and update the account balance
        self.transaction_repo.add_transaction(transaction)
        self.accounts_repo.update_account_balance(transaction)

        response = ResponseSuccess("Transaction registered succesfully")
        return response, 201

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
        account_number = request.args.get("account_number", None)
        period = request.args.get("period", None)

        if not period or not TRANSACTION_PERIOD_PATTERN.match(period):
            return make_response("Invalid period", 401)

        subject_account = self.accounts_repo.get_account_by_number(
            account_number, current_user
        )
        if not subject_account:
            return make_response("Account not found", 401)

        transactions = self.transaction_repo.get_transactions_by(
            subject_account.id, period
        )

        return transactions, 200
