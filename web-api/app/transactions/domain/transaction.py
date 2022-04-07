from app.transactions.domain.transaction_type import TransactionType
from app.transactions.repository.transaction import Transaction as TransactionModel
from marshmallow import Schema, fields
from marshmallow.decorators import post_load
from marshmallow.validate import ContainsOnly, Length, Range, Regexp

TRANSACTION_PERIOD_PATTERN = r"^\d{6}$"
"""The transaction period must be a four digits string, i.e. 202101 for 2021 January"""


class Transaction(Schema):
    """
    Represents a transaction. Its fields are the following:

    - id: Transaction Id.
    - transaction_type: Can only be DEBIT or CREDIT.
    - amount: An absolute value. Negative values are not accepted.
    In accounting, a Debit (subsctraction) from one account is a Credit (addition) to another.
    - note: The subject of the transaction.
    - account: The destination of the account.
    - performed_by: Determines the user who did this. This is an example exercice, but in real world we must track where the money came from.
    - occurred_at: When did the transaction happened.
    - period: The statement period; i.e., 202101 (Janary 2021).
    """

    id = fields.Integer(required=False, dump_default=0, missing=0)
    transaction_type = fields.String(
        required=True,
        validate=ContainsOnly(TransactionType.CREDIT, TransactionType.DEBIT),
    )
    amount = fields.Float(required=True, validate=Range(min=0.01))
    note = fields.String(required=False, validate=Length(max=255), missing=None)
    account_id = fields.String(required=True, validate=Length(min=4, max=16))
    performed_by = fields.Integer(required=True)
    occurred_at = fields.DateTime(required=False, missing=None)
    period = fields.String(required=False, validate=Regexp(TRANSACTION_PERIOD_PATTERN))

    @post_load
    def create_transaction(self, data, **kwargs):
        return TransactionModel(**data)
