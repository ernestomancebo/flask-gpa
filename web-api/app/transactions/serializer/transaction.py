from app.extensions import ma
from app.transactions.domain.transaction import Transaction
from app.transactions.domain.transaction_type import TransactionType
from marshmallow import fields
from marshmallow.decorators import post_load
from marshmallow.validate import ContainsOnly, Length, Range


class TransactionSchema(ma.Schema):
    """JSON Transaction serializer"""

    id = fields.Integer(required=False, dump_default=0)
    transaction_type: fields.String(
        required=True,
        validate=ContainsOnly(TransactionType.CREDIT, TransactionType.DEBIT),
    )
    amount: fields.Float(required=True, validate=Range(min=0.01))
    note: fields.String(required=False, validate=Length(max=255))
    account: fields.String(required=True, validate=Length(min=17, max=30))
    performed_by: fields.Integer(required=True)
    occurred_at: fields.DateTime(required=True)
    period: fields.String(required=False)

    @post_load
    def create_transaction(self, data, **kwargs):
        return Transaction(**data)
