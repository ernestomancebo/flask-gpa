"""Flask views/resources exposure"""


from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from app.auth.resource import AuthenticateResource
from app.user.resource import UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(UserResource, "/user", endpoint="user")
api.add_resource(
    AuthenticateResource, "/user/authentication", endpoint="user-authentication"
)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_err(e):
    return jsonify(e.messages), 400
