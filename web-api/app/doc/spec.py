"""OpenAPI v3 Specification"""

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from app.account.domain.account import Account
from app.transactions.domain.transaction import Transaction
from app.user.domain.user import User

spec = APISpec(
    title="GPA API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Security Schema
jwt_scheme = {
    "type": "http",
    "in": "header",
    "name": "x-access-tokens",
    "bearerFormat": "JWT",
}

spec.components.security_scheme("jwt", jwt_scheme)

# Schemas
spec.components.schema("User", schema=User)
spec.components.schema("Transaction", schema=Transaction)


# Tags for Enpoint annotations
tags = [
    {"name": "User Functions", "description": "Operations related to the Users"},
    {"name": "Account Functions", "description": "Operations related to the Accounts"},
    {
        "name": "Transaction Functions",
        "description": "Operations related to the Transactions",
    },
]

for t in tags:
    spec.tag(t)
