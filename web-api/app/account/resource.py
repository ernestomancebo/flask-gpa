from app.account.domain.account import Account
from app.account.repository.account import Account as ModelAccount
from app.account.repository.repository import AccountRepository
from app.auth.token_required import token_required
from app.extensions import db

from app.user.repository.user import User
from flask_restful import Resource, request


class AccountResource(Resource):
    """Account related operations"""

    def __init__(self):
        self.account_schema = Account()
        self.accounts_schema = Account(many=True)
        self.accounts_repo = AccountRepository(db)

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

        # Default initial values
        j["owner"] = current_user.id
        j["balance"] = 0

        # This field is expected by the schema.
        # As we're creating, default this to zero
        errors = self.account_schema.validate(j)

        if errors:
            return {"status": "error", "message": str(errors)}, 400

        account: ModelAccount = self.account_schema.load(j)
        account.id = None
        self.accounts_repo.create_account(account)

        return {"status": "success", "message": "Account registered successfully"}, 201

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
        return self.accounts_schema.dump(accounts), 200
