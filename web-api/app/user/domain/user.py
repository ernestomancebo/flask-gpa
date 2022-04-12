from app.user.domain.user_roles import UserRoles
from marshmallow import Schema, fields
from marshmallow.decorators import post_load
from marshmallow.validate import ContainsOnly, Email, Length


class User(Schema):
    """
    Representation of a GPA System user.
    """

    id = fields.Integer(required=False, dump_default=0)
    name = fields.String(validate=Length(max=80), required=True)
    username = fields.String(validate=Length(max=80), required=True)
    email = fields.String(validate=Email, required=True)
    # Password can't see the light of the outter world
    password = fields.String(validate=Length(max=255), required=True, load_only=True)
    active = fields.Boolean(required=False, dump_default=True)
    # Roles can be only the defined at UserRoles class.
    role = fields.String(
        validate=(ContainsOnly(UserRoles.USER, UserRoles.ADMIN)),
        required=True,
    )

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
