from functools import wraps

import jwt
from app.http.response import ResponseFailure, ResponseTypes
from app.user.repository.user import User
from flask import current_app, request


def token_required(f):
    """JWT generator"""

    @wraps(f)
    def decorator(*args, **kwargs):
        TOKEN_HEADER = "x-access-tokens"

        if TOKEN_HEADER not in request.headers:
            response = ResponseFailure(
                ResponseTypes.PARAMETERS_ERROR, "Authentication Token is missing"
            )
            return response.value, 403

        token = request.headers[TOKEN_HEADER]

        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], "HS256")
            current_user = User.query.filter_by(id=data["public_id"]).first()
        except:
            response = ResponseFailure(
                ResponseTypes.PARAMETERS_ERROR, "A valid Token is missing"
            )
            return response.value, 403

        return f(*args, current_user, **kwargs)

    return decorator
