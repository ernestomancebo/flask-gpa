import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Account:
    """
    Domain representation of a banking account.

    The properties of this entity are:
    - id: a database identificator.
    - account_number: The account number. Can be different from ID,
    because is a business related value.
    - owner: The customer id who owns this account.
    - description: An user arbitrary description (i.e. Vacation Savings).
    - amount: The current amount.

    The number of the account. For US accounts, it can be up to 17 digits,
     for europeans accounts can be up to 30.
    More details can be seen here:
    https://www.sapling.com/8038665/bank-account-number-standards
    For the sake of the example we're keeping this as simple as only digits of 17.
    """

    id: int
    account_number: str
    owner: int
    description: str
    balance: float
    creation_date: datetime
