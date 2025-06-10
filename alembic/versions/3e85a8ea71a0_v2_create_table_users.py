"""v2_create_table_users

Revision ID: 3e85a8ea71a0
Revises: a42bb23752b2
Create Date: 2025-06-10 10:18:17.914805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e85a8ea71a0'
down_revision: Union[str, None] = 'a42bb23752b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String),
        sa.Column('hashed_password', sa.String)
    )


def downgrade() -> None:
    op.drop_table('users')