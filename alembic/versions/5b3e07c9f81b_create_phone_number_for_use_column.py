"""Create phone number for use column

Revision ID: 5b3e07c9f81b
Revises:
Create Date: 2025-11-11 21:49:04.221837

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5b3e07c9f81b"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # to run this upgrade: "alembic updgrade 5b3e07c9f81b"

    # Add columns as non-nullable
    """Upgrade schema."""
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))

    # Updtad existing records with a default value
    op.execute("UPDATE users SET phone_number = '' WHERE phone_number IS NULL")

    # Make it non-nullable
    op.alter_column("users", "phone_number", nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    # to run this downgrade: "alembic downgrade 5b3e07c9f81b"
    op.drop_column("users", "phone_number")
