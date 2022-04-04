from datetime import datetime


class Transaction:
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

    id: int
    transaction_type: str
    amount: float
    note: str
    account: int
    performed_by: int
    occurred_at: datetime
    period: str
