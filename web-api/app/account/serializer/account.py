from app.extensions import ma
from marshmallow import fields
from marshmallow.validate import Length, Range


class AccountSchema(ma.Schema):
    """JSON Account serializer."""

    id: fields.Integer(required=False, dump_default=0)
    account_number: fields.String(required=True, validate=Range(min=17, max=30))
    owner: fields.Integer(require=True)
    description: fields.String(required=False, validate=Length(max=100))
    balance: fields.Float(required=True)
    creation_date: fields.DateTime(required=False)
