# from app.extensions import ma
from marshmallow import fields, Schema
from marshmallow.validate import Length, Range


class Account(Schema):
    """
    Domain representation of an account.

    The properties of this entity are:
    - id: a database identificator.
    - account_number: The account number. Can be different from ID,
    because is a business related value.
    - owner: The customer id who owns this account.
    - description: An user arbitrary description (i.e. Vacation Savings).
    - amount: The current amount.
    """

    id = fields.Integer(required=False, dump_default=0)
    account_number = fields.String(required=True, validate=Range(min=4, max=6))
    owner = fields.Integer(require=True)
    description = fields.String(required=False, validate=Length(max=100))
    balance = fields.Float(required=True)
    creation_date = fields.DateTime(required=False)
