from app.extensions import ma
from app.user.domain.user import User
from app.user.domain.user_roles import UserRoles
from marshmallow import fields
from marshmallow.decorators import post_load
from marshmallow.validate import ContainsOnly, Email, Length


class UserSchema(ma.Schema):
    """JSON User serializer."""

    id = fields.Integer(required=False, dump_default=0)
    name = fields.String(validate=Length(max=80), required=True)
    username = fields.String(validate=Length(max=80), required=True)
    email = fields.String(validate=Email, required=True)
    password = fields.String(validate=Length(max=255), required=True)
    active = fields.Boolean(required=False, dump_default=True)
    # Roles can be only the defined at UserRoles class.
    role = fields.String(
        validate=(
            ContainsOnly(UserRoles.USER, UserRoles.ADMIN)
        ),
        required=True,
    )

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
