"""OpenAPI v3 Specification"""

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from app.transactions.serializer.transaction import TransactionSchema
from app.user.serializer.user import UserSchema

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
spec.components.schema("User", schema=UserSchema)
spec.components.schema("Transaction", schema=TransactionSchema)


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
