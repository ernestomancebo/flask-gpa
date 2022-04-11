import json

from app.auth.token_required import token_required
from app.extensions import db
from app.http.response import ResponseFailure, ResponseSuccess, ResponseTypes
from app.user.domain.user import User
from app.user.domain.user_roles import UserRoles
from app.user.repository.repository import UserRepository
from flask_restful import Resource, request


class UserResource(Resource):
    """User related operations"""

    def __init__(self):
        self.user_schema = User()
        self.user_repo = UserRepository(db)

    @token_required
    def post(self, current_user: User):
        """
        ---
        description: Allow admin user to create other users
        security:
            - jwt: []
        parameters:
            - in: body
              name: data
              required: true
              schema:
                type: User
              description: User object to be created. The field id is not required.
        responses:
            "201":
                description: User Created
            "401":
                description: Bad Request. Invalid parameters.
            "403":
                description: Bad Request. Unauthorized.
        tags:
            - User Functions
        """

        if current_user.role != UserRoles.ADMIN:
            response = ResponseFailure(ResponseTypes.PARAMETERS_ERROR, "Unauthorized")
            return response.value, 403

        j = json.loads(bytes.decode(request.data))
        # This field is expected by the schema.
        # As we're creating, default this to zero
        errors = self.user_schema.validate(j)

        if errors:
            response = ResponseFailure(ResponseTypes.PARAMETERS_ERROR, errors)
            return response.value, 401
            # abort(401, str(errors))

        # Setting this back to None, thus
        # the db engine generates the id
        j["id"] = None
        user = User(**j)
        self.user_repo.add_user(user)

        return {"status": "success", "message": "User registered successfully"}, 201
