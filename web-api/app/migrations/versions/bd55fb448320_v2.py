"""v2

Revision ID: bd55fb448320
Revises: 
Create Date: 2022-04-07 15:48:31.981303

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "bd55fb448320"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # op.alter_column(
    #     "transaction",
    #     "occurred_at",
    #     type_=sa.TIMESTAMP(timezone=False),
    #     nullable=True,
    # )

    # op.execute(
    #     "ALTER TABLE transaction ALTER COLUMN occurred_at TYPE TIMESTAMP without time zone"
    # )

    # -- Create a temporary TIMESTAMP column
    # op.execute(
    #     "ALTER TABLE transaction ADD COLUMN occurred_at_holder TIMESTAMP without time zone NULL;"
    # )

    # -- Copy casted value over to the temporary column
    # op.execute("UPDATE transaction SET occurred_at_holder = occurred_at::TIMESTAMP;")

    # -- Modify original column using the temporary column
    # op.execute(
    #     "ALTER TABLE transaction ALTER COLUMN occurred_at TYPE TIMESTAMP without time zone USING occurred_at_holder;"
    # )

    # -- Drop the temporary column (after examining altered column values)
    # op.execute("ALTER TABLE transaction DROP COLUMN occurred_at_holder;")
    pass


def downgrade():
    pass
