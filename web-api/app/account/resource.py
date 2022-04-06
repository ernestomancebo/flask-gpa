from app.account.repository.repository import AccountRepository
from app.account.domain.account import Account
from app.auth.token_required import token_required
from app.extensions import db
from app.http.request import json_body_required
from app.http.response import ResponseFailure, ResponseSuccess, ResponseTypes
from app.user.repository.user import User
from flask import abort, make_response
from flask_restful import Resource, request


class AccountResource(Resource):
    """Account related operations"""

    def __init__(self):
        self.account_schema = Account()
        self.accounts_repo = AccountRepository(db)

    # @json_body_required
    @token_required
    def post(self, current_user: User):
        """
        ---
        description: Allows an user to register transactions
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
            - Account Functions
        """
        j = request.json

        # This field is expected by the schema.
        # As we're creating, default this to zero
        errors = self.account_schema.validate(j)

        if errors:
            response = ResponseFailure(ResponseTypes.PARAMETERS_ERROR, str(errors))
            return response.value, 401
            # abort(401, str(errors))

        account: Account = self.account_schema.load(j)
        self.accounts_repo.create_account(account, current_user)

        response = ResponseSuccess("Transaction registered succesfully")
        return response, 201

    @token_required
    def get(self, current_user: User):
        """
        ---
        description: Retrieves all the accounts to the user
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
            - Account Functions
        """
        accounts = self.accounts_repo.get_user_accounts(current_user)
        return accounts, 200
