from datetime import datetime, timedelta

import jwt
from app.extensions import pwd_context
from app.user.domain.user import User
from flask import current_app, request
from flask.helpers import make_response
from flask_restful import Resource


class AuthenticateResource(Resource):
    """Authentication related Operations"""

    def __init__(self):
        user_service = None

    def post(self):
        """
        ---
        description: Authenticates an user
        responses:
            "200":
                description: Login Successful
            "401":
                description: Bad Request. Invalid parameters.
        tags:
            - User Functions
        """
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response(
                "could not verify",
                401,
                {"WWW.Authentication": 'Basic realm: "login required"'},
            )

        user: User = self.user_service.get_by_username(auth.username)
        if pwd_context.verify(auth.password, user.password):
            token = jwt.encode(
                {
                    "public_id": user.id,
                    "exp": datetime.utcnow() + timedelta(minutes=30),
                },
                current_app.config["SECRET_KEY"],
            )

            return {"token": token}, 200

        return make_response(
            "could not verify",
            401,
            {"WWW.Authentication": 'Basic realm: "login required"'},
        )
